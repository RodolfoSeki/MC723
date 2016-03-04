# MC723 -Exerc�cio 1
Aluno Luiz Rodolfo Felet Sekijima
RA 117842

## primo.c n�o otimizado
O programa primo.c executado sem nenhuma otimaza��o de c�digo ou de flags imprime o seguinte resultado, todos os tempos a seguir s�o mostrados com o calculo de uma m�dia de 10 execu��es:
~~~
real	0m0.305s
user	0m0.301s
sys     0m0.001s
~~~

A seguir vemos como as flags de otimiza��o do gcc influ�ncia os tempos de execu��o:

-O0
  : ~~~
    real	0m0.300s
    user	0m0.300s
    sys 	0m0.000s
    ~~~
-O1
  : ~~~
    real	0m0.260s
    user	0m0.260s
    sys 	0m0.000s
    ~~~

-O2
  : ~~~
    real	0m0.287s
    user	0m0.287s
    sys	    0m0.000s
    ~~~

-O3
  : ~~~
    real	0m0.288s
    user	0m0.287s
    sys	    0m0.000s
    ~~~

A flag que mais reduziu o tempo de execu��o foi a -O1

Outras flags que podem ser aplicadas s�o:

-Os
  : ~~~
    real	0m0.288s
    user	0m0.287s
    sys	    0m0.000s
    ~~~

-Ofast
  : ~~~
    real	0m0.288s
    user	0m0.287s
    sys	    0m0.000s
    ~~~
    
-mtune=native
  : ~~~
    real	0m0.288s
    user	0m0.287s
    sys	    0m0.000s
    ~~~

## main.c e calc_primo.c

Separando o programa em dois arquivos (os arquivos deste codigo se encontram em /exercicio1/dois_arquivos), podemos compila-lo novamente usando uma makefile que define as regras de complia��o, gerando object files para cada arquivo de c�digo antes de fazer o link entre eles. Estes foram os resultados dos tempos:

Sem flags:
  : ~~~
    real	0m0.288s
    user	0m0.287s
    sys	    0m0.000s
    ~~~

Melhor flag -O:
  : ~~~
    real	0m0.288s
    user	0m0.287s
    sys	    0m0.000s
    ~~~


## calc_primo.c somente com �mpares

## gprof

## Programa paralelizado

