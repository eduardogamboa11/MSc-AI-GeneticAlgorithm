import numpy

def get_population(rows, columns):
    population = numpy.random.randint(255, size=(rows,columns))

    return population


def tournament(population, columns):
    number_of_contestants = 3
    contestants = numpy.random.randint(columns, size=number_of_contestants)

    return min(contestants)


def main():
    rows = 20 
    columns = 20

    population = get_population(rows, columns)

    father = tournament(population, columns)
    mother = tournament(population, columns)

    print("Father", population[father])
    print("Mother", population[mother])


main()