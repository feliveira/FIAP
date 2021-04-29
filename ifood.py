restaurantes = [["Sukiya - Saúde", 4.6, 7.99],
                ["A Feijoada", 4.4, 9.90],
                ["Kibon Sorveteria - Saúde", 4.9, 6.99],
                ["Giraffas Carrefour Metrocar", 4.4, 5.99],
                ["Makis Place - Saúde", 4.7, 7.99],
                ["Viena - Shopping Santa Cruz", 4.4, 12.49]]

lista_notas = []

for notas in restaurantes:
    lista_notas.append(notas[1])
    
lista_notas.sort()
lista_notas.reverse()

restaurantes_ordenados = []

# Ordena os restaurantes por nota em ordem decrescente
while len(lista_notas) > 0:
    for restaurante in restaurantes:
        if restaurante[1] == lista_notas[0]:
            restaurantes_ordenados.append(restaurante)
            lista_notas.pop(0)

# Lida com o frete
for x in range(1,len(restaurantes_ordenados)):
 if restaurantes_ordenados[x][1] == restaurantes_ordenados[x-1][1]:
   if restaurantes_ordenados[x][2] < restaurantes_ordenados[x-1][2]:
     restaurante_maior_frete = restaurantes_ordenados[x-1]
     restaurantes_ordenados[x-1] = restaurantes_ordenados[x]
     restaurantes_ordenados[x] = restaurante_maior_frete

print("\nO ranking dos restaurantes próximos ao endereço de entrega seguindo os critérios de avaliação e valor do frete foi:\n")
for x in range(len(restaurantes_ordenados)):
    print("{}° {} | Nota: {} | Valor do Frete: R$ {}".format(x+1,restaurantes_ordenados[x][0],restaurantes_ordenados[x][1],restaurantes_ordenados[x][2]))
    
