# Restaurantes participantes
restaurantes = [["Sukiya - Saúde", 4.6, 2.5],
                ["A Feijoada", 4.4, 9.90],
                ["Makis Place - Saúde", 4.7, 7,99],
                ["Kibon Sorveteria - Saúde", 4.9, 6.99],
                ["Lanchonete do Clebinho",4.9, 2.5],
                ["Giraffas Carrefour Metrocar", 4.4, 5.99],
                ["Viena - Shopping Santa Cruz", 4.4, 12.49]]

# Cria lista para armazenar as notas do restaurante
lista_notas = []

# Percorre a lista de restaurantes e armazena as notas em uma lista independente
for notas in restaurantes:
    lista_notas.append(notas[1])

# Organiza a lista de notas em ordem decrescente
lista_notas.sort()
lista_notas.reverse()

# Cria lista para armazenar os restaurantes ordenados por notas
restaurantes_por_notas = []

# Enquanto a lista de notas tiver valores, ordena os restaurantes por nota em ordem decrescente
while len(lista_notas) > 0:
    for maior in restaurantes:
        if maior[1] == lista_notas[0]:
            restaurantes_por_notas.append(maior)
            lista_notas.pop(0)



# ============================ LIDAR COM O FRETE ==========================

# Cria lista para armazenar os valores dos fretes
lista_fretes = []

# Percorre a lista de restaurantes ordenados por nota e armazena em outra lista o tempo do frete
for frete in restaurantes_por_notas:
    lista_fretes.append(frete[2])

# Ordena a lista de tempo do frete em ordem crescente
lista_fretes.sort()

print(lista_fretes)

while len(lista_fretes) > 0:
    for frete in restaurantes_por_notas:
        if frete[2] == lista_fretes[0]:
            restaurantes_ordenados.append(frete)
            lista_fretes.pop(0)

print(restaurantes_ordenados)







