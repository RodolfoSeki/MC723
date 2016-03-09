# MC723 -Exercício 1
Aluno Luiz Rodolfo Felet Sekijima

RA 117842

Para todos os tempos de processamento dos programas exibidos a seguir, os testes foram executados em uma mesma maquina no IC, calculando a média de 100 execuções. Os valores tem precisão de 0.001s, a menor medida de tempo do comando "time", por isso os valores foram arrendados.

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


O compilador gcc permite no momento de compilação do programa setar *flags* que são variavéis de ambiente que indicam o modo que deve ser feita a compilação do código fonte. Elas melhoram o tamanho e tempo de execução do código compilado ao custo de tempo e memória no momento de compilação. Estas *flags* podem ser setadas incluindo no comando do gcc a variável "-O", seguida pelo nível de otimização que se deseja.  


A seguir vemos como a otimização via -O do gcc influenciam os tempos de execução e qual seu propósito:


#### -O0

Este é padrão, qualquer programa compilado sem *flags* será processado como "-O0", reduz tempo e memória no momento de compilação e facilita o *debbuging* do programa.  
~~~
real	0.3016s
user	0.30054s
sys	    0.00036s
~~~

#### -O1 ou -O

Nível de otimização básico, tenta reduzir tempo de execução e tamanho do código.

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

Maior nível de otimização, tenta deixar o código mais rápido possível na execução, o que aumenta em muito o tempo de compilação. No entanto, o uso de -O3 não é garantia de código mais rápido, pois os binários podem ser maiores e por causa do maior uso de memória. 
~~~
real	0.29582s
user	0.29418s
sys		0.00064s
~~~

#### -Ofast
Tenta deixar o -O3 mais rápido mas acaba quebrando os padrões importantes de compilação, não recomendado.
~~~
real	0.28996s
user	0.28842s
sys		0.0007s
~~~

#### -mtune e -march

Outra otimização possível é a opção -mtune que tenta ajustar o código favorecendo a sequência instruções que irão rodar mais rápida na CPU especificada.

~~~
real	0.30314s
user	0.30192s
sys		0.00036s
~~~


#### Melhor variável de otimização

A variável apresentou a melhor redução no tempo de execução do programa, era de se esperar que -O2 e -O3 fossem melhores pois ativam mais *flags* de otimização, mas para um código tão pequeno como esse, apenas duas funções, acabaram gerando uma complexidade exagerada no programa devido aos arquivos binários grandes e maior consumo de memória, o que resultou em maior lentidão na execução.

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

^Compile o programa sem nenhuma opção de compilação extra. 
	Quanto tempo ele gasta?
	Veja se o valor muda utilizando, separadamente, cada uma das otimizações -O0, -O1, -O2 -O3 (letra O maiúscula seguida de um número).
		Como especificar as otimizações que um compilador deve utilizar num programa?
		Qual delas deu o melhor tempo?
	Existem outras otimizações que você pode aplicar no processador atual, consulte o manual do gcc por otimizações da categoria -mtune e veja quais se aplicam ao seu processador.
		Para que elas servem?
		O tempo melhorou?
	Quais otimizações são importantes para o processador que você está utilizando?
	
	
Quebre o programa em dois arquivos separados: main.c com a função main e calc_primo.c com a função primo.
Faça as alterações necessárias nos dois arquivos para que eles compilem.
	Como compilá-los?
	Você consegue montar um script que compile estes dois programas?
	E um Makefile? 
	Qual a diferença entre um Makefile e um script?
Rode novamente o programa e veja se ele gasta o mesmo tempo com a melhor otimização utilizada anteriormente.
	O resultado foi o esperado? Comente.
	
Modifique seu programa para calcular quantos números primos existem entre 1 e n, seguindo o mesmo algoritmo utilizado, modificando apenas a função main e fazendo com que n seja um parâmetro passado por linha de comando.
	Meça o tempo com um arquivo fonte e com dois.
	O resultado foi o esperado? Comente.

Agora é hora de tentar melhorar um pouco o programa (mas não muito ainda).
Edite o laço da função primo para varrer apenas os números ímpares, dividindo o conjunto de números a testar por dois.
Lembre-se que o resultado deve ser o mesmo para a mesma entrada! Caso encontre algum problema, utilize o GDB para depurar seu programa.
Muitas vezes, a interface em modo texto do GDB dificulta a depuração, recomendo que vocês utilizem um visualizador gráfico para o GDB.
Um bom visualizador é o DDD (basta executar ddd na linha de comando).
Alguns comandos interessantes do GDB que você deve saber utilizar: breakpoint, watchpoint, print, display, run, set args e help.
O que é "depurar um programa"?
Como executar o GDB?
Como utilizar um ambiente gráfico com o GDB?


Em qual parte seu programa gasta mais tempo? use o gprof para descobrir
Como descobrir a parte que é mais executada de um programa?
Como utilizar o gprof?



Se você tiver que paralelizar alguma parte do código, qual parte você escolheria?
Como paralelizar de forma escalável o código?
Como fazer com que um programa tire proveito de multiprocessamento de forma escalável?
Eu sugiro utilizar OpenMP, veja um tutorial, o site oficial, uso pelo GCC e implementação GNU do for.
	Meça o tempo do programa paralelizado.
	O resultado foi o esperado? Comente.

Como melhorar ainda mais o desempenho deste programa?

