import random 
import math
#import mathplotlib.collection as mc
#import mathplotlib.pylab as pl

n_travellers = 10 #numero de caixeiros viajantes 
n_cities = 22

# 1. Metodo que cria a matriz 
# esse metodo é só para criarmos uma matriz para testarmos 
# a nossa heuristica, ou seja, ela não sera utilizada
def create_random_problem(n_cities): 

    coordinates = [] #listas são mutaveis

    for _ in range(n_cities): 
        coordinates.append(
            (
                int(random.uniform(0, 100)), 
                int(random.uniform(0, 100))
            )
        )

    distances = [[0 for i in range(n_cities)] for i in range(n_cities)] 

    for i in range(n_cities):
        for j in range(i + 1 , n_cities): 
            distances[i][j] = distances [i][j] = int(       #tuplas são imutaveis
                math.sqrt(
                    (coordinates[j][0] - coordinates[i][0])**2 + #(x1 - x0)
                    (coordinates[j][1] - coordinates[i][1])**2   #(y1 - y0)
                )
            )
    
    return coordinates

# Exemplo de uso
# print(create_random_problem(5))

# 2. Caminhar pelo vetor e ver a quantidade de cidades
matrix = create_random_problem(5)
 
def quantity_cities(matrix):
    i = 0
    for _ in matrix:
        i += 1
    return i

# Exemplo de uso
# print("A matriz possui", quantity_cities(matrix), "cidades.")
quant_cities = quantity_cities(matrix)

# 3. Dividir a quantidade de cidades para cada caixeiro
def n_cities_per_traveler(travellers, cities):

    routes = [] # vetor que retorna a quantidade de cidades que cada caixeiro ira viajar
    cities_per_travellers = int (cities / travellers) 
    rest = int(cities % travellers)
    routes = [cities_per_travellers] * travellers # divide as cidades para cada viajante

    # as cidades que restarem serão somadas aos primeiros caixeiros do vetor
    for i in range(rest):
        routes[i] += 1
        
    return routes

routes = n_cities_per_traveler(n_travellers, n_cities) # vetor que possui a quantidade de caminhos por caixeiro

# Exemplo de uso
# print(n_cities_per_traveler(n_travellers, n_cities))

# 4. Percorrer a matrix e calcular qual é o ponto mais distante a partir
# do primeiro ponto da matriz
def euclidean_distance(ponto1, ponto2):
    # Calcula a distância euclidiana entre dois pontos no plano cartesiano. ex. pontos:(x1, y1), (x2, y2)

    x1, y1 = ponto1 
    x2, y2 = ponto2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Encontra a posição mais distante em relação à primeira posição na matriz de pontos.
def farthest_city(m):
    cities = m[0]
    max_distance = 0
    max_position = False

    for position in m:
        dist = euclidean_distance(cities, position)
        if dist > max_distance:
            max_distance = dist
            max_position = position

    return max_position

final_city = farthest_city(matrix) # pegando a ultima posicao da matriz

# Exemplo de uso
# print("A matriz é: ", matrix, "A primeira posicao da matriz é: ", matrix[0], " já a mais distante é: ", farthest_city(matrix))

# 5. Media entre a primeira posicao da matriz e a posicao mais longe da matriz
def avarage_distance(p1, p2):
    m_x = int((p1[0] + p2[0]) / 2) # calculando media de x
    m_y = int((p1[1] + p2[1]) / 2) # calculando media de y
    return (m_x, m_y) # media dos dois valores

city_avarage_distance = avarage_distance(matrix[0], final_city) #media das disntancia entre a cidade inicial e final

# Exemplo de uso
# print("Media entre a cidade inicial", starting_city, "até a cidade final ", final_city, "é", city_avarage_distance)

# 6. Ir para a cidade mais próxima da media criada acima, parecido
# com o metodo farthest_city
def distance(p1, p2): 
   return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

def nearby_city(m, distance_avarage):
    min_distance = float('inf')
    nearst_city = False

    for p in m:
        dist = euclidean_distance(p, distance_avarage)
        if dist < min_distance:
            min_distance = dist
            nearst_city = p

    return nearst_city

next_city = nearby_city(matrix, city_avarage_distance)

# Exemplo de uso
# print("A matriz é", matrix, "sua ultima posicao é", final_city ,"o ponto médio é", city_avarage_distance, 
#      "e seu ponto mais proximo na matriz é", next_city)


# 7. Gerar matriz que tem a ordem dos caminhos(cidades) a serem percorridos #ESTA COM ERRO
def ordered_paths(m):
    vet_caminhos = []
    anterior = final_city
    atual = next_city

    #vet_caminhos[0] = matrix[0] # primeira posição recebe a primeira posição da matrix
    matrix[1] = anterior # segunda posicao do vetor recebe a cidade mais longe 
    matrix[2] = atual # terceira posicao do vetor recebe a cidade mais proxima entre a media das duas cidades

    for i in vet_caminhos[2:]:
        anterior = atual
        atual = avarage_distance(anterior, atual), nearby_city(matrix, atual)
        vet_caminhos[i] = atual

    return vet_caminhos
        
#caminhos = ordered_paths(matrix)

# Exemplo de uso
#print("O vetor de caminhos para serem percorridos de acordo com a heruristica = ", caminhos)

# 8. Dar as cidades para os caixeiros de acordo com o vet_caminhos e a quantidade cidades
# que cada caixeiro deverá viajar. Cada caixeiro viajante terá o seu vetor de caminhos
def sort_cities_per_traveler(city, quant):
    distributions = []
    for quantity in quant:
        distribution = city[:quantity]
        distributions.append(distribution)
        city = city[quantity:]
    return distributions

# Exemplo de uso
distributions = sort_cities_per_traveler(matrix, routes) #DE VEZ MATRIX PRECISO COLOCAR O VETOR ORDENADO CRIADO NO METODO ACIMA
for i, distribution in enumerate(distributions):
    print(f"Viajante {i + 1} irá passar por:", distribution)

# 9. Desehar gráfico 

# 10. Ler o arquivo txt, pegar o numero de caixeiros viajantes e a matriz das cidades 