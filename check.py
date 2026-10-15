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


# EXERCISE 2
def tsp_distance(route, distances):
    total_distance = 0
    i = 0
    while i < len(route):
        total_distance += distances[route[i]][route[(i + 1) % len(route)]]
        i += 1
    return total_distance
def fitness_tsp(route):
    return 1 / tsp_distance(route, distances)


if __name__ == "__main__":
    # EXERCISE 2
    distances = [
        [0, 2, 9, 10, 7, 3],
        [2, 0, 6, 4, 3, 8],
        [9, 6, 0, 8, 5, 6],
        [10, 4, 8, 0, 7, 9],
        [7, 3, 5, 7, 0, 2],
        [3, 8, 6, 9, 2, 0]
    ]

    route = [0, 1, 2, 3, 4, 5]

    print(tsp_distance(route, distances))
    print(fitness_tsp(route))
