# Simulação de como o Python/JS gerencia memória internamente.
# 7. Estouro de Capacidade: Crie um vetor de tamanho 5. Tente inserir 6 elementos
# usando um contador manual. Quando o contador superar o tamanho, exiba a
# mensagem: "Erro: Overflow de Memória".

vetor = []
contador = 0
tamanho_limite = 5

for i in range(6):
    elemento_novo = i + 2   #Aqui criamos elementos do nosso vetor

    if contador >= tamanho_limite:
        print("Erro: Overflow de Memória")
    else:
        vetor.append(elemento_novo)
        contador += 1

print("Conteúdo final do nosso vetor:", vetor)