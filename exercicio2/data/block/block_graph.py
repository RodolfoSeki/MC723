#!/usr/bin/env python

import sys
import math
import matplotlib.pyplot as plt

flag = 0

# Valores do block_size do grafico
x_axis = [8,16,32,64,128,256,512,1024,2048,4096,8192]

ASSOCIATIVIDADE = 1

#script para gerar graficos das configuracoes da cache diferentes
# variando o block_size


print "Gerando grafico para block size diferentes"
print "Associatividade fixada para " + str(ASSOCIATIVIDADE)

menor_bloco = int(math.log(x_axis[0],2))

imiss   =[0.0]*len(x_axis)
dmiss   =[0.0]*len(x_axis)


with open(sys.argv[1]) as f:
    for line in f:
    	
    	# busca testes que tem associatividade 1
        if flag == 0 and line.find('Associatividade|'+str(ASSOCIATIVIDADE)+'|') != -1:
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
            pos_array = int(math.log(block_size,2)) - menor_bloco
            
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
plt.xlabel('Block Size')
plt.ylabel('Miss rate')
plt.title('Cache L1 Instruction - Block Size por Miss Rate')
plt.grid(True)
plt.semilogx(x_axis, imiss, basex=2)


plt.subplot(212)
plt.xlabel('Block Size')
plt.ylabel('Miss rate')
plt.title('Cache L1 Data - Block Size por Miss Rate')
plt.grid(True)
plt.semilogx(x_axis, dmiss, basex=2)
plt.tight_layout()

plt.savefig("block_"+sys.argv[1]+".png")

#plt.show()
