import algorithm
import random
import gym

number_of_iterations = 10
min_population_count = 1
max_population_count = 200
min_crossing_population_count = 1
max_crossing_population_count = 400
min_generation_count = 1
max_generation_count = 200
min_probability_of_mutation = 0.0
max_probability_of_mutation = 1.0
simulation_steps = algorithm.simulation_steps
space_dimension = algorithm.space_dimension

best_simulation_steps = None
best_population_count = None
best_crossing_population_count = None
best_number_of_pairs = None
best_tournament_population = None
best_generation_count = None
best_space_dimension = None
best_probability_of_mutation = None
best_result = -1

def optimize(env:gym.Env):
    for _ in range(number_of_iterations):
        population_count = random.randint(min_population_count, max_population_count)
        crossing_population_count = random.randint(min_crossing_population_count, max_crossing_population_count)
        number_of_pairs = random.randint(0, int(crossing_population_count/2))
        tournament_population = random.randint(0, crossing_population_count)
        generation_count = random.randint(min_generation_count, max_generation_count)
        probability_of_mutation = random.random()
        algorithm.set_hyperparameters(simulation_steps, population_count, crossing_population_count,
                                      number_of_pairs, tournament_population, generation_count,
                                      space_dimension, probability_of_mutation)
        algorithm.reset_algorithm()
        result, _ = algorithm.run(env)
        if result > best_result:
            set_best_parameters(simulation_steps, population_count, crossing_population_count,
                                number_of_pairs, tournament_population, generation_count,
                                space_dimension, probability_of_mutation, best_result)
    print_parameters()



def set_best_parameters(simulation_steps, population_count, crossing_population_count,
                        number_of_pairs, tournament_population, generation_count,
                        space_dimension, probability_of_mutation, result):
    global best_simulation_steps
    global best_population_count
    global best_crossing_population_count
    global best_number_of_pairs
    global best_tournament_population
    global best_generation_count
    global best_space_dimension
    global best_probability_of_mutation
    global best_result
    best_simulation_steps = simulation_steps
    best_population_count = population_count
    best_crossing_population_count = crossing_population_count
    best_number_of_pairs = number_of_pairs
    best_tournament_population = tournament_population
    best_generation_count = generation_count
    best_space_dimension = space_dimension
    best_probability_of_mutation = probability_of_mutation
    best_result = result

def print_parameters():
    print('Best parameters:')
    print('simulation_steps = ' + str(best_simulation_steps))
    print('population_count = ' + str(best_population_count))
    print('crossing_population_count = ' + str(best_crossing_population_count))
    print('number_of_pairs = ' + str(best_number_of_pairs))
    print('tournament_population = ' + str(best_tournament_population))
    print('generation_count = ' + str(best_generation_count))
    print('space_dimension = ' + str(best_space_dimension))
    print('probability_of_mutation = ' + str(best_probability_of_mutation))


# run
env = gym.make("CartPole-v1")
env.action_space.seed(42)
env.reset(seed=42)
optimize(env)
