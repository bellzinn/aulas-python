#Faça um programa que itera em uma string e toda vez que uma vogal aparecer na sua string print o seu nome entre as letras.

#inicio:

cont = ''

while cont != 's': #loop do progama
  vogais = ('aeiouAEIOU')
  string = input('bem vindo ao progama de analise,digite a seguir a frase ou palavra que vc queira analisar ')
  div = ''.join(filter(lambda i: i not in vogais, string ))
  nome = input('para finalizar,digite agora o seu nome: ')
  for fin in div:
   print(fin)
   print(nome)
  else:
    cont = input('analise encerrada,se quiser realizar outra analise,digite quaquer outra tecla,se quiser encerrar digite S ') #condiçaõ para o fim do progama
print('****progama encerrado****') #fim
