# Clara Andrade Sant'Anna Santos
# Julia Enriquetto de Brito 
import random 
import math
import matplotlib.collections as mc
import matplotlib.pylab as pl
import matplotlib.pyplot as plt
import tkinter as tk  # bib de interface gráfica (GUIs)
from tkinter import filedialog # o filedialog serve para selecionar arquivos

# Informe a quantidade de viajantes e de cidades antes de rodar o projeto (de acordo com as instâncias disponibilizadas)
n_travellers = 3
n_cities = 48

#1. Método que lê o arquivo e mostra a quantidade de caixeiros e a matriz
def read_arq_txt():
    root = tk.Tk()
    root.withdraw()  # Esconde a janela principal
    name_arq = filedialog.askopenfilename(title="Selecione o arquivo TXT")  # Abre o explorador de arquivos
    with open(name_arq, 'r') as arq:
        lines = arq.readlines()
        m_cities = []
        for line in lines:
            x = int(line[3:6])  # Lê os caracteres 4 ao 6 como valor de x 
            y = int(line[7:10])  # Lê os caracteres 8 ao 10 como valor de y
            m_cities.append((x, y))
        return m_cities

m_cities = read_arq_txt() # matriz de cidades
matrix = m_cities

# Exemplo de uso - testes de funcionamento
# print(m_cities)

# 2. Dividir a quantidade de cidades para cada caixeiro
def n_cities_per_traveler(travellers, cities):

    routes = [] # vetor que retorna a quantidade de cidades que cada caixeiro ira viajar
    cities_per_travellers = int (cities / travellers) 
    rest = int(cities % travellers)
    routes = [cities_per_travellers] * travellers # divide as cidades para cada viajante

    # as cidades que restarem serão somadas aos primeiros caixeiros do vetor
    for i in range(rest):
        routes[i] += 1
        
    return routes

n_cities_to_be_visited = n_cities_per_traveler(n_travellers, n_cities) # vetor que possui a quantidade de caminhos por caixeiro

# Exemplo de uso
# print(n_cities_per_traveler(n_travellers, n_cities))

# 3. Percorrer a matriz e calcular qual é o ponto mais distante a partir
# do primeiro ponto da matriz
def euclidean_distance(ponto1, ponto2):
    # Calcula a distância euclidiana entre dois pontos no plano cartesiano. ex. pontos:(x1, y1), (x2, y2)
    # Utilizamos como base o metodo do código do professor, feito em aula 

    x1, y1 = ponto1 
    x2, y2 = ponto2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Encontra a posição mais distante em relação à primeira posição na matriz de pontos
def farthest_city(m):
    cities = m[0]
    max_distance = 0
    max_position = tuple()

    for position in m:
        dist = euclidean_distance(cities, position)
        if dist > max_distance:
            max_distance = dist
            max_position = position

    return max_position

final_city = farthest_city(matrix) # pegando a ultima posicao da matriz

# Exemplo de uso
# print("A matriz é: ", matrix, "A primeira posicao da matriz é: ", matrix[0], " já a mais distante é: ", farthest_city(matrix))

# 4. Media entre a primeira posicao da matriz e a posicao mais longe da matriz
def avarage_distance(p1, p2):
    m_x = int((p1[0] + p2[0]) / 2) # calculando media de x
    m_y = int((p1[1] + p2[1]) / 2) # calculando media de y
    return (m_x, m_y) # media dos dois valores

city_avarage_distance = avarage_distance(matrix[0], final_city) # media das disntancia entre a cidade inicial e final

# Exemplo de uso
# print("Media entre a cidade inicial", starting_city, "até a cidade final ", final_city, "é", city_avarage_distance)

# 5. Ir para a cidade mais próxima da media criada acima, parecido
# com o metodo farthest_city
def nearby_city(m, distance_avarage, already_visited):
    
    min_distance = float('inf') # float('inf') foi utilizado para inicializar a variável utilizando infinito (inf) +
    nearst_city = tuple()

    for p in m:
        dist = euclidean_distance(p, distance_avarage)
        if dist < min_distance and p not in already_visited:
            min_distance = dist
            nearst_city = p

    return nearst_city

next_city = nearby_city(matrix, city_avarage_distance, [])

# Exemplo de uso
# print("A matriz é", matrix, "sua ultima posicao é", final_city ,"o ponto médio é", city_avarage_distance, 
#      "e seu ponto mais proximo na matriz é", next_city)


# 6. Gerar matriz que tem a ordem dos caminhos(cidades) a serem percorridos 
# Recebemos ajuda do monitor Marcos para arrumar esse método, porque estava com erro tanto de execução quanto de lógica
def ordered_paths(m):
    if n_cities == 1: 
        return [m[0]]

    if n_cities == 2:
        return [m[0], final_city]

    vet_routes = [m[0], final_city, next_city]

    for i in range(1, n_cities - 1):
        avg = avarage_distance(vet_routes[i], vet_routes[i+1])
        next = nearby_city(matrix, avg, vet_routes)
        vet_routes.append(next)

    return vet_routes
        
routes = ordered_paths(matrix)

# Exemplo de uso
# print("O vetor de caminhos para serem percorridos de acordo com a heruristica = ", routes)

# 7. Dar as cidades para os caixeiros de acordo com o vet_caminhos e a quantidade cidades
# que cada caixeiro deverá viajar. Cada caixeiro viajante terá o seu vetor de caminhos
def sort_cities_per_traveler(city, quant):
    distributions = []
    for quantity in quant:
        distribution = city[:quantity] # começa a partir do 1 :quantity
        distributions.append(distribution)
        city = city[quantity:]
    return distributions

distributions = sort_cities_per_traveler(routes, n_cities_to_be_visited) 
# print(distributions)

# Exemplo de uso
#for i, distribution in enumerate(distributions):
#   print(f"Viajante {i + 1} irá passar por:", distribution)

# 8. Calcula a eficiencia da nossa heuristica
def get_total_distance(mVet):
    add_distance = 0
    for v in mVet:
        distance_vector = 0
        for i in range(1, len(v)):
            p_previous = v[i - 1]
            p_current = v[i]
            distance = math.sqrt((p_current[0] - p_previous[0])**2 + (p_current[1] - p_previous[1])**2)
            distance_vector += distance
        add_distance += int(distance_vector)
    return add_distance

# Exemplo de uso 
add_distance = get_total_distance(distributions)
print("A soma das distâncias dos vetores é:", add_distance)

# 9. Desehar gráfico 
# Para desenhar o gráfico usaremos a matriz routes, que já retorna a ordem das cidades certas a serem percorridas
# porém o metodo que cria o routes, gera no final um elemento vazio (), por isso esse método serve apenas para 
# apagar esse ultimo elemento vazio. Criando uma nova rota a que vai ser desenhada
def remove_empty(routes):
    # Verifica se a matriz não está vazia
    if routes:
        # Percorre a matriz de trás para frente
        for i in range(len(routes) - 1, -1, -1):
            if not routes[i]:  # Verifica se o elemento é vazio
                routes.pop(i)  # Remove o elemento vazio
                break  # Sai do loop após remover o elemento vazio
    return routes

new_routes = remove_empty(routes) # A partir da nova rota vamos desenhar o gráfico

plt.figure(figsize=(10, 10))
plt.gca().set_aspect('equal', adjustable='box')  # Mantém a proporção entre os eixos

# Desenha os pontos
x, y = zip(*new_routes)
plt.scatter(x, y)

# Adiciona os rótulos dos pontos
for i, (x, y) in enumerate(new_routes):
    plt.annotate(f"{i+1}", (x, y), textcoords="offset points", xytext=(0,10), ha='center')

# Desenha as linhas entre os pontos
for i in range(len(new_routes) - 1):
    x_values = [new_routes[i][0], new_routes[i+1][0]]
    y_values = [new_routes[i][1], new_routes[i+1][1]]
    plt.plot(x_values, y_values, 'k-')

# Adiciona a linha final entre o último e o primeiro ponto
x_values = [new_routes[-1][0], new_routes[0][0]]
y_values = [new_routes[-1][1], new_routes[0][1]]
plt.plot(x_values, y_values, 'k-')

plt.xlabel('Coordenadas X')
plt.ylabel('Coordenadas Y')
plt.title('Multiplos Caixeiros Viajantes')

plt.grid(True)

# Salva a imagem em um arquivo
plt.savefig('desenho_caminhos.png')

plt.show()
