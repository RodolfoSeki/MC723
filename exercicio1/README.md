# MC723 -Exerc�cio 1
Aluno Luiz Rodolfo Felet Sekijima

RA 117842

Para todos os tempos de processamento dos programas exibidos a seguir, os testes foram executados em uma mesma maquina no IC, calculando a m�dia de 100 execu��es. Os valores tem precis�o de 0.001s, a menor medida de tempo do comando "time", por isso os valores foram arrendados.

## primo.c n�o otimizado
O programa original disponibilizado para o exerc�cio se encontra no subdiret�rio "exercicio1/original" e foi compilado sem nenhuma flag de otimiza��o com o seguinte comando:

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

### Otimiza��o por *flags* (gcc)


O compilador gcc permite no momento de compila��o do programa setar *flags* que s�o variav�is de ambiente que indicam o modo que deve ser feita a compila��o do c�digo fonte. Elas melhoram o tamanho e tempo de execu��o do c�digo compilado ao custo de tempo e mem�ria no momento de compila��o. Estas *flags* podem ser setadas incluindo no comando do gcc a vari�vel "-O", seguida pelo n�vel de otimiza��o que se deseja.  


A seguir vemos como a otimiza��o via -O do gcc influenciam os tempos de execu��o e qual seu prop�sito:


#### -O0

Este � padr�o, qualquer programa compilado sem *flags* ser� processado como "-O0", reduz tempo e mem�ria no momento de compila��o e facilita o *debbuging* do programa.  
~~~
real	0.3016s
user	0.30054s
sys	    0.00036s
~~~

#### -O1 ou -O

N�vel de otimiza��o b�sico, tenta reduzir tempo de execu��o e tamanho do c�digo.

~~~
real	0.26174s
user	0.25934s
sys		0.00044s
~~~

#### -O2
Otimiza��o al�m de -O1, seta todas as *flags* de -O1 e mais alguns parametros de otimiza��o. Tenta reduzir mais o tempo de execu��o sem modificar o tamanho do c�digo compilado.

~~~
real	0.28886s
user	0.28796s
sys		0.00038s
~~~

#### -O3

Maior n�vel de otimiza��o, tenta deixar o c�digo mais r�pido poss�vel na execu��o, o que aumenta em muito o tempo de compila��o. No entanto, o uso de -O3 n�o � garantia de c�digo mais r�pido, pois os bin�rios podem ser maiores e por causa do maior uso de mem�ria. 
~~~
real	0.29582s
user	0.29418s
sys		0.00064s
~~~

#### -Ofast
Tenta deixar o -O3 mais r�pido mas acaba quebrando os padr�es importantes de compila��o, n�o recomendado.
~~~
real	0.28996s
user	0.28842s
sys		0.0007s
~~~

#### -mtune e -march

Outra otimiza��o poss�vel � a op��o -mtune que tenta ajustar o c�digo favorecendo a sequ�ncia instru��es que ir�o rodar mais r�pida na CPU especificada.

~~~
real	0.30314s
user	0.30192s
sys		0.00036s
~~~


#### Melhor vari�vel de otimiza��o

A vari�vel apresentou a melhor redu��o no tempo de execu��o do programa, era de se esperar que -O2 e -O3 fossem melhores pois ativam mais *flags* de otimiza��o, mas para um c�digo t�o pequeno como esse, apenas duas fun��es, acabaram gerando uma complexidade exagerada no programa devido aos arquivos bin�rios grandes e maior consumo de mem�ria, o que resultou em maior lentid�o na execu��o.

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
MC723 - Checklist Exercicio 1

^Compile o programa sem nenhuma op��o de compila��o extra. 
	Quanto tempo ele gasta?
	Veja se o valor muda utilizando, separadamente, cada uma das otimiza��es -O0, -O1, -O2 -O3 (letra O mai�scula seguida de um n�mero).
		Como especificar as otimiza��es que um compilador deve utilizar num programa?
		Qual delas deu o melhor tempo?
	Existem outras otimiza��es que voc� pode aplicar no processador atual, consulte o manual do gcc por otimiza��es da categoria -mtune e veja quais se aplicam ao seu processador.
		Para que elas servem?
		O tempo melhorou?
	Quais otimiza��es s�o importantes para o processador que voc� est� utilizando?
	
	
Quebre o programa em dois arquivos separados: main.c com a fun��o main e calc_primo.c com a fun��o primo.
Fa�a as altera��es necess�rias nos dois arquivos para que eles compilem.
	Como compil�-los?
	Voc� consegue montar um script que compile estes dois programas?
	E um Makefile? 
	Qual a diferen�a entre um Makefile e um script?
Rode novamente o programa e veja se ele gasta o mesmo tempo com a melhor otimiza��o utilizada anteriormente.
	O resultado foi o esperado? Comente.
	
Modifique seu programa para calcular quantos n�meros primos existem entre 1 e n, seguindo o mesmo algoritmo utilizado, modificando apenas a fun��o main e fazendo com que n seja um par�metro passado por linha de comando.
	Me�a o tempo com um arquivo fonte e com dois.
	O resultado foi o esperado? Comente.

Agora � hora de tentar melhorar um pouco o programa (mas n�o muito ainda).
Edite o la�o da fun��o primo para varrer apenas os n�meros �mpares, dividindo o conjunto de n�meros a testar por dois.
Lembre-se que o resultado deve ser o mesmo para a mesma entrada! Caso encontre algum problema, utilize o GDB para depurar seu programa.
Muitas vezes, a interface em modo texto do GDB dificulta a depura��o, recomendo que voc�s utilizem um visualizador gr�fico para o GDB.
Um bom visualizador � o DDD (basta executar ddd na linha de comando).
Alguns comandos interessantes do GDB que voc� deve saber utilizar: breakpoint, watchpoint, print, display, run, set args e help.
O que � "depurar um programa"?
Como executar o GDB?
Como utilizar um ambiente gr�fico com o GDB?


Em qual parte seu programa gasta mais tempo? use o gprof para descobrir
Como descobrir a parte que � mais executada de um programa?
Como utilizar o gprof?



Se voc� tiver que paralelizar alguma parte do c�digo, qual parte voc� escolheria?
Como paralelizar de forma escal�vel o c�digo?
Como fazer com que um programa tire proveito de multiprocessamento de forma escal�vel?
Eu sugiro utilizar OpenMP, veja um tutorial, o site oficial, uso pelo GCC e implementa��o GNU do for.
	Me�a o tempo do programa paralelizado.
	O resultado foi o esperado? Comente.

Como melhorar ainda mais o desempenho deste programa?

