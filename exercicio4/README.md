# Exercício 4: Plataformas e Periféricos
Aluno Luiz Rodolfo Felet Sekijima

RA 117842

Para o exercício 4 de MC723 nos foi proposto implementar periféricos e plataforma multicore no simulador MIPS.


## Periférico Básico

O periférico implementado em [ac_tlm_peripheral.cpp](mips-tlm/ac_tlm_peripheral.cpp) tem a seguinte função: toda escrita em um endereço base grava o valor determinado, e a leitura retorna o valor no endereço base e muda o valor armazenado para 1. O endereço base é o primeiro endereço de memória do periférico (0x6400000).
O periférico é útil para controle de concorrência, para restringir a modificação de uma região crítica de memória.

~~~~c
ac_tlm_rsp_status ac_tlm_peripheral::writem( const uint32_t &a , const uint32_t &d ){
  cout << "addr: " <<  std::hex  << a << " data: " << d << endl;
  value = d;
  return SUCCESS;
}
ac_tlm_rsp_status ac_tlm_peripheral::readm( const uint32_t &a , uint32_t &d ){
  d = value;
  value = 1;
  return SUCCESS;
}
~~~~

Por causa de conversão de endian se escrevermos 1 no periférico na leitura deste valor veremos o valor 16777216, que em hexadecimal é o valor 0x01000000 em notação big endian.

### Teste do periférico - Programa hello.c

O programa faz diversas leituras e escritas no endereço indicado para comprovar o funcionamento do periférico. Abaixo vemos a função main de [hello.c](mips-tlm/hello.c)

~~~~c
#define LOCK_ADDRESS 0x6400000 /*endereço 104857600*/
main(){
        printf("Hello world\n");
        printf("Imprimindo valor inicial do lock\n");
        printf("Valor:%d\n",*lock);
        printf("Mudando valor do lock para 1\n");
        *lock = 1;
        printf("Imprimindo valor do lock\n");
        printf("Valor:%d\n",*lock);
        printf("Mudando valor do lock para 2\n");
        *lock = 2;
        printf("Imprimindo valor inicial do lock\n");
        printf("Valor:%d\n",*lock);
        printf("Imprimindo valor inicial do lock\n");
        printf("Valor:%d\n",*lock);
        return 0;
}
~~~~

E a saída do programa:

~~~
ArchC: Reading ELF application file: hello.mips
ArchC: -------------------- Starting Simulation --------------------

Hello world
Imprimindo valor inicial do lock
Valor:0
Mudando valor do lock para 1
addr: 6400000 data: 1000000
Imprimindo valor do lock
Valor:1
Mudando valor do lock para 2
addr: 6400000 data: 2000000
Imprimindo valor inicial do lock
Valor:2
Imprimindo valor inicial do lock
Valor:16777216
ArchC: -------------------- Simulation Finished --------------------

Info: /OSCI/SystemC: Simulation stopped by user.
ArchC: Simulation statistics
    Times: 0.00 user, 0.00 system, 0.00 real
    Number of instructions executed: 18607
    Simulation speed: (too fast to be precise)
~~~

Vemos então o programa lendo e escrevendo valores no endereço 0x6400000, e vemos que se tentarmos fazer duas leituras consecutivas, na segunda leitura o valor será 16777216, isso pois a cada leitura o periférico grava este valor. Este comportamento que é útil para controle de concorrência.


## Plataforma multicore

Para analisar a plataforma multicore do simulador um programa que calcula os divisores de um inteiro **n** foi utilizado para calcular sua eficiência rodando em um único processador ou em dois.
O programa vai calcular os divisores de 367567200, pois este número possui 1150 mútiplos, para que os processadores tenham que usar a região crítica com frequência. Assim, o teste com dois processadores será feito da seguinte forma: um processador ficará encarregado em calcular os multiplos ímpares e outro calculará os pares, quando um múltiplo for encontrado o programa entra na região crítica e escreve em um vetor o valor e o contador de multiplos será atualizado. No final do programa será impresso o total de múltiplos e o vetor com os valores. O progama com um único processador realiza todos os procedimentos que o de múltiplos processadores, mas apenas o primerio processador faz os calculos de múltiplos.
Abaixo vemos o loop principal do programa:
~~~c
    while(i <= limit){
        if(n%i==0) {
            AcquireLock();
            vetor[number_divs]=i;
            number_divs++;
            ReleaseLock();
        }
        i+=2; //pulando de par para par ou impar para impar
    }
~~~


Assim temos os seguintes resultados para os testes com a plataforma multicore, alguns valores da saída foram cortados para melhor vizualização no relatório mas é possível ver toda a saída nos arquivos .out:

Programa single core ([prime_single.c](mips-tlm/prime_single.c))
~~~
-bash-4.3$ ./mips.x --load=prime_single.mips 
ArchC: Reading ELF application file: prime_single.mips
ArchC: -------------------- Starting Simulation --------------------
O numero 367567200 tem 1150 divisores
2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 20 21 22 24 25 26 27 28 30 32 33 34 35 36 39 40 42 44 45 48 50 51 52 54 55 56 60 63 65 66 68 70 72 75 77 78 80 84 85 88 90 91 96 99 100 102 104 105 108 110 112 117 119 120 126 130 132 135 136 140 143 144 150 153 154 156 160 165 168 170 175 176 180 182 187 189 195 198 200 204 208 210 216 220 221 224 225 231 234 238 240 252 255 260 264 270 272 273 275 280 286 288 297 300 306 308 312 315 325 330 336 340 350 351 352 357 360 364 374 378 385 390 396 400 408 416 420 425 429 432 440 442 450 455 459 462 468 476 480 495 504 510 520 525 528 540 544 546 550 560 561 572 585 594 595 600 612 616 624 630 650 660 663 672 675 680 693 700 702 714 715 720 728 748 756 765 770 780 792 800 ...
ArchC: -------------------- Simulation Finished --------------------

Info: /OSCI/SystemC: Simulation stopped by user.
ArchC: Simulation statistics
    Times: 88.74 user, 0.06 system, 88.78 real
    Number of instructions executed: 1472633250
    Simulation speed: 16594.92 K instr/s

ArchC: Simulation statistics
    Times: 88.74 user, 0.06 system, 88.78 real
    Number of instructions executed: 64
    Simulation speed: 0.00 K instr/s

~~~

Programa multi core ([prime_multi.c](mips-tlm/prime_multi.c))
~~~
-bash-4.3$ ./mips.x --load=prime_multi.mips
ArchC: Reading ELF application file: prime_multi.mips
ArchC: -------------------- Starting Simulation --------------------
O numero 367567200 tem 1150 divisores
2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 21 20 25 22 27 24 33 26 35 28 39 30 45 32 51 34 55 36 63 40 65 42 44 75 48 77 50 52 85 54 91 56 99 60 105 66 68 117 70 119 72 78 135 80 143 84 88 153 90 96 165 100 102 175 104 108 187 110 189 112 195 120 126 130 221 132 225 136 231 140 144 150 255 154 156 160 273 275 168 170 176 297 180 182 315 198 325 200 204 208 351 210 357 216 220 224 385 234 238 240 252 425 260 429 264 270 272 455 280 459 286 288 300 495 306 308 312 525 330 336 340 561 350 352 360 585 364 595 374 378 390 396 400 408 663 416 420 675 432 693 440 442 450 715 462 468 476 480 765 504 510 520 819 528 825 540 544 546 550 560 572 594 600 935 612 945 616 624 630 975 650 1001 660 672 680 700 702 1071 714 720 728 1105 748 756 770 1155 780 792 800 ...
ArchC: -------------------- Simulation Finished --------------------

Info: /OSCI/SystemC: Simulation stopped by user.
ArchC: Simulation statistics
    Times: 81.51 user, 0.02 system, 81.51 real
    Number of instructions executed: 829384962
    Simulation speed: 10175.25 K instr/s

ArchC: Simulation statistics
    Times: 81.51 user, 0.02 system, 81.51 real
    Number of instructions executed: 827031731
    Simulation speed: 10146.38 K instr/s


~~~

### Análise do resultado

Podemos ver que o número de múltiplos encontrados é o mesmo, mas a sequência em que eles são mostrados não é, isso porque o prime_single verifica múltiplos sequêncialmente, enquanto que o prime_multi procura intercalando ímpares e pares entre os processadores. Um problema que o processamento paralalelo pode causar neste caso é se a saída deve estar ordena, então seria necessário ordenar o vetor enquanto que com só um core não seria necessário.
Abaixo vemos os valores de total de instruções executadas e tempo de execução dos programas:

Programa single core ([prime_single.c](mips-tlm/prime_single.c))

| Processador  | Instruções  |
|---|---|
|  0 |1472633250   |
| 1  | 64  |

Programa multi core ([prime_multi.c](mips-tlm/prime_multi.c))

| Processador  | Instruções  |
|---|---|
| 0  | 829384962  |
| 1  | 827031731  |


Aqui vemos ganhos expressivos no programa multicore quanto a quantidade de instruções executadas, ao distribuir o processamento houve uma redução de 43.7% instruções no processador 0. Apesar do número total de instruções ter aumentado, talvez por causa da espera pela liberação do lock, podemos esperar que o segundo programa termine a execução por volta de 43.7% mais rápido.

## Conclusão

A proposta do exercício é o estudo e análise de periféricos e aplicações multicore, para isso um periférico simples para controle de concorrência e uma aplicação multicore foram implementados. O periférico foi utilizado na aplicação para controlar a escrita no vetor de múltiplos, e a aplicação funcionou conforme o esperado, assim, o exercício foi bem sucedido.
