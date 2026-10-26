import random

# ---------------------------------------
# Game settings
# ---------------------------------------

ACTIONS = ["A", "D", "C", "R"]

POPULATION_SIZE = 10
CHROMOSOME_LENGTH = 6
MUTATION_RATE = 0.1
CROSSOVER_RATE = 0.8
GENERATIONS = 20


# ---------------------------------------
# Fitness function
# ---------------------------------------

def fitness(strategy):
    score = 0

    for action in strategy:

        if action == "A":
            score += 20       # Attack

        elif action == "D":
            score += 10       # Defend

        elif action == "C":
            score += 15       # Chase

        elif action == "R":
            score += 5        # Retreat

    return score


# ---------------------------------------
# Create initial population
# ---------------------------------------

def create_population():

    population = []

    for i in range(POPULATION_SIZE):

        strategy = [
            random.choice(ACTIONS)
            for j in range(CHROMOSOME_LENGTH)
        ]

        population.append(strategy)

    return population


# ---------------------------------------
# Selection
# ---------------------------------------

def selection(population):

    parent1 = random.choice(population)
    parent2 = random.choice(population)

    if fitness(parent1) > fitness(parent2):
        return parent1
    else:
        return parent2


# ---------------------------------------
# Crossover
# ---------------------------------------

def crossover(parent1, parent2):

    if random.random() < CROSSOVER_RATE:

        point = random.randint(1, CHROMOSOME_LENGTH - 1)

        child1 = parent1[:point] + parent2[point:]
        child2 = parent2[:point] + parent1[point:]

        return child1, child2

    return parent1[:], parent2[:]


# ---------------------------------------
# Mutation
# ---------------------------------------

def mutation(strategy):

    for i in range(CHROMOSOME_LENGTH):

        if random.random() < MUTATION_RATE:

            strategy[i] = random.choice(ACTIONS)

    return strategy


# ---------------------------------------
# Genetic Algorithm
# ---------------------------------------

def genetic_algorithm():

    population = create_population()

    best_strategy = None
    best_score = 0

    for generation in range(GENERATIONS):

        # Find best strategy
        for strategy in population:

            score = fitness(strategy)

            if score > best_score:

                best_score = score
                best_strategy = strategy[:]

        print(
            "Generation:",
            generation + 1,
            "Best Strategy:",
            best_strategy,
            "Score:",
            best_score
        )

        # Create new population
        new_population = []

        while len(new_population) < POPULATION_SIZE:

            # Selection
            parent1 = selection(population)
            parent2 = selection(population)

            # Crossover
            child1, child2 = crossover(parent1, parent2)

            # Mutation
            child1 = mutation(child1)
            child2 = mutation(child2)

            new_population.append(child1)

            if len(new_population) < POPULATION_SIZE:
                new_population.append(child2)

        population = new_population

    print("\n----------------------------")
    print("FINAL RESULT")
    print("----------------------------")

    print("Best NPC Strategy:", best_strategy)
    print("Best Score:", best_score)


# ---------------------------------------
# Run the program
# ---------------------------------------

genetic_algorithm()
