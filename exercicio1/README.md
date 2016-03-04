# MC723 -Exercício 1
Aluno Luiz Rodolfo Felet Sekijima
RA 117842

## primo.c não otimizado
O programa primo.c executado sem nenhuma otimazação de código ou de flags imprime o seguinte resultado, todos os tempos a seguir são mostrados com o calculo de uma média de 50 execuções:
~~~
real	0.3071s
user	0.30556s
sys	    0.00064s
~~~

A seguir vemos como as flags de otimização do gcc influência os tempos de execução:

-O0
~~~
real	0m0.305s
user	0m0.301s
sys     0m0.001s
~~~
-O1
~~~
real	0m0.305s
user	0m0.301s
sys     0m0.001s
~~~

-O2
~~~
real	0m0.305s
user	0m0.301s
sys     0m0.001s
~~~

-O3
~~~
real	0m0.305s
user	0m0.301s
sys     0m0.001s
~~~

A flag que mais reduziu o tempo de execução foi a -O1

Outras flags que podem ser aplicadas são:

-Os
~~~
real	0m0.305s
user	0m0.301s
sys     0m0.001s
~~~

-Ofast
~~~
real	0m0.305s
user	0m0.301s
sys     0m0.001s
~~~
    
-mtune=native
~~~
real	0m0.305s
user	0m0.301s
sys     0m0.001s
~~~

## main.c e calc_primo.c

Separando o programa em dois arquivos (os arquivos deste codigo se encontram em /exercicio1/dois_arquivos), podemos compila-lo novamente usando uma makefile que define as regras de compliação, gerando object files para cada arquivo de código antes de fazer o link entre eles. Estes foram os resultados dos tempos:

Sem flags:
~~~
real	0m0.305s
user	0m0.301s
sys     0m0.001s
~~~

Melhor flag -O:
~~~
real	0m0.305s
user	0m0.301s
sys     0m0.001s
~~~


## calc_primo.c somente com ímpares

## gprof

## Programa paralelizado

