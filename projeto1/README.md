# FFmpeg - Grupo 2

## O que faz? Para que serve?
FFmpeg é uma coleção de bibliotecas e ferramentas para processar conteúdo multimídia, como áudio, vídeo, textos e metadados. Suporta vários tipos de formatos e é altamentente portátil. Iremos utilizá-lo para realizar o transcode de uma amostra de vídeo blu-ray 1080p no formato mp4 para o formato avi.

## Por que é bom para medir desempenho?
O programa é bom para medir desempenho porque é intensivo no uso de processamento multi-core, memória e acesso a disco. 

## O que baixar
É necessário clonar o [repositório do FFmpeg](https://github.com/FFmpeg/FFmpeg) e também fazer o download da [amostra de vídeo](http://downloads.dvdloc8.com/trailers/divxdigest/bourne_ultimatum_trailer.zip).

## Como compilar/instalar
Para compilar é necessário gerar os arquivos necessários com o comando:

	$ ./configure --disable-yasm
E compilar com:

	$ make

Após isso, o binário estará disponível na raiz do git, com o nome ffmpeg.
    
## Como executar
Para executar o programa com a amostra, é necessário definir alguns parâmetros padrões, logo, uma linha de comando que sintetiza é:
	
    $ ./ffmpeg -i in.mp4 -acodec copy -vcodec mpeg4 out.avi
    
## Como medir o desempenho
Para medir o desempenho, usamos:

* Page fault, cache miss, stalled
> Comandos uteis  
> $ perf stat -d  
> $ perf stat -r 10  
> $ perf report --stdio

* Tempo - usamos a própria medida do FFmpeg que é exibida na saída, isso é, o tempo de transcode gasto que é emitido como:
	
    
    
* Memória: meidmos o uso de memória através de um gráfico, que será extraído e renderizado com o seguinte comando:
```sh
    #!/bin/bash
	while true; do
      ps -C ffmpeg -o pid=,%mem=,vsz= >> mem.log
      gnuplot gnuplot.script
      sleep 1
	done &
```
Além disso, é necessário ter um arquivo gnuplot.script na pasta com o seguinte conteúdo:
```sh
set term png small size 800,600
set output "mem-graph.png"

set ylabel "VSZ"
set y2label "%MEM"

set ytics nomirror
set y2tics nomirror in

set yrange [0:*]
set y2range [0:*]

plot "/tmp/mem.log" using 3 with lines axes x1y1 title "VSZ", \
     "/tmp/mem.log" using 2 with lines axes x1y2 title "%MEM"
```

## Como apresentar o desempenho
Como o desempenho deverÃ¡ ser mostrado. Margem de erro, etc. 
## MediÃ§Ãµes base (uma mÃ¡quina)
Inclua a especificaÃ§Ã£o dos componentes relevantes e os resultados de desempenho.
