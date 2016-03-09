# MC723 -Exercício 1
Aluno Luiz Rodolfo Felet Sekijima

RA 117842

Para todos os tempos de processamento dos programas exibidos a seguir, os testes foram executados em uma mesma maquina no IC, calculando a média de 50 execuções. Os valores tem precisão de 0.001s, a menor medida de tempo do comando "time", por isso os valores foram arrendados.

## primo.c não otimizado
O programa original disponibilizado para o exercício se encontra no subdiretório "exercicio1/original" e foi compilado sem nenhuma flag de otimização com o seguinte comando:

```bash
gcc primo.c -o primo
```
E com o seguinte resultado de tempo de execução:

~~~
real	0.3071s
user	0.30556s
sys	    0.00064s
~~~

Este será o tempo base para podermos determinar as melhores otmizações feitas sobre o programa original.

### Otimização por *flags* (gcc)


O compilador gcc permite no momento de compilação do programa setar *flags* que são variavéis de ambiente que indicam o modo que deve ser feita a compilação do código fonte. Elas melhoram o tamanho e tempo de execução do código compilado ao custo de tempo e memória no momento de compilação. Estas *flags* podem ser setadas pelas variável "-O", seguida pelo nível de otimização que se deseja.  


A seguir vemos como a otimização via -O do gcc influenciam os tempos de execução e qual seu propósito:


#### -O0

Este é padrão, qualquer programa compilado sem *flags* será processado como "-O0", reduz tempo e memória no momento de compilação e facilita o *debbuging* do programa.  
~~~
real	0.3016s
user	0.30054s
sys	    0.00036s
~~~

#### -O1 ou -O

Nível de otimização basico, tenta reduzir tempo de execução e tamanho do código.

~~~
real	0.26174s
user	0.25934s
sys		0.00044s
~~~

#### -O2
Otimização além de -O1, seta todas as *flags* de -O1 e mais alguns parametros de otimização. Tenta reduzir mais o tempo de execução sem modificar o tamanho do código compilado.

~~~
real	0.28886s
user	0.28796s
sys		0.00038s
~~~

#### -O3

Maior nível de otimização, tenta deixar o código mais rápido possível na execução , o que aumenta em muito o tempo de compilação. No entanto, o uso de -O3 não é garantia de 
~~~
real	0.29582s
user	0.29418s
sys		0.00064s
~~~

A flag que mais reduziu o tempo de execugco foi a -O1

Outras flags que podem ser aplicadas sco:

-Os
~~~
real	0.28832s
user	0.28768s
sys		0.00034s
~~~

-Ofast
~~~
real	0.28996s
user	0.28842s
sys		0.0007s
~~~
    
-mtune=native
~~~
real	0.30314s
user	0.30192s
sys		0.00036s
~~~

## main.c e calc_primo.c

Separando o programa em dois arquivos ("/exercicio1/dois_arquivos"), podemos compila-lo novamente usando uma makefile que define as regras de compliagco, gerando object files para cada arquivo de csdigo antes de fazer o link entre eles. Estes foram os resultados dos tempos:

Sem flags:
~~~
real	0.28956s
user	0.28844s
sys		0.00048s
~~~

Melhor flag -O1:
~~~
real	0.29106s
user	0.29002s
sys		0.00038s
~~~

## Primos entre 1 e n
Para os padronizar o calculo do tempo de execugco destes programas, que calculam o nzmero de primos entre 1 e n, todos os testes foram realizados calculando a quantidade de primos entre 1 e 123456 e sem flags de otimizagco.

### Um arquivo fonte
~~~
real	1.73622s
user	1.73288s
sys		0.00074s
~~~
### Dois arquivos fontes
~~~
real	1.9196s
user	1.91548s
sys		0.00122s
~~~
## calc_primo.c somente com mmpares

~~~
real	1.01936s
user	1.01136s
sys		0.00178s
~~~

## gprof

## Programa paralelizado
~~~
real	0.88822s
user	0.87694s
sys		0.00098s
~~~

# Falta