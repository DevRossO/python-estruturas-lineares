# 8. Estratégia de Expansão: Ao detectar o erro do exercício anterior, o programa deve:
# Criar um novo vetor com o dobro do tamanho (10).
# Copiar os dados do vetor antigo para o novo.
# Deletar o vetor antigo (ou deixar o Garbage Collector agir).

vetor = []
contador = 0
tamanho_limite = 5
vetor_novo = []

for i in range(10):
    elemento_novo = i * 3   #Aqui criamos elementos do nosso vetor

    if contador >= tamanho_limite:
        tamanho_limite *= 2
        vetor_novo = list(vetor)
        vetor_novo.append(elemento_novo)
        vetor = vetor_novo
    vetor.append(elemento_novo)
    contador += 1

print("Conteúdo final do nosso vetor:", vetor)