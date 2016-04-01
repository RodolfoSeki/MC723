

# MC723 -Trabalho 1 (Parte 3)
Aluno Luiz Rodolfo Felet Sekijima

RA 117842

Como parte final do projeto 1 de MC723 sobre benchmarking, nos foi proposto realizar uma comparação dos computadores usados nos diversos benchmarks desenvolvidos durante o projeto. É importante notar que como as máquinas usadas foram usadas em benchmarks diferentes, não há como fazer uma comparação direta entre máqinas, os métodos de comparação descritos aqui são uma tentativa de descrever o desempenho do computador de modo que todos sejam comparáveis. Este relatório descreve dois métodos de comparação que geram uma nota de 0 a 10 de desempenho de um computador e faz uma análise dos benchmarks, computadores e métodos de comparação. Os dados e gráficos usados neste relatório podem ser encontrados no [link](https://docs.google.com/spreadsheets/d/19AsZPF5wWzLuQSpBF7YQ_B6IGZk35y0MTbK8ylPBcdQ/edit?usp=sharing) para leitura.

## Benchmark

Cada grupo criou um benchmark sobre um programa de código fonte aberto, com base em valores que foram extraidos durante a execução do programa, o parâmetro mais usados nos benchmarks foi o tempo de execução, outros parâmetros mais usados foram performance de disco na escrita e leitura, número de cache miss e número de ciclos. Um problema identificado nos benchmarks é de que a análise de alguns parâmetros não era suportada por todos os computadores usados no benchmark, diminuindo a quantidade de valores para comparar. Outro problema é a escolha de valores que são muito pequenos e sucetíveis a grandes erros, tempos de execução inferiores a 10 segundos podem gerar erros de precisão e colocam em dúvida a qualidade do benchmark. Os parâmetros que apresentaram estes problemas não foram utilizados nos métodos de comparação mas no geral, os benchmarks apresentaram dados interessantes para podermos realizar uma comparação entre os computadores. 


## Métodos

### Método 1

O primeiro método de comparação proposto é a normalização de cada parâmetro dos benchmarks para um valor entre 0 e 10 e então tirar uma média para cada máquina dos seus valores normalizados. A fórmula de normalização a seguir converte um conjunto de valores para valores entre 0 e 1, baseados nos valores máximo e mínimo do conjunto. Então basta multiplicar este valor por 10 e obtemos uma nota até 10 para um certo parâmetro dos benchmarks.

![Formúla de normalização 0 a 1]
(normalize.jpg)

Então cada máquina terá diversas notas de acordo com os benchmarks usados, tirando a média ponderada destas notas teremos a nota final daquele computador.

O problema deste método é que como poucos computadores foram usados, o desvio padrão é muito alto em algumas medidas usadas nos benchmakrs, e como veremos na próxima seção, isso causa com que as notas baixas se aproximem muito do valor 0 e notas altas se aproximem bastante do 10, deixando um vazio em notas intermediarias. E como cada parâmetro de desempenho tem peso igual no cálculo da nota final, uma medida com desvio padrão alto pode afetar negativamente o resultado final, gerando uma nota que não condiz com a realidade. Para resolver este problema, o método seguinte gera notas uniformes para cada parâmetro de desempenho antes de gerar a nota final.

### Método 2

Neste método, primeiro os valores de desempenho são convertidos em um ranking de melhor desempenho, quanto melhor o desempenho maior o ranking. Então a partir do ranking são geradas notas de 0 a 10, proporcionais a posição no ranking daquele parâmetro, assim teremos uma distribuição de notas muito mais homogênea e o desvio padrão das medidas cai expressivamente. Agora com as notas para cada parâmetro, geramos a nota final ponderada. 
Este método é melhor que o anterior pois, se considerarmos que todos os parâmetros são igualmente importantes e relevantes para a comparação, ele faz com que as notas dos parâmetros sejam determinadas por um mesmo fator, o posicionamento no ranking.

Se analisarmos os histogramas de notas dos dois métodos veremos que o método 2 distribui melhor as notas, mostrando uma melhor realidade dos dados.

![Histograma de notas do método 1]
(hist1.png)

![Histograma de notas do método 2]
(hist2.png)


### Comparação de apenas valores de tempo

Como o único valor em comum nos benchmarks é o tempo de execução, é interessante executar os métodos de comparação apenas para valores de tempo de execução. Além disso quando discutimos desempenho um dos fatores mais importantes é o tempo de execução de um programa pela máquina, por isso, os métodos foram repetidos apenas para valores de tempo.

## Análise das máquinas

A seguir as máquinas analisadas pelos benchmarks foram classificadas pela nota final dada por cada método, indicando também as especificações da máquina. As máquinas foram destacadas por cores representanto famílias iguais de processador, as fámilias destacadas são Intel Core i7, Intel Core i5 e Intel Core 2 QUAD (máquinas do Instituto de Computação).

### Método 1 - Notas

![Notas do método 1]
(notas1.png)



