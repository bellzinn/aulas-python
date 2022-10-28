import statistics
cont = ''


while cont != 's': #loop do progama
 lista = []
 n = 1
 quant = int(input('bem vindo ao progama de analise,digite a seguir quantos numeros irão compor a sua lista para comecar a analise '))
 
 for x in range (0,quant):   
  print('digite a seguir o',n,'da sua lista')
  dado =float(input('digite o seu numero de escolha: '))
  lista.append(dado)
  n = n + 1
  
 else:
  print(statistics.median(lista))
  cont = input('analise encerrada,se quiser realizar outra analise,digite quaquer outra tecla,se quiser encerrar digite S ') #condiçaõ para o fim do progama
print('****progama encerrado****') #fim
