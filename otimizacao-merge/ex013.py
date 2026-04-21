# Desafios de lógica avançada com arrays. 
# 13. Vetor Esparso: Escreva uma função que conte quantos elementos são "zero" em 
# um vetor de 50 posições. Se mais de 70% forem zero, imprima "Vetor Ineficiente: 
# Recomenda-se compressão". 

vetor = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 29, 21, 16, 11, 5, 4, 12]
limite = len(vetor) * 0.7
contador = 0
for i in vetor:
    if i == 0:
        contador += 1
if contador >= limite:
    print("Seu vetor é ineficiente, recomenda-se compresão")
print(f"Quantidade de zeros em seu vetor: {contador}")
