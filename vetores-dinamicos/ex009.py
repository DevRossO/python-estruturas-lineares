# Relatório de Overhead: A cada inserção, imprima: Itens: X | Capacidade Real: Y.
# Observe como a capacidade aumenta em saltos, e não um a um.

vetor = []
contador = 0
tamanho_limite = 5
vetor_novo = []

for i in range(10):
    elemento_novo = i * 3 
    capacidade_real = tamanho_limite - contador

    if contador >= tamanho_limite:
        tamanho_limite *= 2
        vetor_novo = list(vetor)
        vetor = vetor_novo

    vetor.append(elemento_novo)
    contador += 1
    print(f"Elemento {elemento_novo} adicionado | Capacidade real: {capacidade_real} ")

print("Conteúdo final do nosso vetor:", vetor)