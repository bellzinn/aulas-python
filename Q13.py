#Faça um programa que: Dada uma lista [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] e um número inteiro, imprima a tabuada desse número.

#inicio:

cont = ''

while cont != 's': #loop do progama
 num = int(input('bem vindo ao progama,digite o numero inteiro em que vc queira a sua tabuada '))
 lista = ('1,2,3,4,5,6,7,8,9,10').split(',')
 for x in lista:
  y = int(x)
  mult = num * y 
  soma = num + y
  sub = num - y
  div = num / y
  print('quando o valor da lista é igual a ',x,'o valor da sua multplicação vai ser: ',mult,
  'o valor da sua soma vai ser: ',soma,'o valor da sua subtração vai ser: ',sub,'e o vaor da sua divisão vai ser: ',div)
 else:
  cont = input('analise encerrada,se quiser realizar outra analise,digite quaquer outra tecla,se quiser encerrar digite S ') #condiçaõ para o fim do progama
print('****progama encerrado****') #fim