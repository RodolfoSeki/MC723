#!/bin/bash

#ARRAY='183.equake.f2b 168.wupwise.f2b 186.crafty.m2b 252.eon.m2b'
ARRAY='183.equake.f2b'
ASSOCIATIVIDADE='1 2 4 8 16'
BLOCK_SIZE='16 32 64 128 256'
CACHE_SIZE='2K 4K 8K 16K 32K'

for trace in $ARRAY; do
	cd /home/staff/lucas/mc723/traces/$trace	# entra na pasta dos traces que serão usados
	pwd
	IFS='.' read -r id string <<< "$trace"	#separa nome da pasta string receber paramentro do dinero
	echo "$string"
	for cache_size in $CACHE_SIZE;do
		for block_size in $BLOCK_SIZE;do
			for associatividade in $ASSOCIATIVIDADE;do
				#echo -e "Associatividade:$associatividade\nTamanho Cache:$cache_size\nTamanho Bloco:$block_size\n" >> /home/ec2013/ra117842/mc723/MC723/exercicio2/$trace.txt
				../../dinero4sbc/dineroIV -informat s -trname $string -maxtrace 20 -l1-isize $cache_size -l1-ibsize $block_size -l1-dsize $cache_size -l1-dbsize $block_size -l1-iassoc $associatividade -l1-dassoc $associatividade| grep "Metrics\|-----------------\|Demand Fetches\|Fraction of total\|Demand Misses\|Demand miss rate\|Compulsory misses\|Capacity misses\|Conflict misses\|Compulsory fraction\|Capacity fraction\|Conflict fraction" | grep -v "( / Demand Fetches)"  >> /home/ec2013/ra117842/mc723/MC723/exercicio2/$trace.txt
			done
		done
	done
	
	
	
	#../../dinero4sbc/dineroIV -informat s -trname $string -maxtrace 20 -l1-isize 32K -l1-ibsize $i| grep "Metrics\|-----------------\|Demand Fetches\|Fraction of total\|Demand Misses\|Demand miss rate\|Compulsory misses\|Capacity misses\|Conflict misses\|Compulsory fraction\|Capacity fraction\|Conflict fraction" | grep -v "( / Demand Fetches)"  >> /home/ec2013/ra117842/mc723/MC723/exercicio2/$trace.txt

done



#for ((i=1;i<=64;i=i*2))
#do
#    echo -e "Associatividade:1\nTamanho Cache:32K\nTamanho Bloco:\n" >> /home/ec2013/ra117842/mc723/MC723/exercicio2/$trace.txt
#    ../../dinero4sbc/dineroIV -informat s -trname equake_f2b -maxtrace 20 -l1-isize 32K -l1-ibsize $i| grep "Metrics\|-----------------\|Demand Fetches\|Fraction of total\|Demand Misses\|Demand miss rate\|Compulsory misses\|Capacity misses\|Conflict misses\|Compulsory fraction\|Capacity fraction\|Conflict fraction" | grep -v "( / Demand Fetches)"  >> /home/ec2013/ra117842/mc723/MC723/exercicio2/$trace.txt
#    echo -e "\n\n">> /home/ec2013/ra117842/mc723/MC723/exercicio2/$trace.txt
#done

