#Faça um programa que dada a entrada de uma lista o programa calcule a combinatória de  dois elementos
#e nos retorne as combinações em uma nova lista.

#inicio:
import random
cont= ''

while cont != 's': #loop do progama
 lista = []
 lista2 = []
 lista3 = []
 b=0
 a=0

 quant = int(input('bem vindo ao progama de analise,digite a seguir quantos numeros inteiros irão compor a sua lista para comecar a analise,sendo no minimo 3 numeros para formar a sua lista '))
 if quant >= 3:
  for x in range (0,quant):
   dado = int(input('digite um numero para compor a lista: '))
   lista.append(dado)
   lista3.append(dado)
  else:
   for y in range(0,2):
    def selectRandom(lista):
     return random.choice(lista)
    x = selectRandom(lista)
    lista2.append(selectRandom(lista))
    lista.remove(lista2[b])
    lista3.remove(lista2[b])
    b = b + 1
   else:
    z = len(lista)
    for h in range(0,z):
     lista2.append(lista2[0])
     lista2.append(lista[0])
     lista.remove(lista[0])
    else:
      for h in range(0,z):
       lista2.append(lista2[1])
       lista2.append(lista3[a])
       a = a + 1
    print('A combinatoria dos 2 elementos aleatorios foi: ',lista2 )
    
    cont = input('analise encerrada,se quiser realizar outra analise,digite quaquer outra tecla,se quiser encerrar digite S ') #condiçaõ para o fim do progama
   print('****progama encerrado****') #fim
 else:
  print('lista incomplenta')
  cont = input('analise encerrada,se quiser realizar outra analise,digite quaquer outra tecla,se quiser encerrar digite S ') #condiçaõ para o fim do progama

print('****progama encerrado****') #fim
