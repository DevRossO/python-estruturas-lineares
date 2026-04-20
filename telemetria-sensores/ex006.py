# Análise de Extremos: Implemente uma função que encontre o maior e o menor
# valor do vetor percorrendo-o apenas uma vez (Complexidade O(n)).
def maior_menor(vetor):
    maior = vetor[0]
    menor = vetor[0]
    for temp in vetor:
        if temp > maior:
            maior = temp
        elif temp < menor:
            menor = temp
    return maior, menor


print(maior_menor([18, 17, 17, 16, 16, 15, 16, 18, 20, 22, 24, 26, 27, 28, 29, 29, 28,
                      26, 24, 22, 21, 20, 19, 18]))