import algorithm
import random
import gym

number_of_iterations = 50
number_of_repetitions = 10
min_population_count = 1
max_population_count = 200
min_generation_count = 20
max_generation_count = 21
min_probability_of_mutation = 0.0
max_probability_of_mutation = 1.0
simulation_steps = 500
space_dimension = 2

best_simulation_steps = None
best_population_count = None
best_generation_count = None
best_space_dimension = None
best_probability_of_mutation = None
best_result = -1

def optimize(env:gym.Env):
    random.seed(10)
    for _ in range(number_of_iterations):
        result = 0.0
        population_count = random.randint(min_population_count, max_population_count)
        generation_count = random.randint(min_generation_count, max_generation_count)
        probability_of_mutation = random.random()
        hp = algorithm.HyperParameters(simulation_steps, population_count, generation_count,
                                        space_dimension, probability_of_mutation)
        for _ in range(number_of_repetitions):
            res, _ = algorithm.run(env, hp)
            result += res
            hp.reset_algorithm()
        if result/number_of_repetitions > best_result:
            set_best_parameters(simulation_steps, population_count, generation_count,
                                    space_dimension, probability_of_mutation, result/number_of_repetitions)
    print_parameters()



def set_best_parameters(simulation_steps, population_count, generation_count,
                        space_dimension, probability_of_mutation, result):
    global best_simulation_steps
    global best_population_count
    global best_generation_count
    global best_space_dimension
    global best_probability_of_mutation
    global best_result
    best_simulation_steps = simulation_steps
    best_population_count = population_count
    best_generation_count = generation_count
    best_space_dimension = space_dimension
    best_probability_of_mutation = probability_of_mutation
    best_result = result

def print_parameters():
    print('Best parameters:')
    print('simulation_steps = ' + str(best_simulation_steps))
    print('population_count = ' + str(best_population_count))
    print('generation_count = ' + str(best_generation_count))
    print('space_dimension = ' + str(best_space_dimension))
    print('probability_of_mutation = ' + str(best_probability_of_mutation))
    print('best_result = ' + str(best_result))


# run
env = gym.make("CartPole-v1")
env.action_space.seed(42)
env.reset(seed=42)
optimize(env)
