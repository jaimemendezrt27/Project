import random
###exercise 1
def generate_individual_bitstring(size):
    i = 0
    individual = []
    while i < size:
        bitstring = random.randint(0,1)
        individual.append(bitstring)
        i += 1
    return individual
def generate_individual_permutation(size):
    individual2 = list(range(size))
    random.shuffle(individual2)
    return individual2
def generate_population(population_size, function, size):
    population = []
    i = 0
    while i < population_size:
        individual = function(size)
        population.append(individual)
        i += 1
    return population

if __name__ == "__main__":

    # EXERCISE 1
    populationbitstring = generate_population(4, generate_individual_bitstring, 6)
    print(populationbitstring)

    populationpermutation = generate_population(4, generate_individual_permutation, 6)
    print(populationpermutation)