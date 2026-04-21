# Inversão In-Place: Inverta a ordem de todos os elementos do vetor sem criar um
# vetor reserva. Use uma variável aux para trocar os elementos das extremidades até
# chegar ao meio.

vetor = [1, 2, 3, 43, 4, 5, 6, 7, 8, 18, 29, 41, 53, 69, 71, 84]
left = 0
right = len(vetor) - 1
aux = 0
while left < right:
    aux = vetor[left]
    vetor[left] = vetor[right]
    vetor[right] = aux
    left = left + 1
    right = right - 1
print(vetor)