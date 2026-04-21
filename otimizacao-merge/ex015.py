# 15. Merge de Ordenados: Dados dois vetores A e B já ordenados, crie o vetor C que
# combina ambos mantendo a ordem, sem usar o comando .sort().

vetor_a = [1, 2, 5, 6, 7, 9, 14]
vetor_b = [3, 4, 8, 10, 13, 15]

vetor_c = []
i = 0
j = 0

while i < len(vetor_a) and j < len(vetor_b):
    if vetor_a[i] < vetor_b[j]:
        vetor_c.append(vetor_a[i])
        i += 1
    elif vetor_b[j] < vetor_a[i]:
        vetor_c.append(vetor_b[j])
        j += 1

vetor_c.extend(vetor_a[i:])
vetor_c.extend(vetor_b[j:])

print(vetor_c)

