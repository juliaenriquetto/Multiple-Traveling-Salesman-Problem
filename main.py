import random 
import math
#import mathplotlib.collection as mc
#import mathplotlib.pylab as pl

n_travellers = 10 #numero de caixeiros viajantes 
n_cities = 22

#1. Metodo que cria a matriz 
#esse metodo é só para criarmos uma matriz para testarmos 
#a nossa heuristica, ou seja, ela não sera utilizada
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
            distances[i][j] = distances [i][j] = int(       #duplas são imutaveis
                math.sqrt(
                    (coordinates[j][0] - coordinates[i][0])**2 + #(x1 - x0)
                    (coordinates[j][1] - coordinates[i][1])**2   #(y1 - y0)
                )
            )
    
    return coordinates

#Exemplo de uso
#print(create_random_problem(5))

#2. Caminhar pelo vetor e ver a quantidade de cidades
matrix = create_random_problem(5)
 
def quantity_cities(matrix):
    i = 0
    for _ in matrix:
        i += 1
    return i

# Exemplo de uso
#print("A matriz possui", quantity_cities(matrix), "cidades.")
quant_cities = quantity_cities(matrix)

#3. Dividir a quantidade de cidades para cada caixeiro
def number_cities_traveler(travellers, cities):

    cities_per_traveller = [] #vetor que retorna a quantidade de cidades que cada caixeiro ira viajar
    n_per_travellers = int (cities / travellers)
    rest = int(cities % travellers)
    cities_per_traveller = [n_per_travellers] * travellers

    for i in range(rest):
        cities_per_traveller[i] += 1
        
    return cities_per_traveller

print(number_cities_traveler(n_travellers, n_cities))