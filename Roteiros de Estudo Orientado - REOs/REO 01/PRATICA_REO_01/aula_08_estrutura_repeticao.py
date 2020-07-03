########################################################################################################################
# DATA: 03/07/2020
# DISCIPLINA: VISÃO COMPUTACIONAL NO MELHORAMENTO DE PLANTAS
# PROFESSOR: VINÍCIUS QUINTÃO CARNEIRO
# E-MAIL: vinicius.carneiro@ufla.br
# GITHUB: vqcarneiro - https://github.com/VQCarneiro
########################################################################################################################
# AULA 08
# TEMA: Estruturas de repetição
########################################################################################################################
'''
#Exemplo 01: Estrutura de repetição for - Básico
print('-----------------------------------------------------------------------------------------------------------------')
print('Exemplo 01 - Estruturas de Repetição (for) - Básico')
print('-----------------------------------------------------------------------------------------------------------------')
import time
alturas = [1.80,1.75,1.65,1.92, 1.88,1.70,1.55,1.92,2.01]
print('Lista Alturas: ' + str(alturas))
print('-----------------------------------------------------------------------------------------------------------------')
for alt in alturas:
    print(alt)
    time.sleep(0.5)
print('-----------------------------------------------------------------------------------------------------------------')
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
'''
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#Exemplo 02: Estrutura de repetição for - Iterador
'''
print('-----------------------------------------------------------------------------------------------------------------')
print('Exemplo 02 - Estruturas de Repetição - iterador')
print('-----------------------------------------------------------------------------------------------------------------')
import time
alturas = [1.80,1.75,1.65,1.92, 1.88,1.70,1.55,1.92,2.01]
print('Lista Alturas: ' + str(alturas))
print('Número de elementos do vetor alturas: ' + str(len(alturas)))
print('-----------------------------------------------------------------------------------------------------------------')
it = 0
for alt in alturas:
    it = it + 1
    print('Iteração: ' + str(it))
    print(alt)
    time.sleep(0.5)
    print(
        '-----------------------------------------------------------------------------------------------------------------')
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
'''
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#Exemplo 03: Estrutura de repetição for - Posições
'''
print('-----------------------------------------------------------------------------------------------------------------')
print('Exemplo 03 - Estruturas de Repetição - posições')
print('-----------------------------------------------------------------------------------------------------------------')
import time
alturas = [1.80,1.75,1.65,1.92, 1.88,1.70,1.55,1.92,2.01]
print('Lista Alturas: ' + str(alturas))
print('Número de elementos do vetor alturas: ' + str(len(alturas)))
print('-----------------------------------------------------------------------------------------------------------------')
it = 0
for i in range(0,len(alturas),1):
    it = it + 1
    print('Iteração: ' + str(it))
    print('Na posição ' + str(i) + ' há o elemento: ' + str(alturas[int(i)]))
    time.sleep(0.5)
    print(
        '-----------------------------------------------------------------------------------------------------------------')
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
'''
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
'''
#Exemplo 04: Estrutura de repetição for - Enumerate
print('-----------------------------------------------------------------------------------------------------------------')
print('Exemplo 04 - Estruturas de Repetição - enumerate')
print('-----------------------------------------------------------------------------------------------------------------')
import time
alturas = [1.80,1.75,1.65,1.92, 1.88,1.70,1.55,1.92,2.01]
print('Lista Alturas: ' + str(alturas))
print('Número de elementos do vetor alturas: ' + str(len(alturas)))
print('-----------------------------------------------------------------------------------------------------------------')
it = 0
for pos,alt in enumerate(alturas):
    it = it + 1
    print('Iteração: ' + str(it))
    print('Na posição ' + str(pos) + ' há o elemento: ' + str(alt))
    time.sleep(0.5)
    print(
        '-----------------------------------------------------------------------------------------------------------------')
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
'''
'''
#Exemplo 05: Estrutura de repetição for - Matriz (linhas)
print('-----------------------------------------------------------------------------------------------------------------')
print('Exemplo 05 - Estruturas de Repetição - Matriz (linhas)')
print('-----------------------------------------------------------------------------------------------------------------')
import numpy as np
import time
dados = np.loadtxt('dados_selecionados.txt')
nl,nc = np.shape(dados)

print('Dados')
print('-----------------------------------------------------------------------------------------------------------------')
print(dados)
print('-----------------------------------------------------------------------------------------------------------------')
print('Número de Linhas: ' + str(nl))
print('Número de Colunas: ' + str(nc))
print('-----------------------------------------------------------------------------------------------------------------')
contador = 0
for i in np.arange(0,nl,1):
    contador += 1
    print('Iteração: '+ str(contador))
    print('Na linha ' + str(i) + ' há os elementos: ' + str(dados[int(i),:]))
    time.sleep(0.5)
    print(
        '-----------------------------------------------------------------------------------------------------------------')
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
'''

'''
#Exemplo 06: Estrutura de repetição for - Matriz (colunas)
print('-----------------------------------------------------------------------------------------------------------------')
print('Exemplo 06 - Estruturas de Repetição - Matriz (colunas)')
print('-----------------------------------------------------------------------------------------------------------------')
import numpy as np
import time
dados = np.loadtxt('dados_selecionados.txt')
nl,nc = np.shape(dados)

print('Dados')
print('-----------------------------------------------------------------------------------------------------------------')
print(dados)
print('-----------------------------------------------------------------------------------------------------------------')
print('Número de Linhas: ' + str(nl))
print('Número de Colunas: ' + str(nc))
print('-----------------------------------------------------------------------------------------------------------------')
contador = 0
for j in np.arange(0,nc,1):
    contador += 1
    print('Iteração: '+ str(contador))
    print('Na coluna ' + str(j) + ' há os elementos: ' + str(dados[:,int(j)]))
    time.sleep(0.5)
    print(
        '-----------------------------------------------------------------------------------------------------------------')
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
'''

'''
#Exemplo 07: Estrutura de repetição for - Matriz (completa)
print('-----------------------------------------------------------------------------------------------------------------')
print('Exemplo 07 - Estruturas de Repetição - Matriz (completa)')
print('-----------------------------------------------------------------------------------------------------------------')
import numpy as np
import time
dados = np.loadtxt('dados_selecionados.txt')
nl,nc = np.shape(dados)

print('Dados')
print('-----------------------------------------------------------------------------------------------------------------')
print(dados)
print('-----------------------------------------------------------------------------------------------------------------')
print('Número de Linhas: ' + str(nl))
print('Número de Colunas: ' + str(nc))
print('-----------------------------------------------------------------------------------------------------------------')
contador = 0

matriz_quadrados = np.zeros((nl,nc))
for i in np.arange(0,nl,1):
    for j in np.arange(0,nc,1):
        contador += 1
        print('Iteração: '+ str(contador))
        print('Na linha ' + str(i) + ' e coluna ' + str(j) + ' há o elemento: ' + str(dados[int(i),int(j)]))
        time.sleep(0.5)
        matriz_quadrados[int(i),int(j)] = (dados[int(i),int(j)])**2
        print(
            '-----------------------------------------------------------------------------------------------------------------')
np.set_printoptions(precision=2)
np.set_printoptions(suppress=True)
print('-----------------------------------------------------------------------------------------------------------------')
print('Dados')
print('-----------------------------------------------------------------------------------------------------------------')
print(dados)
print('-----------------------------------------------------------------------------------------------------------------')
print('Dados ao Quadrado')
print('-----------------------------------------------------------------------------------------------------------------')
print(matriz_quadrados)
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
'''
'''
#Exemplo 08: Estrutura de repetição while
print('-----------------------------------------------------------------------------------------------------------------')
print('Exemplo 08 - Estruturas de Repetição While')
print('-----------------------------------------------------------------------------------------------------------------')
import time
contador = 0
while contador != 15:
    contador +=1
    time.sleep(0.5)
    print(contador)
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
'''
'''
#Exemplo 09: Estrutura de repetição While
print('-----------------------------------------------------------------------------------------------------------------')
print('Exemplo 09 - Estruturas de Repetição While')
print('-----------------------------------------------------------------------------------------------------------------')
import numpy as np
import time
vetor = np.array([10,24,23,19,55,129,315,7,4])
print('Vetor: ' + str(vetor))
print('Dimensão: ' +str(len(vetor)))
print('-----------------------------------------------------------------------------------------------------------------')
pos = 0
while vetor[pos]!=100:
    print(vetor[pos])
    pos = pos+1
    time.sleep(0.5)
    if pos==(len(vetor)):
        print('Posição igual a: ' +str(pos)+ ' - A condição estabelecida retornou true, vamos sair do while')
        break

print('-----------------------------------------------------------------------------------------------------------------')
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
'''
########################################################################################################################




