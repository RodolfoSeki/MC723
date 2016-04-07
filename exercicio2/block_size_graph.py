#!/usr/bin/env python

import sys
import math
import matplotlib.pyplot as plt

flag = 0
x = [4 , 8 , 16, 32 , 64]

#script para gerar graficos das cofiguracoes da cache diferentes
# os block_sizes sao variados


print "Gerando grafico para block size diferentes"
print "Associatividade fixada para 1"

menor_cache_size = int(math.log(4,2))

imiss8  =[0]*5
imiss16 =[0]*5
imiss32 =[0]*5
imiss64 =[0]*5
dmiss8  =[0]*5
dmiss16 =[0]*5
dmiss32 =[0]*5
dmiss64 =[0]*5

with open(sys.argv[1]) as f:
    for line in f:
    	
    	# busca testes que tem associatividade 1
        if flag == 0 and line.find('Associatividade|1|') != -1:
            x = line.split('|')
            
            cache_size = int(x[1].split('K')[0])
            block_size = int(x[3])
            flag = 1

        if flag == 2 and line.find('Demand miss rate') != -1:
            d_miss_rate = float(line.split('\t')[1].split(' ')[-1])
            
            # determina a posicao no vetor
            pos_array = int(math.log(cache_size,2)) - menor_cache_size

            
            if(block_size == 8):
                imiss8[pos_array]  = i_miss_rate
                dmiss8[pos_array]  = d_miss_rate
            if(block_size == 16):
                imiss16[pos_array]  = i_miss_rate
                dmiss16[pos_array]  = d_miss_rate
            if(block_size == 32):
                imiss32[pos_array]  = i_miss_rate
                dmiss32[pos_array]  = d_miss_rate
            if(block_size == 64):
                imiss64[pos_array]  = i_miss_rate
                dmiss64[pos_array]  = d_miss_rate
            
            # reseta a flag para ler o proximo teste
            flag = 0
		            
        if flag == 1 and line.find('Demand miss rate') != -1:
            i_miss_rate = float(line.split('\t')[1].split(' ')[-1])
            flag = 2

print imiss8
print imiss16
print imiss32
print imiss64
print dmiss8
print dmiss16
print dmiss32
print dmiss64

plt.figure(1)
plt.xlabel('Tamanho da cache')
plt.ylabel('Miss rate')
plt.title('Comparando tamanhos de bloco de cache diferentes')
plt.grid(True)
plt.plot(x, imiss8)
plt.plot(x, imiss16)
plt.plot(x, imiss32)
plt.plot(x, imiss64)
#plt.savefig("active_"+str(sys.argv[1].split('.')[0] + ".png"))
plt.show()



