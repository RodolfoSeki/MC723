# MC723 -Exerc�cio 1
Aluno Luiz Rodolfo Felet Sekijima
RA 117842

## primo.c n�o otimizado
O programa primo.c executado sem nenhuma otimaza��o de c�digo ou de flags est� no subdiret�rio "exercicio1/original", este c�digo imprime o seguinte resultado, todos os tempos a seguir s�o mostrados com o calculo de uma m�dia de 50 execu��es:
~~~
real	0.3071s
user	0.30556s
sys	    0.00064s
~~~

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
Para os padronizar o calculo do tempo de execu��o destes programas, que calculam o n�mero de primos entre 1 e n, todos os testes foram realizados calculando a quantidade de primos entre 1 e 123456 e sem flags de otimiza��o.

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
## calc_primo.c somente com �mpares

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
