

# Exercício 3: Contagem de ciclos
Aluno Luiz Rodolfo Felet Sekijima

RA 117842

Para o exercício 3 de MC723 nos foi proposto fazer a contagem de ciclos de diversos programas, usando um simulador de processador MIPS. Avaliando o desempenho de um processador baseado no tempo de execução de um conjunto de programas.


## Contagem de ciclos

Uma medição que é feita para determinar o desempenho de um sistema é o CPI ou, *cycles per instruction*, que é a média de ciclos da máquinas necessários para executar uma instrução, podemos por exemplo determinar o CPI de uma máquina para um certo programa, contanto a quantidade de ciclos passados e quantas instruções foram realizadas, o CPI será o número de ciclos pelo npumero de instruções. O CPI é importante para analisar desempenho pois se considerarmos dois computadores operando na mesma frequência, aquele com CPI para um determinado programa, irá executar o programa mais rápido, pois no total executa menos instruções.  



## Simulador MIPS

Foram usados os programas disponibilizados pelo professor para simularmos programas em um processador MIPS, o **SystemC** é um conjunto de classes e macros C++ usadas para simulações *event-driven*, baseadas em eventos. O SystemC é utilizado pelo **ArchC**, que é uma linguagem de descrição de arquiteturas que permite criar programas para diversas arquiteturas. É importante lembrar que como cada instrução MIPS tem um trecho diferente de código em C++ para implementa-la, o tempo de simulação não está relacionado diretamente com o tempo de execução de um programa. 

## Resultados
### hello.c

Para aprender mais sobre o ambiente de simulação o programa hello.c foi executado como teste e com o objetivo de fazer com que o programa executasse pelo menos uma intrução de **add**. Para isso o arquivo **mips_isa.cpp** foi modificado para incluir um contador de instruções específico para add, e no final da execução mostrar quantos add foram executados. Diversas modificações foram realizadas no programa, com o intuito de fazer executar operações de add, no entanto, no resultado tinhamos sempre 0 intruções executadas, como mostra o exemplo abaixo:

~~~bash
-bash-4.3$ ./mips.x --load=hello.mips

        SystemC 2.3.1-Accellera --- Mar 31 2016 17:15:46
        Copyright (c) 1996-2014 by all Contributors,
        ALL RIGHTS RESERVED
ArchC: Reading ELF application file: hello.mips
ArchC: -------------------- Starting Simulation --------------------

Hello World
ArchC: -------------------- Simulation Finished --------------------
Numero de instrucoes de add:0

Info: /OSCI/SystemC: Simulation stopped by user.
ArchC: Simulation statistics
    Times: 0.00 user, 0.00 system, 0.00 real
    Number of instructions executed: 2727
    Simulation speed: (too fast to be precise)

~~~

A análise do objdump também indicou que nenhuma instrução de add foi executada, apenas addiu. Por causa disto, uma [pesquisa](http://stackoverflow.com/questions/16634110/difference-between-add-and-addu) foi feita e descobrimos que por padrão a instrução de add do MIPS é evitada, pois esta gera erro quando a operação de soma causa overflow, comportamento que não é desejado, por isso a instrução addu, que não causa overflow, é preferivel do que a add e os compiladores não irão gerar instrução de add a menos que seja forçado. Logo, para obter uma instrução de add no código, é necessário inseri-la no código Assembly.

### Dijkstra (small)

O programa dijkstra_small foi executado com o seguinte comando:

~~~
../mips.x --load=dijkstra_small input.dat 2> output_small.txt
~~~

Enviando o resultado da execução para output_small.txt. De informações relevantes temos que:

~~~bash
[ArchC 2.1] Printing GLOBAL statistics from processor module mips:
     INSTRUCTIONS : 49165637
     SYSCALLS : 293
~~~

Separando as instruções em 3 tipos, acesso à memória, de controle e outras, podemos estimar o número de ciclos realizados pelo programa seguindo a tabela a seguir:

| Categoria        | CPI médio|
| ------------- |:-------------:|
| Acesso à memória     | 10 |
| Controle (branch/jump)      | 3      |
| Outras | 1      |

Fazendo a soma das instruções de categoria temos que então:

| Categoria        | Instruções          | Ciclos (estimado)  |
| ------------- |:-------------:|:-----:|
| Acesso à memória     |  13994142 |   139941420   |
| Controle (branch/jump)|     10835655  |   32506965   |
| Outras |   24335840    |   24335840   |


Totalizando 196,784,225 ciclos e um CPI médio para o programa de 4.00.


Nota: Para realizar a soma de instruções o arquivo texto foi aberto no **gedit**, as linhas com informações sobre as instruções eram selecionadas e passadas para um outro arquivo e um regex ("\n\\[ArchC 2.1\\] \[a-z\]\* \[a-z\]\* \[a-z\]\* \[a-z\]\* \[a-z\]\*_?\[a-z\]\*:\n     COUNT :") era aplicado para retirar o todo o texto e substituir o texto por um sinal de +, então a soma estava pronta e era copiada para um terminal python que retornava o valor da soma.

### Adpcm encoder (small)

O programa adpcm encoder foi executado com o seguinte comando:

~~~
../mips.x --load=bin/rawcaudio < data/small.pcm 2> output_small_adpcm.txt
~~~

Enviando o resultado da execução para output_small_adpcm.txt, temos como informação importante do arquivo: 
~~~bash
ArchC 2.1] Printing GLOBAL statistics from processor module mips:
     INSTRUCTIONS : 27759971
     SYSCALLS : 1380
~~~

| Categoria        | Instruções          | Ciclos (estimado)  |
| ------------- |:-------------:|:-----:|
| Acesso à memória     | 2400352 |   24003520   |
| Controle (branch/jump)      |   7199310    |  21597930    |
| Outras |   18160309    |   18160309   |


Temos então um total de 63,761,759 ciclos e CPI médio do programa de 2.30.

### Dijkstra (large)

Por fim, o programa dijkstra_large foi executado com o seguinte comando:

~~~
../mips.x --load=dijkstra_large input.dat 2> output_large.txt
~~~


Enviando o resultado da execução para output_large.txt, temos como informação importante do arquivo: 
~~~bash
[ArchC 2.1] Printing GLOBAL statistics from processor module mips:
     INSTRUCTIONS : 223690621
     SYSCALLS : 1248
~~~

| Categoria        | Instruções          | Ciclos (estimado)  |
| ------------- |:-------------:|:-----:|
| Acesso à memória     |  63336200 |  633362000    |
| Controle (branch/jump)      |   51329314|   153987942   |
| Outras |   109025107    |  109025107    |

Resultando em um total de 896,375,049 ciclos e CPI médio de 4.01.

## Conclusão


A proposta do exercício era fazer a contagem de ciclos de uma máquina, para isso rodamos diversos programas em um simulador de um processador MIPS e analisamos suas instruções e saídas. Calculamos a duração da execução dos programas por uma estimativa de seu CPI e  ao compararmos o Dijkstra Small com o Adpcm Encoder Small vemos que a quantidade de ciclos do Dijkstra é 3 vezes maior que a do encoder, devido a maior quantidade de instruções de acesso à memória presentes no programa de Dijkstra. E vemos também ao comparar os resultados dos dois programas Dijkstra, que apesar da quantidade de instruções serem diferentes, por se tratar do mesmo programa o CPI médio foi praticamente  o mesmo, 4.0 para o Small e 4.01 para o Large. Logo, como a proposta do exercício foi  bem sucedida.
