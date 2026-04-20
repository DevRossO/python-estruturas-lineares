# Vetor de 24 posições representando as temperaturas de cada hora do dia.
# 4. Acesso Direto: Demonstre a eficiência O(1). Crie uma função que receba o vetor e
# retorne a temperatura da "hora agendada" pelo usuário sem percorrer o array

def hora_agendada(vetor, hora):

    return vetor[hora]


temperatura_do_dia = {0: 18, 1: 17, 2: 17, 3: 16, 4: 16, 5: 15, 6: 16, 7: 18, 8: 20, 9: 22, 10: 24, 11: 26, 12: 27, 13: 28, 14: 29, 15: 29, 16: 28,
                      17: 26, 18: 24, 19: 22, 20: 21, 21: 20, 22: 19, 23: 18}
user = int(input("De qual horário você quer descobrir a temperatura? "))
print(hora_agendada(temperatura_do_dia, user))