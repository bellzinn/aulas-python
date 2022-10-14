#Faça uma programa que dada a entrada de uma lista ele faça o cálculo acumulativo da mesma:

#inicio:

cont= ''

while cont != 's': #loop do progama
 lista = []
 dado2 = 0 
 quant = int(input('bem vindo ao progama de analise,digite a seguir quantos numeros irão compor a sua lista para comecar a analise '))
 for x in range (0,quant):
  dado = float(input('digite um numero para compor a lista: '))
  lista.append(dado + dado2)
  dado2 = dado + dado2
 else:
  print('o cálculo acumulativo dessa lista é: ',lista)
  cont = input('analise encerrada,se quiser realizar outra analise,digite quaquer outra tecla,se quiser encerrar digite S ') #condiçaõ para o fim do progama
print('****progama encerrado****') #fim
