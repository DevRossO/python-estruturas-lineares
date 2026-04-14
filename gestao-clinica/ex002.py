# Remoção com Compactação: Crie uma função removerDaPosicao(vetor, indice).
# Após apagar o dado, mova todos os elementos à direita para a esquerda, garantindo
# que não fiquem "buracos" (valores nulos/undefined) no meio do vetor.

def removerDaPosicao(vetor, indice):
    contador_custo = 0
    for i in range(indice, len(vetor) -1):
        vetor[i] = vetor [i + 1]
        contador_custo = contador_custo + 1
    # vetor[len(vetor) -1] = None #Opção sem usar o fatiamento
    vetor = vetor[0:len(vetor)- 1]
    return vetor, contador_custo

vetor, contador_custo = removerDaPosicao(["Felipe", "Francine", "José", "Sandra", "Marcelo", "Lucia", "Rafael", "Rodrigo", "Joao", "Maria"], 7)
print(f"Contador de custo: {contador_custo}")
print(f"Vetor após deslocamento de memória: {vetor}")