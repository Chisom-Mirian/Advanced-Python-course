
# Imports 
import numpy as np

#import pdb; pdb.set_trace()

from datetime import datetime


n_cities = 10

n_population = 10

mutation_rate = 0.3
# Generating a list of coordenades representing each city

coordinates_list  = []

with open(f'data/SwedenCities.data', 'r') as handle:
        lines = handle.readlines()
        for line in lines:
            [x, y] = map(float, line.split())

            coordinates_list .append([x,y])


names_list = np.array(['Luleå', 'Trollhättan', 'Västerås', 'Umeå', 'Norrköpin', 'Stockholm', 'Uddevalla', 'Västervik', 'Gothenburg', 'Visby'])
cities_dist = { x:y for x,y in zip(names_list,coordinates_list)}

# Function to compute the distance between two points
def city_distance_coordinates(a,b):
    return ((a[0]-b[0])**2+(a[1]-b[1])**2)**0.5

def city_distance_names(city_a, city_b, cities_dist):
    return city_distance_coordinates(cities_dist[city_a], cities_dist[city_b])


# First step: Create the first population set
def gen1(city_list, n_population):

    population_set = []
    for i in range(n_population):
        #Randomly generating a new solution
        sol_i = city_list[np.random.choice(list(range(n_cities)), n_cities, replace=False)]
        population_set.append(sol_i)
    return np.array(population_set)

#import pdb; pdb.set_trace()

population_set = gen1(names_list, n_population)

population_set 
 
#pdb

def fitness(city_list, cities_dist):
    total = 0
    for i in range(n_cities-1):
        a = city_list[i]
        b = city_list[i+1]
        total += city_distance_names(a,b, cities_dist)
    return total


def get_all_fitnes(population_set, cities_dict):
    fitnes_list = np.zeros(n_population)

    #Looping over all solutions computing the fitness for each solution
    for i in  range(n_population):
        fitnes_list[i] = fitness(population_set[i], cities_dict)

    return fitnes_list

fitnes_list = get_all_fitnes(population_set,cities_dist)
fitnes_list


def fitness_eval(city_list, cities_dist):
    total = 0
    for i in range(n_cities-1):
        a = city_list[i]
        b = city_list[i+1]
        total += city_distance_names(a,b, cities_dist)
    return total
def get_all_fitnes(population_set, cities_dict):
    fitnes_list = np.zeros(n_population)

    #Looping over all solutions computing the fitness for each solution
    for i in  range(n_population):
        fitnes_list[i] = fitness_eval(population_set[i], cities_dict)

    return fitnes_list

fitnes_list = get_all_fitnes(population_set,cities_dist)
fitnes_list

def prog_selection(population_set,fitnes_list):
    total_fit = fitnes_list.sum()
    prob_list = fitnes_list/total_fit
    

    prog_list_a = np.random.choice(list(range(len(population_set))), len(population_set),p=prob_list, replace=True)
    prog_list_b = np.random.choice(list(range(len(population_set))), len(population_set),p=prob_list, replace=True)
    
    prog_list_a = population_set[prog_list_a]
    prog_list_b = population_set[prog_list_b]
    
    
    return np.array([prog_list_a,prog_list_b])


prog_list = prog_selection(population_set,fitnes_list)
prog_list[0][2]


def mate_prog(prog_a, prog_b):
    offspring = prog_a[0:5]

    for city in prog_b:

        if not city in offspring:
            offspring = np.concatenate((offspring,[city]))

    return offspring
            
    
    
def mate_population(prog_list):
    new_population_set = []
    for i in range(prog_list.shape[1]):
        prog_a, prog_b = prog_list[0][i], prog_list[1][i]
        offspring = mate_prog(prog_a, prog_b)
        new_population_set.append(offspring)
        
    return new_population_set

new_population_set = mate_population(prog_list)
new_population_set[0]


def mutate_offspring(offspring):
    for q in range(int(n_cities*mutation_rate)):
        a = np.random.randint(0,n_cities)
        b = np.random.randint(0,n_cities)

        offspring[a], offspring[b] = offspring[b], offspring[a]

    return offspring
    
    
def mutate_population(new_population_set):
    mutated_pop = []
    for offspring in new_population_set:
        mutated_pop.append(mutate_offspring(offspring))
    return mutated_pop

mutated_pop = mutate_population(new_population_set)
mutated_pop[0]


best_solution = [-1,np.inf,np.array([])]
for i in range(10):
    if i%100==0: print(i, fitnes_list.min(), fitnes_list.mean(), datetime.now().strftime("%d/%m/%y %H:%M"))
    fitnes_list = get_all_fitnes(mutated_pop,cities_dist)
    
    #Saving the best solution
    if fitnes_list.min() < best_solution[1]:
        best_solution[0] = i
        best_solution[1] = fitnes_list.min()
        best_solution[2] = np.array(mutated_pop)[fitnes_list.min() == fitnes_list]
    
    prog_list = prog_selection(population_set,fitnes_list)
    new_population_set = mate_population(prog_list)
    
    mutated_pop = mutate_population(new_population_set)
    
    
    best_solution
