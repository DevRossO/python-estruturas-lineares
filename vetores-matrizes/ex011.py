# Filtro de Contraste: Percorra o vetor de pixels e multiplique cada valor por 1.2. Se o
# resultado for maior que 255, force o valor para 255 (Truncamento)


vetor_linear = [230, 2, 3, 43, 4, 5, 6, 7, 8, 1, 2, 4, 5, 6, 7, 8]
novo_vetor = []

for i in vetor_linear:
    res = i * 1.2

    if res > 255:
        res = 255

    novo_vetor.append(int(res))

print(novo_vetor)
