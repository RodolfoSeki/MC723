#!/bin/bash

self="${0##*/}"

[ $# -eq 1 ] || { echo -e "Uso: ./$self <numero_do_trace>\nEscolha um numero entre 0 e 3"; exit 1; }

ARRAY=('183.equake.f2b' '168.wupwise.f2b' '186.crafty.m2b' '252.eon.m2b')
trace_num=$1
trace="${ARRAY[$trace_num]}"	# escolhe um trace para rodar todas as configurações de cache para aquele trace

ASSOCIATIVIDADE='1 2 4 8'
BLOCK_SIZE='8 16 32 64'
CACHE_SIZE='4K 8K 16K 32K 64K'



cd /home/staff/lucas/mc723/traces/$trace	# entra na pasta dos traces que serão usados
IFS='.' read -r id string <<< "$trace"	#separa nome da pasta pelo ponto receber paramentro do dinero
IFS='.' read -r str1 str2 <<< "$string" #separa novamente o nome do arquivo para outro parametro 
trname=$str1"_"$str2

for cache_size in $CACHE_SIZE;do
	for block_size in $BLOCK_SIZE;do
		for associatividade in $ASSOCIATIVIDADE;do
			echo -e "\nTamanho da cache|$cache_size|Tamanho do bloco|$block_size|Associatividade|$associatividade|" >> /home/ec2013/ra117842/mc723/MC723/exercicio2/$trace.out
			../../dinero4sbc/dineroIV -informat s -trname $trname -maxtrace 20 -l1-isize $cache_size -l1-ibsize $block_size -l1-dsize $cache_size -l1-dbsize $block_size -l1-iassoc $associatividade -l1-dassoc $associatividade| grep "l1-icache\|l1-dcache\|Metrics\|-----------------\|Demand Fetches\|Fraction of total\|Demand Misses\|Demand miss rate\|Compulsory misses\|Capacity misses\|Conflict misses\|Compulsory fraction\|Capacity fraction\|Conflict fraction" | grep -v "( / Demand Fetches)" >> /home/ec2013/ra117842/mc723/MC723/exercicio2/$trace.out

		done
	done
done

