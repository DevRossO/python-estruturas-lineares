# Uma imagem 4x4 representada por um vetor linear de 16 posições.
# 10. Mapeamento de Coordenadas: Dada uma linha L e uma coluna C, crie a lógica
# para encontrar o valor no vetor linear.
# Fórmula: valor = vetor[linha * largura + coluna]

vetor_linear = [1, 2, 3, 43, 4, 5, 6, 7, 8, 1, 2, 4, 5, 6, 7, 8]
largura = 4

print(f"Vetor linar", vetor_linear)

linha = int(input("Qual linha quer acessar (0-3)? "))
coluna = int(input("Qual coluna quer acessar (0-3)? "))

valor = vetor_linear[linha * largura + coluna]

print(valor)
