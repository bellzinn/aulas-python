vetor = []

for i in range(5):
    num = float(input("digite um número para ser analisado: "))
    vetor.append(num)

maior = vetor.index(max(vetor))
menor = vetor.index(min(vetor))

print("O maior valor encontrado está na posição ", maior)
print("O menor valor enconteado está na posição ", menor)