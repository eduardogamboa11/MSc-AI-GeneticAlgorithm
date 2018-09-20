
def get_population():
    rows = 10 
    columns = 10
    #create random population of 10x10 with 0-255 values for each.
    population = [[random.randrange(255)]*rows for i in range(columns)]

    print(population)


