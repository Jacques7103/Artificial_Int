import random

# Define the cities and their distances
cities = {
    'A': {'B': 12, 'C': 10, 'G': 12},
    'B': {'A': 12, 'C': 8, 'D': 12},
    'C': {'A': 10, 'B': 8, 'D': 11, 'E': 3, 'G': 9},
    'D': {'B': 12, 'C': 11, 'E': 11, 'F': 10},
    'E': {'C': 3, 'D': 11, 'F': 6, 'G': 7},
    'F': {'D': 10, 'E': 6, 'G': 9},
    'G': {'A': 12, 'C': 9, 'F': 9, 'E': 7}
}

# Number of generations and population size
num_generations = 100
population_size = 100

# Create an initial population with random routes starting and ending at A
def create_individual():
    cities_list = list(cities.keys())
    cities_list.remove('A')
    random.shuffle(cities_list)
    return ['A'] + cities_list + ['A']

# Define a function to calculate the total distance of a route
def calculate_route_distance(route):
    distance = 0
    for i in range(len(route) - 1):
        start_city = route[i]
        end_city = route[i + 1]
        if end_city in cities[start_city]:
            distance += cities[start_city][end_city]
        else:
            # Handle the case when there's no direct connection
            return float('inf')
    return distance

# Define a function to mutate an individual
def mutate(individual):
    if len(individual) >= 4:  # Ensure that A and at least one other city are not mutated
        idx1, idx2 = random.sample(range(1, len(individual) - 1), 2)
        individual[idx1], individual[idx2] = individual[idx2], individual[idx1]

# Create the initial population
population = [create_individual() for _ in range(population_size)]

# Main loop for genetic algorithm
for generation in range(num_generations):
    # Evaluate the fitness of each individual in the population
    fitness_scores = [1 / calculate_route_distance(ind) for ind in population]
    total_fitness = sum(fitness_scores)

    # Select parents for the next generation
    parents = random.choices(population, weights=fitness_scores, k=population_size)

    # Create the next generation through crossover and mutation
    new_population = []
    for _ in range(population_size):
        parent1, parent2 = random.sample(parents, 2)
        child = parent1[:]
        for i, city in enumerate(parent2):
            if city not in child:
                child[i] = city
        if random.random() < 0.1:
            mutate(child)
        new_population.append(child)

    population = new_population

# Find the best route in the final population
best_route = min(population, key=lambda ind: calculate_route_distance(ind))
best_distance = calculate_route_distance(best_route)

# Print the best route and distance
print("Best Route:", best_route)
print("Shortest Distance:", best_distance)
