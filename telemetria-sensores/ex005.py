# Busca Manual: Implemente uma função existeTemperatura(vetor, valorBuscado).
# Use um laço para percorrer o vetor e retorne o índice da primeira ocorrência. Se não
# encontrar, retorne -1.


def existeTemperatura(vetor, valorBuscado):
        for hora, temperatura in vetor.items():
            if valorBuscado == temperatura:
                return hora
        return -1

temperatura_do_dia = {0: 18, 1: 17, 2: 17, 3: 16, 4: 16, 5: 15, 6: 16, 7: 18, 8: 20, 9: 22, 10: 24, 11: 26, 12: 27, 13: 28, 14: 29, 15: 29, 16: 28,
                      17: 26, 18: 24, 19: 22, 20: 21, 21: 20, 22: 19, 23: 18}
busca_temperatura = int(input("Qual temperatura você busca no dia de hoje? "))
print(existeTemperatura(temperatura_do_dia, busca_temperatura))