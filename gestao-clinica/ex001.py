# Inserção em O(n): Crie uma função inserirNoInicio(vetor, novoPaciente). Você deve
# percorrer o vetor do fim para o começo, movendo cada elemento uma posição para
# a direita, e então inserir o novo paciente no índice 0.
def inserirNoInicio(vetor, novoPaciente):
    contador_custo = 0
    for i in range(len(vetor) -1, 0, -1):
        vetor[i] = vetor[i -1]
        contador_custo = contador_custo + 1
    vetor[0] = novoPaciente
    return vetor, contador_custo
    
vetor, contador_custo = inserirNoInicio(["Felipe", "Francine", "José", "Sandra", "Marcelo", "Lucia", "Rafael", "Rodrigo", "Joao", "Maria"], "Bela")
print(f"Contador de Custo: {contador_custo}")
print(f"Resultado do vetor com deslocamento de memória: {vetor}")