#!/usr/bin/env python

import sys
import re

# Calcula a media de tempo entre todas as simulacoes para entre:
# real, sys, user

soma_real = 0.0
soma_user = 0.0
soma_sys = 0.0

# Soma os tempos de execucao para cada execucao
with open(sys.argv[1]) as f:
    for line in f:
        if 'real' in line:
            actual = line.split('m')[1]
            soma_real = soma_real + float(actual.split('s')[0])
        if 'user' in line:
            actual = line.split('m')[1]
            soma_user = soma_user + float(actual.split('s')[0])
        if 'sys' in line:
            actual = line.split('m')[1]
            soma_sys = soma_sys + float(actual.split('s')[0])

# Calcula e imprime a media de tempos
print('real	'+ str(soma_real/int(sys.argv[2]))+'s')
print('user	'+ str(soma_user/int(sys.argv[2]))+'s')
print('sys		'+ str(soma_sys/int(sys.argv[2]))+'s')

