#Faça um programa, com uma função que dado uma lista e uma posição da mesma faça o quartil dessa posição.

from configparser import Interpolation
import numpy as np

cont = ''

while cont != 's': #loop do progama
 lista = [] 
 quant = int(input('bem vindo ao progama de analise,digite a seguir quantos numeros irão compor a sua lista para comecar a analise '))
 for x in range (0,quant):   
  dado = float(input('digite um numero para compor a lista: '))
  lista.append(dado)
 else:
  
  print('o 1 quartil dessa lista é: ', np.quantile(lista, .25,
  interpolation = "midpoint"))
  print('o 2 quartil dessa lista é: ', np.quantile(lista, .50,
  interpolation = "midpoint"))
  print('o 3 quartil dessa lista é: ', np.quantile(lista, .75,
  interpolation = "midpoint"))
  print('o 4 quartil dessa lista é: ', np.quantile(lista, .100,
  interpolation = "midpoint"))
  cont = input('analise encerrada,se quiser realizar outra analise,digite quaquer outra tecla,se quiser encerrar digite S ') #condiçaõ para o fim do progama
print('****progama encerrado****') #fim
