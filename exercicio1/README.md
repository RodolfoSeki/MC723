# MC723 -Exerc�cio 1
Aluno Luiz Rodolfo Felet Sekijima

RA 117842

Para todos os tempos de processamento dos programas exibidos a seguir, os testes foram executados em uma mesma maquina no IC, com processador i5-3570 de 4 *cores*, calculando a m�dia de 100 execu��es. Os valores tem precis�o de 0.001s, a menor medida de tempo do comando "time", por isso os valores foram arrendados.

## primo.c n�o otimizado
O programa original disponibilizado para o exerc�cio se encontra no subdiret�rio "exercicio1/original" e foi compilado sem nenhuma flag de otimiza��o com o seguinte comando:

```bash
gcc primo.c -o primo
```
E com o seguinte resultado de tempo de execu��o:

~~~
real	0.307s
user	0.305s
sys		0.001s
~~~

Este ser� o tempo base para podermos determinar as melhores otmiza��es feitas sobre o programa original.

### Otimiza��o por *flags* (gcc)


O compilador gcc permite no momento de compila��o do programa setar *flags* que s�o variav�is de ambiente que indicam o modo que deve ser feita a compila��o do c�digo fonte. Elas melhoram o tamanho e tempo de execu��o do c�digo compilado ao custo de tempo e mem�ria no momento de compila��o. Estas *flags* podem ser setadas incluindo no comando do gcc a vari�vel "-O", seguida pelo n�vel de otimiza��o que se deseja.  


A seguir vemos como a otimiza��o via -O do gcc influenciam os tempos de execu��o e qual seu prop�sito:


#### -O0

Este � padr�o, qualquer programa compilado sem *flags* ser� processado como "-O0", reduz tempo e mem�ria no momento de compila��o e facilita o *debbuging* do programa.  
~~~
real	0.299s
user	0.298s
sys		0.001s
~~~

#### -O1 ou -O

N�vel de otimiza��o b�sico, tenta reduzir tempo de execu��o e tamanho do c�digo.

~~~
real	0.269s
user	0.268s
sys		0.001s
~~~

#### -O2
Otimiza��o al�m de -O1, seta todas as *flags* de -O1 e mais alguns parametros de otimiza��o. Tenta reduzir mais o tempo de execu��o sem modificar o tamanho do c�digo compilado.

~~~
real	0.295s
user	0.295s
sys		0.000s
~~~

#### -O3

Maior n�vel de otimiza��o, tenta deixar o c�digo mais r�pido poss�vel na execu��o, o que aumenta em muito o tempo de compila��o. No entanto, o uso de -O3 n�o � garantia de c�digo mais r�pido, pois os bin�rios podem ser maiores e por causa do maior uso de mem�ria. 
~~~
real	0.296s
user	0.295s
sys		0.001s
~~~

#### -Ofast
Tenta deixar o -O3 mais r�pido mas acaba quebrando os padr�es importantes de compila��o, n�o recomendado.
~~~
real	0.292s
user	0.291s
sys		0.001s
~~~

#### -mtune

Outra otimiza��o poss�vel � a op��o -mtune que tenta ajustar o c�digo favorecendo a sequ�ncia instru��es que ir�o rodar mais r�pida na CPU especificada.

O computador utilizado � da fam�lia Ivy Bridge da Intel, mas outros parametros de otimiza��o que podem ser aplicados s�o o *intel*, com c�digo otimizado para a s vers�se mais atuais de processadores da Intel, e o *native*, em que o compilador tenta determinar o tipo de processador. 

##### -mtune=ivybridge
~~~
real	0.298s
user	0.297s
sys		0.001s
~~~

##### -mtune=intel
real	0.274s
user	0.273s
sys		0.001s

##### -mtune=native

real	0.300s
user	0.298s
sys		0.001s


#### Melhor vari�vel de otimiza��o

A vari�vel -O1 apresentou a melhor redu��o no tempo de execu��o do programa, era de se esperar que -O2 e -O3 fossem melhores pois ativam mais *flags* de otimiza��o, mas para um c�digo t�o pequeno como esse, apenas duas fun��es, mais flags de otimiza��o acabaram gerando uma complexidade exagerada no programa devido aos arquivos bin�rios grandes e maior consumo de mem�ria, o que resultou em maior lentid�o na execu��o.

## main.c e calc_primo.c

Separando o programa em dois arquivos ("/exercicio1/dois_arquivos"), podemos compila-lo usando um *makefile*, o *makefile* � um arquivo que define as diretivas de complia��o. Para o programa primo, ele gera um *object file* para cada arquivo fonte e ent�o faz o *link* entre eles. Estes foram os resultados dos tempos:

### Sem flags
~~~
real	0.297s
user	0.296s
sys		0.001s
~~~

### -O1
~~~
real	0.297s
user	0.293s
sys		0.001s
~~~

Vemos que os tempos de execu��o foram praticamente iguais e muito pr�ximo do tempo de execu��o um �nico arquivo sem flags, o que mostra que as otimiza��es da vari�vel -O1 talvez n�o afetem a velocidade de execu��o do programa quando ele � separado em dois arquivos.

Al�m de compilar via *makefile*, � possivel criar um *script* bash que executa os mesmos comandos de compila��o. O resultado na execu��o do c�digo ser� o mesmo, no entanto, o *makefile* � prefer�vel ao *script* pois na hora de recompilar um programa, o *makefile* apenas recompila aqueles arquivos que foram alterados ap�s a �ltima chamada do *make* 

## Primos entre 1 e n

Para os padronizar o calculo do tempo de execu��o dos programas a seguir, que calculam o n�mero de primos entre 1 e n, todos os testes foram realizados calculando a quantidade de primos entre 1 e 123456 e sem flags de otimiza��o.

### Um arquivo fonte
~~~
real	1.675s
user	1.673s
sys		0.001s
~~~
### Dois arquivos fontes
~~~
real	1.859s
user	1.856s
sys		0.002s
~~~

Podemos ver que o programa compilado de um �nico arquivo fonte � mais r�pido na execu��o, o que pode indicar que o *linker* do gcc deixe o programa com dois arquivos fontes ligeiramente mais devagar.

### verificando apenas �mpares

Reescrevendo o la�o que procura divisores de um n�mero n, dividimos pela metade o n�mero de testes feitos por n�mero, para o programa de calculo de primos com dois arquivos, vemos a seguir o resultado desta altera��o:

~~~
real	0.956s
user	0.952s
sys		0.001s
~~~

Vemos que o tempo reduziu bastaste, praticamente metade da vers�o com dois arquivos, isso pode ser explicado pelo fato de que o programa passa a maior parte do tempo executando a fun��o primo, que ser�  visto quando usarmos a ferramenta *gprof*.

## Ferramentas

Podemos utilizar ferramentas na hora de depurar um programa e fazer uma an�lise de sua performance. O processo de depurar consiste em encontrar e reduzir os *bugs* no c�digo, para isso exisetm programas como o GDB. Al�m disso podemos querer saber quanto tempo o programa est� gastando em cada parte do c�digo, para isso existem *softwares* de *profiling* como o gprof.

### GDB

O GDB � um *debugger* de programas, ele permite visualizar o estado do programa comando a comando, permitindo ver os valores atribuidos a vari�veis e aos registradores. Para utilizado � necess�rio compilar o programa com a op��o -g.

#### Interface gr�fica DDD
O GDB pode ser complicado para visualiar as informa��es que desejamos, para isso existem interfaces gr�ficas que apresentam as funcionalidades do programa com uma cara mais amig�vel.
Podemos rodar o DDD no terminal com o comando:

~~~
ddd
~~~

Um interface ser� aberta e podemos inserir o programa a ser depurado no DDD. H� um terminal onde podemos inserir comandos do GDB como breakpoint e run para analisar o c�digo.

### gprof

O gprof � uma ferramenta de *profiling*, ela analisa o tempo gasto pelo programa e cada fun��o. Para executa-lo devemos compilar o programa que desejamos analisar com a op��o -pg e executa-lo, com isso um arquivo gmon.out ser� gerado. Ent�o podemos rodar o seguinte comando:
~~~
gprof [nome_do_programa] gmon.out
~~~

A sa�da ser� semelhante a que se segue:
~~~
Flat profile:

Each sample counts as 0.01 seconds.
  %   cumulative   self              self     total           
 time   seconds   seconds    calls  us/call  us/call  name    
 95.46      2.46     2.46   123454    19.95    19.95  primo

...
		     Call graph (explanation follows)

granularity: each sample hit covers 2 byte(s) for 0.41% of 2.46 seconds

index % time    self  children    called     name
                2.46    0.00  123454/123454      main [2]
[1]    100.0    2.46    0.00  123454         primo [1]
-----------------------------------------------
                                                 <spontaneous>
[2]    100.0    0.00    2.46                 main [2]
                2.46    0.00  123454/123454      primo [1]
-----------------------------------------------
~~~

Podemos ver ent�o que o programa primo gasta quase 95.5% do tempo de execu��o na fun��o primo e quantas vezes esta fun��o foi chamada. Logo, devemos focar o empenho de otimizar esta fun��o se desejamos deixar o programa mais r�pido.

## Programa paralelizado

Para escolher qual parte do c�digo otimizar, devemos analisar o tempo gasto pelo programa. No nosso caso a fun��o primo toma a maior parte do programa, logo vale muito mais a pena otimizar esta fun��o do que otimizar a fun��o main. O *loop* for que chama a fun��o primo � uma boa op��o para paralelizarmos o programa pois cada itera��o do loop � independente da outra, por consequ�ncia podemos reduzir o tempo de execu��o ao rodar estas itera��es em paralelo. Os resultados seguem:

~~~
real	0.360s
user	0.850s
sys		0.001s
~~~
Comparando com a vers�o n�o paralelizado do mesmo programa, temos uma redu��o de 2.6 no tempo de execu��o. Como o computador possui 4 cores para realizar o parelelismo, era de se esperar uma redu��o maior no tempo, no entanto � um bom resultado na otimiza��o do programa.

## Melhorando o desempenho do programa

Para melhorar o desempenho do programa, podemos aplicar todas as otimiza��es descritas anteriormente em um �nico programa, encontrado em /exercicio1/final/. Ent�o aplicamos a melhor vari�vel de otimiza��o encontrada '-O1', usamos a op��o -mtune=intel, paralelizamos o *loop* para chamada da fun��o primo, e dentro da fun��o, reduzimos o n�mero de itera��es at� a raiz de n. Com todas estas altera��es, obtemos o seguinte resultado:


~~~
real	0.004s
user	0.011s
sys		0.001s
~~~

Vemos ent�o como � importante a otimiza��o de c�digo, visto que o programa final � quase 400 vezes mais r�pido que o programa sem otimiza��es (/exercicio1/n_primos_1_arquivo).
