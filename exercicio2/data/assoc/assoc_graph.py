#!/usr/bin/env python

import sys
import math
import matplotlib.pyplot as plt

flag = 0

BLOCK_SIZE = 256

# Valores de associatividade do grafico
x_axis = [1,2,4,8,16,32,64,128]

#script para gerar graficos das cofiguracoes da cache diferentes
# variando a associatividade


print "Gerando grafico para caches com associatividades diferentes"
print "Tamanho do bloco fixado para " + str(BLOCK_SIZE)


menor_bloco = int(math.log(x_axis[0],2))

imiss   =[0.0]*len(x_axis)
dmiss   =[0.0]*len(x_axis)

with open(sys.argv[1]) as f:
    for line in f:
    	
    	# busca testes que tem associatividade 1
        if flag == 0 and line.find('Tamanho do bloco|'+str(BLOCK_SIZE)+'|') != -1:
            x = line.split('|')
            cache_size = int(x[1].split('K')[0])
            block_size = int(x[3])
            assoc = int(x[5])
            if cache_size == 32:
                flag = 1

        if flag == 2 and line.find('Demand miss rate') != -1:
            #print line
            d_miss_rate = float(line.split('\t')[1].split(' ')[-1])
            
            # determina a posicao no vetor
            pos_array = int(math.log(assoc,2))

            imiss[pos_array]  = i_miss_rate
            dmiss[pos_array]  = d_miss_rate
            
            # reseta a flag para ler o proximo teste
            flag = 0
		            
        if flag == 1 and line.find('Demand miss rate') != -1:
            #print line
            i_miss_rate = float(line.split('\t')[1].split(' ')[-1])
            flag = 2



print imiss
print dmiss


plt.figure(1)
plt.subplot(211)
plt.xlabel('Associatividade')
plt.ylabel('Miss rate')
plt.title('Cache L1 Instruction - Associatividade por Miss Rate')
plt.grid(True)
plt.semilogx(x_axis, imiss, basex=2)


plt.subplot(212)
plt.xlabel('Associatividade')
plt.ylabel('Miss rate')
plt.title('Cache L1 Data - Associatividade por Miss Rate')
plt.grid(True)
plt.semilogx(x_axis, dmiss, basex=2)
plt.tight_layout()

plt.savefig("assoc_"+sys.argv[1]+".png")

#plt.show()

