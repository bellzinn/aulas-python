#Faça um programa, com uma função que calcule a média de uma lista.

#inicio:

cont = ''
import statistics#biblioteca do python
#tambem poderia ser usado as funções len(lista) e sum(lista) para realizar o calculo das medias

while cont != 's': #loop do progama
 lista = [] 
 quant = int(input('bem vindo ao progama de analise,digite a seguir quantos numeros irão compor a sua lista para comecar a analise '))
 for x in range (0,quant):   
  dado = float(input('digite um numero para compor a lista: '))
  lista.append(dado)
 else:
  media = statistics.mean(lista)
  print('a media dessa lista é: ',media)  
  
  cont = input('analise encerrada,se quiser realizar outra analise,digite quaquer outra tecla,se quiser encerrar digite S ') #condiçaõ para o fim do progama
print('****progama encerrado****') #fim