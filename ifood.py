# Restaurantes participantes
restaurantes = [["Sukiya - Saúde", 4.6, 7.99],
                ["A Feijoada", 4.4, 9.90],
                ["Kibon Sorveteria - Saúde", 4.9, 6.99],
                ["Giraffas Carrefour Metrocar", 4.4, 5.99],
                ["Makis Place - Saúde", 4.7, 7.99],
                ["Viena - Shopping Santa Cruz", 4.4, 12.49]]

# Cria lista para armazenar as notas dos restaurantes
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

# Percorre a lista ordenada por notas começando do segundo item
for x in range(1,len(restaurantes_por_notas)):  
# Compara a nota do segundo item atual da lista com a do primeiro, se ambas as notas forem iguais,
# lidará com o critério de desempate: o frete
 if restaurantes_por_notas[x][1] == restaurantes_por_notas[x-1][1]:
   # Verifica se o valor do frete do segundo termo é menor que a do anterior
   if restaurantes_por_notas[x][2] < restaurantes_por_notas[x-1][2]:
     # Se a condição for verdadeira utiliza a variável "restaurante" para realizar as trocas de posições
     # Salva o restaurante de frete menor
     restaurante = restaurantes_por_notas[x-1]
     # Coloca o restaurante de maior frete na posição seguinte
     restaurantes_por_notas[x-1] = restaurantes_por_notas[x]
     # Substitui a posição anterior com o restaurante de menor frete 
     restaurantes_por_notas[x] = restaurante

# Imprime o ranking de restaurantes
for x in range(len(restaurantes_por_notas)):
    print("{}° {} | Nota: {} | Valor do Frete: R$ {}".format(x+1,restaurantes_por_notas[x][0],restaurantes_por_notas[x][1],restaurantes_por_notas[x][2]))
    

