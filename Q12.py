#Faça um programa que receba uma string, com um número de ponto flutuante, e imprima qual a parte dele que não é inteira;

#inicio

cont = ''

while cont != 's': #loop do progama
 num = input('bem vindo ao progama de analise,digite a seguir um numero a ser analizado ').split(',')
 print(num[1])
 cont = input('analise encerrada,se quiser realizar outra analise,digite quaquer outra tecla,se quiser encerrar digite S ') #condiçaõ para o fim do progama
print('****progama encerrado****') #fim