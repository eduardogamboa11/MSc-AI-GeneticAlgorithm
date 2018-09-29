import numpy
import math


def get_population(rows, individuals):
    bits = 8
    population = numpy.random.randint(2**bits, size=(rows,individuals))

    return population


def tournament(population, individuals):
    number_of_contestants = 3
    
    contestants = numpy.random.randint(individuals + 1, size=number_of_contestants)
    winner = population[min(contestants)]
    
    return winner


def main():
    rows = 8 

    population = get_population(rows, individuals)

    father = tournament(population, individuals)
    mother = tournament(population, individuals)

    print("Father", father)
    print("Mother", mother)


main()
