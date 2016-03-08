# MC723 -Exerc�cio 1
Aluno Luiz Rodolfo Felet Sekijima

RA 117842

Para todos os tempos de processamento dos programas exibidos a seguir, os testes foram executados em uma mesma maquina no IC, calculando a m�dia de 50 execu��es, tentando gerar condi��es iguais para todas as simula��es. Os valores tem precis�o de 0.001s, a menor medida de tempo do comando "time", por isso os valores foram arrendados.

## primo.c n�o otimizado
O programa que calcula se um inteiro � um primo disponibilizado para o exerc�cio se encontra no subdiret�rio "exercicio1/original" e foi compilado sem nenhuma flag de otimiza��o com o seguinte comando:

```bash
gcc primo.c -o primo
```
E com o seguinte resultado de tempo de execu��o:

~~~
real	0.3071s
user	0.30556s
sys	    0.00064s
~~~
Este ser� o tempo base para podermos determinar as melhores otmiza��es feitas sobre o programa original.

### Otimiza��o por flags -O (gcc)


O compilador gcc permite no momento de compila��o do programa setar flags que melhoram o tamanho e tempo de execu��o do c�digo compilado ao custo de tempo e mem�ria no momento de compila��o.




A seguir vemos como as flags de otimizagco do gcc influjncia os tempos de execugco:

-O0
~~~
real	0.3016s
user	0.30054s
sys	    0.00036s
~~~
-O1
~~~
real	0.26174s
user	0.25934s
sys		0.00044s
~~~

-O2
~~~
real	0.28886s
user	0.28796s
sys		0.00038s
~~~

-O3
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
[] 

[] 
