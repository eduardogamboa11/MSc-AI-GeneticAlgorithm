import numpy
import math
import random
from matplotlib import pyplot as plt


def get_population(alleles, chromosomes, individuals):    
    population = numpy.random.randint(2**alleles, size=(individuals, chromosomes))

    return population


def tournament(population, individuals):
    number_of_contestants = 20
    
    contestants = numpy.random.randint(individuals, size=number_of_contestants)
    winner = population[min(contestants)]
    
    return winner


def numbers_to_string(individual):
    binary_string = ''

    for chromosomes in individual:
        binary_string += '{0:08b}'.format(chromosomes)

    return binary_string
    

def get_child(father, mother, population, individuals):
    cut_distance = random.randint(1,len(father)-1)

    father_x = father[:cut_distance]
    father_y = father[cut_distance:]
    mother_x = mother[:cut_distance]
    mother_y = mother[cut_distance:]

    child1 = father_x + mother_y
    child2 = mother_x + father_y

    #Mutation
    mutation_numbers = numpy.random.randint(len(father), size=math.ceil(len(father)*mutation_probability))
    
    if cut_distance in mutation_numbers:
        mutation_bit = random.randint(1,len(father)-1)

        if child1[mutation_bit-1] is '0':
            child1 = child1[:mutation_bit - 1] + '1' + child1[mutation_bit:]
        elif child1[mutation_bit-1] is '1':   
            child1 = child1[:mutation_bit - 1] + '0' + child1[mutation_bit:]
    
    return child1, child2


def string_to_numbers(alleles, chromosomes, individual):
    numbers = numpy.empty([chromosomes], dtype=int)

    for i in range(chromosomes):
        numbers[i] = int(individual[i*alleles:(i+1)*alleles], 2)
    
    return numbers


def get_aptitude(ind):
    A, B, C, D, E, F, G, H = 25, 123, 13, 15, 0.08, 80, 16, 15

    #Avoid division by 0
    for i in range(len(ind)):
        if ind[i] == 0:
            ind[i] = 1

    A1 = ind[0]
    B1 = ind[1]
    C1 = ind[2]
    D1 = ind[3]
    E1 = ind[4]/500
    F1 = ind[5]
    G1 = ind[6]
    H1 = ind[7]

    aptitude = 0

    #calculate difference from target with individual for every x(t) 
    for t in range(500):
        x = (A * math.exp(-t/B)) * (C * math.sin(t/D)) + (E * math.exp(t/F)) * (G * math.cos(t/H))
        y = (A1 * math.exp(-t/B1)) * (C1 * math.sin(t/D1)) + (E1 * math.exp(t/F1)) * (G1 * math.cos(t/H1))
        aptitude += abs(x - y)    

    return aptitude


def graph_comparison(individual):
    #Use to compare graphs between target and individual
    A, B, C, D, E, F, G, H = 25, 123, 13, 15, 0.08, 80, 16, 15

    for i in range(len(individual)):
        if individual[i] == 0:
            individual[i] = 1

    A1 = individual[0]
    B1 = individual[1]
    C1 = individual[2]
    D1 = individual[3]
    E1 = individual[4]/500
    F1 = individual[5]
    G1 = individual[6]
    H1 = individual[7]

    x = []
    y = []

    for t in range(500):
        x.append((A * math.exp(-t/B)) * (C * math.sin(t/D)) + (E * math.exp(t/F)) * (G * math.cos(t/H)))
        y.append((A1 * math.exp(-t/B1)) * (C1 * math.sin(t/D1)) + (E1 * math.exp(t/F1)) * (G1 * math.cos(t/H1)))

    plt.plot(x,"blue",y,"red")
    plt.show()


alleles = 8
chromosomes = 8 
individuals = 2000
population = get_population(alleles, chromosomes, individuals)
mutation_probability = 0.015

for gen in range(1):
    new_population = []
    for i in range(int(individuals/2)):
        father = tournament(population, individuals)
        mother = tournament(population, individuals)
        
        father_b = numbers_to_string(father)
        mother_b = numbers_to_string(mother)

        child1_bin, child2_bin = get_child(father_b, mother_b, population, individuals)
        child_1 = string_to_numbers(alleles, chromosomes, child1_bin)
        child_2 = string_to_numbers(alleles, chromosomes, child2_bin)

        new_population.append([child_1, get_aptitude(child_1)])
        new_population.append([child_2, get_aptitude(child_2)])

    results = sorted(new_population, key=lambda x:(x[1]))

    print('gen:', gen)
    print(results[0])

    for individual in range(individuals):
        population[individual]=results[individual][0]

#COMPARISON
graph_comparison(population[0])
