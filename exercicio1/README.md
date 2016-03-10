# MC723 -Exercício 1
Aluno Luiz Rodolfo Felet Sekijima

RA 117842

Para todos os tempos de processamento dos programas exibidos a seguir, os testes foram executados em uma mesma maquina no IC, com processador i5-3570 de 4 *cores*, calculando a média de 100 execuções. Os valores tem precisão de 0.001s, a menor medida de tempo do comando "time", por isso os valores foram arrendados.

## primo.c não otimizado
O programa original disponibilizado para o exercício se encontra no subdiretório "exercicio1/original" e foi compilado sem nenhuma flag de otimização com o seguinte comando:

```bash
gcc primo.c -o primo
```
E com o seguinte resultado de tempo de execução:

~~~
real	0.307s
user	0.305s
sys		0.001s
~~~

Este será o tempo base para podermos determinar as melhores otmizações feitas sobre o programa original.

### Otimização por *flags* (gcc)


O compilador gcc permite no momento de compilação do programa setar *flags* que são variavéis de ambiente que indicam o modo que deve ser feita a compilação do código fonte. Elas melhoram o tamanho e tempo de execução do código compilado ao custo de tempo e memória no momento de compilação. Estas *flags* podem ser setadas incluindo no comando do gcc a variável "-O", seguida pelo nível de otimização que se deseja.  


A seguir vemos como a otimização via -O do gcc influenciam os tempos de execução e qual seu propósito:


#### -O0

Este é padrão, qualquer programa compilado sem *flags* será processado como "-O0", reduz tempo e memória no momento de compilação e facilita o *debbuging* do programa.  
~~~
real	0.299s
user	0.298s
sys		0.001s
~~~

#### -O1 ou -O

Nível de otimização básico, tenta reduzir tempo de execução e tamanho do código.

~~~
real	0.269s
user	0.268s
sys		0.001s
~~~

#### -O2
Otimização além de -O1, seta todas as *flags* de -O1 e mais alguns parametros de otimização. Tenta reduzir mais o tempo de execução sem modificar o tamanho do código compilado.

~~~
real	0.295s
user	0.295s
sys		0.000s
~~~

#### -O3

Maior nível de otimização, tenta deixar o código mais rápido possível na execução, o que aumenta em muito o tempo de compilação. No entanto, o uso de -O3 não é garantia de código mais rápido, pois os binários podem ser maiores e por causa do maior uso de memória. 
~~~
real	0.296s
user	0.295s
sys		0.001s
~~~

#### -Ofast
Tenta deixar o -O3 mais rápido mas acaba quebrando os padrões importantes de compilação, não recomendado.
~~~
real	0.292s
user	0.291s
sys		0.001s
~~~

#### -mtune

Outra otimização possível é a opção -mtune que tenta ajustar o código favorecendo a sequência instruções que irão rodar mais rápida na CPU especificada.

O computador utilizado é da família Ivy Bridge da Intel, mas outros parametros de otimização que podem ser aplicados são o *intel*, com código otimizado para a s versõse mais atuais de processadores da Intel, e o *native*, em que o compilador tenta determinar o tipo de processador. 

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


#### Melhor variável de otimização

A variável -O1 apresentou a melhor redução no tempo de execução do programa, era de se esperar que -O2 e -O3 fossem melhores pois ativam mais *flags* de otimização, mas para um código tão pequeno como esse, apenas duas funções, mais flags de otimização acabaram gerando uma complexidade exagerada no programa devido aos arquivos binários grandes e maior consumo de memória, o que resultou em maior lentidão na execução.

## main.c e calc_primo.c

Separando o programa em dois arquivos ("/exercicio1/dois_arquivos"), podemos compila-lo usando um *makefile*, o *makefile* é um arquivo que define as diretivas de compliação. Para o programa primo, ele gera um *object file* para cada arquivo fonte e então faz o *link* entre eles. Estes foram os resultados dos tempos:

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

Vemos que os tempos de execução foram praticamente iguais e muito próximo do tempo de execução um único arquivo sem flags, o que mostra que as otimizações da variável -O1 talvez não afetem a velocidade de execução do programa quando ele é separado em dois arquivos.

Além de compilar via *makefile*, é possivel criar um *script* bash que executa os mesmos comandos de compilação. O resultado na execução do código será o mesmo, no entanto, o *makefile* é preferível ao *script* pois na hora de recompilar um programa, o *makefile* apenas recompila aqueles arquivos que foram alterados após a última chamada do *make* 

## Primos entre 1 e n

Para os padronizar o calculo do tempo de execução dos programas a seguir, que calculam o número de primos entre 1 e n, todos os testes foram realizados calculando a quantidade de primos entre 1 e 123456 e sem flags de otimização.

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

Podemos ver que o programa compilado de um único arquivo fonte é mais rápido na execução, o que pode indicar que o *linker* do gcc deixe o programa com dois arquivos fontes ligeiramente mais devagar.

### verificando apenas ímpares

Reescrevendo o laço que procura divisores de um número n, dividimos pela metade o número de testes feitos por número, para o programa de calculo de primos com dois arquivos, vemos a seguir o resultado desta alteração:

~~~
real	0.956s
user	0.952s
sys		0.001s
~~~

Vemos que o tempo reduziu bastaste, praticamente metade da versão com dois arquivos, isso pode ser explicado pelo fato de que o programa passa a maior parte do tempo executando a função primo, que será  visto quando usarmos a ferramenta *gprof*.

## Ferramentas

Podemos utilizar ferramentas na hora de depurar um programa e fazer uma análise de sua performance. O processo de depurar consiste em encontrar e reduzir os *bugs* no código, para isso exisetm programas como o GDB. Além disso podemos querer saber quanto tempo o programa está gastando em cada parte do código, para isso existem *softwares* de *profiling* como o gprof.

### GDB

O GDB é um *debugger* de programas, ele permite visualizar o estado do programa comando a comando, permitindo ver os valores atribuidos a variáveis e aos registradores. Para utilizado é necessário compilar o programa com a opção -g.

#### Interface gráfica DDD
O GDB pode ser complicado para visualiar as informações que desejamos, para isso existem interfaces gráficas que apresentam as funcionalidades do programa com uma cara mais amigável.
Podemos rodar o DDD no terminal com o comando:

~~~
ddd
~~~

Um interface será aberta e podemos inserir o programa a ser depurado no DDD. Há um terminal onde podemos inserir comandos do GDB como breakpoint e run para analisar o código.

### gprof

O gprof é uma ferramenta de *profiling*, ela analisa o tempo gasto pelo programa e cada função. Para executa-lo devemos compilar o programa que desejamos analisar com a opção -pg e executa-lo, com isso um arquivo gmon.out será gerado. Então podemos rodar o seguinte comando:
~~~
gprof [nome_do_programa] gmon.out
~~~

A saída será semelhante a que se segue:
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

Podemos ver então que o programa primo gasta quase 95.5% do tempo de execução na função primo e quantas vezes esta função foi chamada. Logo, devemos focar o empenho de otimizar esta função se desejamos deixar o programa mais rápido.

## Programa paralelizado

Para escolher qual parte do código otimizar, devemos analisar o tempo gasto pelo programa. No nosso caso a função primo toma a maior parte do programa, logo vale muito mais a pena otimizar esta função do que otimizar a função main. O *loop* for que chama a função primo é uma boa opção para paralelizarmos o programa pois cada iteração do loop é independente da outra, por consequência podemos reduzir o tempo de execução ao rodar estas iterações em paralelo. Os resultados seguem:

~~~
real	0.360s
user	0.850s
sys		0.001s
~~~
Comparando com a versão não paralelizado do mesmo programa, temos uma redução de 2.6 no tempo de execução. Como o computador possui 4 cores para realizar o parelelismo, era de se esperar uma redução maior no tempo, no entanto é um bom resultado na otimização do programa.

## Melhorando o desempenho do programa

Para melhorar o desempenho do programa, podemos aplicar todas as otimizações descritas anteriormente em um único programa, encontrado em /exercicio1/final/. Então aplicamos a melhor variável de otimização encontrada '-O1', usamos a opção -mtune=intel, paralelizamos o *loop* para chamada da função primo, e dentro da função, reduzimos o número de iterações até a raiz de n. Com todas estas alterações, obtemos o seguinte resultado:


~~~
real	0.004s
user	0.011s
sys		0.001s
~~~

Vemos então como é importante a otimização de código, visto que o programa final é quase 400 vezes mais rápido que o programa sem otimizações (/exercicio1/n_primos_1_arquivo).
