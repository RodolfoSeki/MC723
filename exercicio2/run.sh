#!/bin/bash


cd /home/staff/lucas/mc723/traces/183.equake.f2b

for ((i=1;i<=64;i=i*2))
do
    echo -e "Associatividade:1\nTamanho Cache:32K\nTamanho Bloco:\n" >> /home/ec2013/ra117842/mc723/MC723/exercicio2/equake_f2b.txt
    ../../dinero4sbc/dineroIV -informat s -trname equake_f2b -maxtrace 20 -l1-isize 32K -l1-ibsize $i| grep "Metrics\|-----------------\|Demand Fetches\|Fraction of total\|Demand Misses\|Demand miss rate\|Compulsory misses\|Capacity misses\|Conflict misses\|Compulsory fraction\|Capacity fraction\|Conflict fraction" | grep -v "( / Demand Fetches)"  >> /home/ec2013/ra117842/mc723/MC723/exercicio2/equake_f2b.txt
    echo -e "\n\n">> /home/ec2013/ra117842/mc723/MC723/exercicio2/equake_f2b.txt
done

