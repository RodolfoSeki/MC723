

# MC723 -Trabalho 1 (Parte 3)
Aluno Luiz Rodolfo Felet Sekijima

RA 117842

Como parte final do projeto 1 de MC723 sobre benchmarking, nos foi proposto realizar uma comparação dos computadores usados nos diversos benchmarks desenvolvidos durante o projeto. É importante notar que como as máquinas usadas foram usadas em benchmarks diferentes, não há como fazer uma comparação direta entre máqinas, os métodos de comparação descritos aqui são uma tentativa de descrever o desempenho do computador de modo que todos sejam comparáveis. Este relatório descreve dois métodos de comparação que geram uma nota de 0 a 10 de desempenho de um computador e faz uma análise dos benchmarks, computadores e métodos de comparação. Os dados e gráficos usados neste relatório podem ser encontrados no [link](https://docs.google.com/spreadsheets/d/19AsZPF5wWzLuQSpBF7YQ_B6IGZk35y0MTbK8ylPBcdQ/edit?usp=sharing) para leitura.

## Benchmark

Cada grupo criou um benchmark sobre um programa de código fonte aberto, com base em valores que foram extraidos durante a execução do programa, o parâmetro mais usados nos benchmarks foi o tempo de execução, outros parâmetros mais usados foram performance de disco na escrita e leitura, número de cache miss e número de ciclos. Um problema identificado nos benchmarks é de que a análise de alguns parâmetros não era suportada por todos os computadores usados no benchmark, diminuindo a quantidade de valores para comparar. Outro problema é a escolha de valores que são muito pequenos e sucetíveis a grandes erros, tempos de execução inferiores a 10 segundos podem gerar erros de precisão e colocam em dúvida a qualidade do benchmark. Os parâmetros que apresentaram estes problemas não foram utilizados nos métodos de comparação mas no geral, os benchmarks apresentaram dados interessantes para podermos realizar uma comparação entre os computadores. 

### Benchmarks do Grupo B

Os benchmarks usados pelo nosso grupo são sobre programas relacionados a processamento de imagens e um compilador:
* GENETIC é um programa que recria a imagem através de polígonos semi-transparentes que são gerados por um algoritmo genético.
* FFmpeg é uma coleção de bibliotecas e ferramentas para processar conteúdo multimídia, como áudio, vídeo, textos e metadados. Suporta vários tipos de formatos e é altamentente portátil. E foi utilizado para realizar o transcode de uma amostra de vídeo blu-ray 1080p no formato mp4 para o formato avi.
* O [TCC Tiny C Compiler 0.9.26](http://bellard.org/tcc/) é um compilador para a linguagem C. E utilizamos o tcc para compilar a biblioteca [C FFTW](http://www.fftw.org/).

No GENETIC como parâmetro de desempenho foram usados o tempo de execução do programa, com esse tempo de execução e o tamanho da imagem processada é calculado o desempenho de escrita da imagem no disco. As duas medidas são muito importantes para determinar o desempenho, mas apenas estas duas não são suficientes para gerar um bom benchmark. O programa TCC apresentou o mesmo problema, apresentou como benchmark apenas a média de tempos de excução do programa, medida muito importante para determinar desempenho mas não suficiente.

O programa FFmpeg foi o que apresentou um benchmark mais completo, medindo valores de tempo de execução, mas também incluindo valores relativos ao hardware como page fault, cache miss e stall de ciclos. Estes outros valores estão relacionados ao modo como o computador processa as instruções, formando um benchmark mais informativo.  

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


O método 1 conseguiu determinar as máquinas de pior desempenho de modo semelhante com o método 2, mas para as outras máquinas os valores parecem incertos, as máquinas destacadas em amarelo são as máquinas do IC, que além de possuir mesmo processador, tem as mesma configurações de software e hardware. Se olharmos os valores dos benchmarks para estes computadores eles são muitos próximos, mas o método atribuiu notas muito diferente entre eles, entre 2.25 e 8.46, mesmo existindo diferenças físicas entre as máquinas, as notas estão muito diferentes.

### Método 2 - Notas

![Notas do método 2]
(nota2.png)


O método 2 apresentou um ranking melhor entre as máquinas, atribuindo notas mais próximas para as máquinas do IC e mostrando os computadores com processador de mais novos e maior memória no topo do ranking.

### Método 2 apenas para valores de tempo - Notas

![Notas do método 2 apenas para valores de tempo]
(notas2T.png)

![Histograma de notas do método 2 para valores de tempo]
(hist2T.png)

Vemos uma classificação semelhante a anterior, mas agora as máquinas do IC apresentam notas muito semelhantes, com excessão da máquina usada por Victor Sousa, as outras notas estão em um intevalo de 1 ponto apenas. E o histograma de notas também está melhor distribuido. Portanto este será o ranking usado para determinar o desempenho dos computadores.

## Desempenho das máquinas


Segundo o ranking de notas anterior o computador de melhor desempenho foi o usado por Titouan Thibaud, com processador Intel Core i7-2630QM CPU, 2.00GHz de frequência e 4GB de memória rodando Linux Mint. No entanto se obesrvarmos os benchmarks, está máquina executou apenas um benchmarks, enquanto as outras máquinas executaram pelo menos 3 benchmarks diferentes e como ele foi o melhor colocado no seu benchmark em todos os parâmetros, recebeu  nota 10. Provavelmente se ele executasse outros benchmarks a nota cairira bastante, então vamos desconsiderar este computador.
A segunda maior nota é um Intel Core i7-4700HQ, com 16GB de memória e rodando Ubuntu 14.04. Analisando o desempenho nos benchmarks, ele está bem colocado em todos os benchmarks, sendo o primeiro ou segundo em quase todos os parâmetros, apenas no quesito de page faults o computador apresentou desempenho muito abaixo. Assim, podemos determinar que este foi o computador que apresentou o melhor desempenho entre todos os utilizados nos benchmarks.

## Conclusão

O projeto tem como intuito gerar benchmarks para ser possível comparar diversos computadores, diversos fatores dificultaram com que essa comparação fosse feita, poucos parâmetros diferentes de desempenho, uso de benchmarks diferentes entre computadores, poucos computadores para comparação e configurações de hardware muito semelhantes. Mas o relatório se propos a analisar estes benchmarks e determinar um método de comparação entre os computadores, e realizou a tarefa de forma satisfatória, fornecendo um meio de comparação para incluir todas as máquinas.
