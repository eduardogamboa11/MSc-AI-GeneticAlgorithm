import numpy
import math
import random
from matplotlib import pyplot as plt


def get_population(allele, genotype, individuals):    
    population = numpy.random.randint(2**allele, size=(individuals, genotype))

    return population


def tournament(population, individuals):
    number_of_contestants = 20
    
    contestants = numpy.random.randint(individuals, size=number_of_contestants)
    winner = population[min(contestants)]
    
    return winner


def get_aptitude(ind):
    A, B, C, D, E, F, G, H = 25, 123, 13, 15, 0.08, 80, 16, 15

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

    for t in range(500):
        x = (A * math.exp(-t/B)) * (C * math.sin(t/D)) + (E * math.exp(t/F)) * (G * math.cos(t/H))
        y = (A1 * math.exp(-t/B1)) * (C1 * math.sin(t/D1)) + (E1 * math.exp(t/F1)) * (G1 * math.cos(t/H1))
        aptitude += abs(x - y)    

    return aptitude
    

def get_child(father, mother, population, individuals):
    cut_distance = random.randint(1,len(father)-1)
    mutation_numbers = numpy.random.randint(len(father), size=math.ceil(len(father)*0))

    father_x = father[:cut_distance]
    father_y = father[cut_distance:]
    mother_x = mother[:cut_distance]
    mother_y = mother[cut_distance:]

    child1 = father_x + mother_y
    child2 = mother_x + father_y
    
    if cut_distance in mutation_numbers:
        mutation_bit = random.randint(1,len(father)-1)

        if child1[mutation_bit-1] is '0':
            child1 = child1[:mutation_bit - 1] + '1' + child1[mutation_bit:]
        elif child1[mutation_bit-1] is '1':   
            child1 = child1[:mutation_bit - 1] + '0' + child1[mutation_bit:]
    
    return child1, child2


def many_to_one(individual):
    binary_string = ''

    for chromosome in individual:
        binary_string += '{0:08b}'.format(chromosome)

    return binary_string


def one_to_many(allele, genotype, individual):
    numbers = numpy.empty([genotype], dtype=int)

    for i in range(genotype):
        numbers[i] = int(individual[i*allele:(i+1)*allele], 2)
    
    return numbers


allele = 8
genotype = 8 
individuals = 2000
population = get_population(allele, genotype, individuals)
'''
#test best result 1908
A, B, C, D, E, F, G, H = 25, 123, 13, 15, 0.08, 80, 16, 15
a1,b1,c1,d1,e1,f1,g1,h1= 16, 129, 19, 15,   53/500, 84, 16, 15 
x = []
y = []
for t in range(500):
    x.append((A * math.exp(-t/B)) * (C * math.sin(t/D)) + (E * math.exp(t/F)) * (G * math.cos(t/H)))
    y.append((a1 * math.exp(-t/b1)) * (c1 * math.sin(t/d1)) + (e1 * math.exp(t/f1)) * (g1 * math.cos(t/h1)))

plt.plot(x, 'blue', y, 'red')
plt.show()
'''

evolution = []
for gen in range(100):
    new_population = []
    for i in range(int(individuals/2)):
        father = tournament(population, individuals)
        mother = tournament(population, individuals)
        
        father_b = many_to_one(father)
        mother_b = many_to_one(mother)

        child1_bin, child2_bin = get_child(father_b, mother_b, population, individuals)
        child_1 = one_to_many(allele, genotype, child1_bin)
        child_2 = one_to_many(allele, genotype, child2_bin)

        new_population.append([child_1, get_aptitude(child_1)])
        new_population.append([child_2, get_aptitude(child_2)])

    results = sorted(new_population, key=lambda x:(x[1]))
    #for i in range(100):
    #    evolution.append(results[99-i][1])
    #plt.plot(evolution, 'blue')
    #plt.show()
    print('gen:', gen)
    print('1   ', results[0])
    print('10  ', results[10])
    print('20  ', results[20])
    print('100 ', results[100])
    print('200 ', results[200])
    print('300 ', results[300])
    print('400 ', results[400])
    print('500 ', results[500])
    print('600 ', results[600])
    print('800 ', results[800])
    print('1000', results[1000])
    print('1100', results[1100])
    print('1200', results[1200])
    print('1500', results[1500])
    print('1800', results[1800])
    print('2000', results[1999])

    for individual in range(individuals):
        population[individual]=results[individual][0]

