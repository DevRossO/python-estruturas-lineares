# Unique (Sem Set): Dado um vetor com valores repetidos e ordenados (ex: [1, 1, 2, 
# 3, 3]), remova as duplicatas deslocando os elementos para a esquerda, deixando o 
# vetor "limpo".

vetor = [1, 1, 2, 3, 3, 4, 4, 5, 6, 7, 7, 8, 9, 9]

duplicatas = 1
for i in range(1, len(vetor)):
    if vetor[i] != vetor[i -1]:
        vetor[duplicatas] = vetor[i]
        duplicatas += 1

print(vetor)

        


