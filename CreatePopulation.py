import numpy
import math
import random

def get_population(bits, genotype, individuals):
    
    population = numpy.random.randint(2**bits, size=(individuals, genotype))

    return population


def tournament(population, individuals):
    number_of_contestants = 3
    
    contestants = numpy.random.randint(individuals, size=number_of_contestants)
    winner = population[min(contestants)]
    
    return winner


def get_aptitude(ind):
    A, B, C, D, E, F, G, H = 25, 123, 13, 15, 0.08, 80, 16, 15

    A1 = ind[0]/5
    B1 = ind[1]
    C1 = ind[2]/10
    D1 = ind[3]/10
    E1 = ind[4]/500
    F1 = ind[5]/2
    G1 = ind[6]/10
    H1 = ind[7]/10

    aptitude = A-A1 + B-B1 + C-C1 + D-D1 + E-E1 + F-F1 + G-G1 + H-H1
    
    return aptitude
'''
    for t in range(500):
        x(t) = a*exp(-t/b)-c*sin(t/d) + e*exp(t/f)-g*cos(t/h) 
'''
    

def get_child(father, mother):
    cut_distance = random.randint(1,len(father)-1)
    print(cut_distance)
    
    father_x = father[:cut_distance]
    father_y = father[cut_distance:]
    mother_x = mother[:cut_distance]
    mother_y = mother[cut_distance:]

    child1 = father_x + mother_y
    child2 = mother_x + father_y

    return child1, child2


def many_to_one(individual):
    binary_string = ''

    for chromosome in individual:
        binary_string += '{0:08b}'.format(chromosome)
    
    return binary_string


def one_to_many(bits, genotype, individual):
    numbers = numpy.empty([genotype], dtype=int)

    for i in range(genotype):
        numbers[i] = int(individual[i*bits:(i+1)*bits], 2)
    
    return numbers


def main():
    bits = 8
    genotype = 8 
    individuals = 10
    population = get_population(bits, genotype, individuals)
    new_population = []

    for i in range(int(individuals/2)):
        father = tournament(population, individuals)
        mother = tournament(population, individuals)
        
        father_b = many_to_one(father)
        mother_b = many_to_one(mother)

        child1_bin, child2_bin = get_child(father_b, mother_b)
        
        child_1 = one_to_many(bits, genotype, child1_bin)
        print('dadx',father)
        print('son1',child_1)
        print('momx',mother)
        child_2 = one_to_many(bits, genotype, child2_bin)
        print('son2',child_2, '\n')
        new_population.append([child_1, get_aptitude(child_1)])
        new_population.append([child_2, get_aptitude(child_2)])

    results = sorted(new_population, key=lambda x:(-abs(x[1])))

    for i in range(individuals):
        population[i]=results[i][0]

main()

