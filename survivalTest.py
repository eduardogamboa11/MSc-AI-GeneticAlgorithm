import numpy
import math
import random
from matplotlib import pyplot as plt


def tournament(population, individuals):
    number_of_contestants = 50
    
    contestants = numpy.random.randint(individuals, size=number_of_contestants)
    winner = population[min(contestants)]
    
    return winner


def many_to_one(individual):
    binary_string = ''

    for chromosomes in individual:
        binary_string += '{0:01b}'.format(chromosomes)

    return binary_string


def get_child(father, mother, population, individuals):
    cut_distance = random.randint(1,len(father)-1)


    father_x = father[:cut_distance]
    father_y = father[cut_distance:]
    mother_x = mother[:cut_distance]
    mother_y = mother[cut_distance:]

    child1 = father_x + mother_y
    child2 = mother_x + father_y
    
    mutation_number = random.randint(0, int(100/mutation_probability))

    if mutation_number is 100:
        mutation_bit = random.randint(1,len(father)-1)

        if child1[mutation_bit-1] is '0':
            child1 = child1[:mutation_bit - 1] + '1' + child1[mutation_bit:]
        elif child1[mutation_bit-1] is '1':   
            child1 = child1[:mutation_bit - 1] + '0' + child1[mutation_bit:]
    
    return child1, child2


def one_to_many(allele, chromosomes, individual):
    numbers = numpy.empty([chromosomes], dtype=int)

    for i in range(chromosomes):
        numbers[i] = int(individual[i*allele:(i+1)*allele], 2)

    return numbers

    
def get_aptitude(individual):
    aptitude = 0
    total_weight = 0
    weights = individual*gear_weights

    for weight in weights:
        total_weight += weight

    if total_weight < max_weight:
        values = individual*gear_values
        for value in values:
            aptitude += value

    return aptitude


allele = 1
individuals = 10000
chromosomess = 9
mutation_probability = 0.015
generations = 1
max_weight = 80

survival_gear = [
    {'Name':'Food','Weight':15,'Value':5},
    {'Name':'Matches','Weight':8,'Value':6},
    {'Name':'Map','Weight':8,'Value':3},
    {'Name':'Shelter','Weight':50,'Value':7},
    {'Name':'Knife','Weight':10,'Value':8},
    {'Name':'Rope','Weight':20,'Value':8},
    {'Name':'Extra Clothes','Weight':30,'Value':5},
    {'Name':'Water','Weight':15,'Value':6},
    {'Name':'Bow and Arrow','Weight':40,'Value':7}
]

gear_weights = []
gear_values = []
for gear in survival_gear:
    gear_weights.append(gear['Weight'])
    gear_values.append(gear['Value'])


population = numpy.random.randint(2**allele, size=(individuals, chromosomess))

for gen in range(generations):
    new_population = []
    for i in range(int(individuals/2)):
        father = tournament(population, individuals)
        mother = tournament(population, individuals)
        
        father_b = many_to_one(father)
        mother_b = many_to_one(mother)

        child1_bin, child2_bin = get_child(father_b, mother_b, population, individuals)
        child_1 = one_to_many(allele, chromosomess, child1_bin)
        child_2 = one_to_many(allele, chromosomess, child2_bin)

        new_population.append([child_1, get_aptitude(child_1)])
        new_population.append([child_2, get_aptitude(child_2)])

    results = sorted(new_population, key=lambda x:(-x[1]))

    print('gen:', gen)
    for i in range(10000):
        if i%1000 is 0:
            print(results[i])


    for individual in range(individuals):
        population[individual]=results[individual][0]