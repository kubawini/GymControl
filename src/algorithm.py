import gym
import random

# Hyper parameters
simulation_steps = 500
population_count = 200
crossing_population_count = int(population_count + population_count/10*4)
number_of_pairs = int(4 * population_count / 10)
tournament_population = 20
generation_count = 100
space_dimension = 2
max_probability_of_mutation = 0.7
best_individual = None
best_result = 0




### MAIN FUNCTION ###
def run(env:gym.Env) -> list:
    population = initialize_population(population_count)
    for _ in range(generation_count):
        selection(population)
        crossing(population, env)
        mutation(population)
    result = best_result
    moves = best_individual.copy()
    return result, moves



### Main components ###
def initialize_population(count:int):
    population = list()
    for _ in range(population_count):
        single = list()
        for _ in range(simulation_steps):
            decision = random.randint(0,space_dimension-1)
            single.append(decision)
        population.append(single)
    return population

# TODO Random selection - maybe upgrade to proportional selection?
def selection(population:list):
    for _ in range(crossing_population_count - population_count):
        index = random.randint(0, population_count - 1)
        new_individual = population[index].copy()
        population.append(new_individual)
    return population # TODO I think it's useless


def crossing(population:list, env:gym.Env):
    for i in range(number_of_pairs):
        indexes_of_competitors1 = list()
        indexes_of_competitors2 = list()
        set_tournament_indexes(tournament_population,crossing_population_count - i,
                           indexes_of_competitors1,indexes_of_competitors2)
        parent1_index, parent2_index = get_two_winners(indexes_of_competitors1,indexes_of_competitors2, population, env)
        cross(parent1_index,parent2_index,population)
    return population # TODO this line is actually not needed
    

def mutation(population:list):
    for individual in population:
        for i in range(len(individual)):
            if random.random() < max_probability_of_mutation * (min(1, 100 * i/best_result)):
                if individual[i] == 0:
                    individual[i] = 1
                else:
                    individual[i] = 0
    return population # TODO Do I really need this?


def count_target_function(individual:list, env:gym.Env):
    sum = 0
    for i in range(simulation_steps):
        step = individual[i]
        observation, reward, terminated, truncated, _ = env.step(step)
        sum += reward
        if terminated or truncated:
            break
    env.reset(seed=42)
    global best_result
    global best_individual
    if sum > best_result:
        best_individual = individual.copy()
        best_result = sum
        print(best_result)
    return sum




# Configuration #
def reset_algorithm():
    global best_individual, best_result
    best_individual = None
    best_result = 0

def set_hyperparameters(sim_st=None, pop_cnt=None, cr_pop_cnt=None,
                        nr_p=None, t_pop=None, gen_cnt=None, sp_dim=None, pr_mut=None):
    global simulation_steps, population_count, crossing_population_count, number_of_pairs
    global tournament_population, generation_count, space_dimension, max_probability_of_mutation
    if not sim_st == None:
        simulation_steps = sim_st
    if not pop_cnt == None:
        population_count = pop_cnt
    if not cr_pop_cnt == None:
        crossing_population_count = cr_pop_cnt
    if not nr_p == None:
        number_of_pairs = nr_p
    if not t_pop == None:
        tournament_population = t_pop
    if not gen_cnt == None:
        generation_count = gen_cnt
    if not sp_dim == None:
        space_dimension = sp_dim
    if not pr_mut == None:
        max_probability_of_mutation = pr_mut




# Rest of functions #  
def get_two_winners(indexes_of_competitors1:list, indexes_of_competitors2:list, population:list, env:gym.Env):
    competitor1 = indexes_of_competitors1[0]
    max_function1 = count_target_function(population[competitor1], env)
    competitor2 = indexes_of_competitors2[0]        
    max_function2 = count_target_function(population[competitor2], env)
    for index in indexes_of_competitors1:
        index_target_function = count_target_function(population[index], env)
        if (index_target_function > max_function1):
            competitor1 = index
            max_function1 = index_target_function
    for index in indexes_of_competitors2:
        index_target_function = count_target_function(population[index], env)
        if (index_target_function > max_function2):
            competitor2 = index
            max_function2 = index_target_function
    return competitor1, competitor2


def cross(parent1_index:int, parent2_index:int, population:list):
    if parent1_index != parent2_index:
        if parent1_index > parent2_index:
            parent1_index, parent2_index = parent2_index, parent1_index
        child = natural_crossing(parent1_index, parent2_index, population)
        population.pop(parent2_index)
        population.pop(parent1_index)
        population.append(child)
    else:
        population.pop(parent1_index) # TODO This makes no sense to delete the best parent


def natural_crossing(parent1_index:int, parent2_index:int, population:list):
    parent1:list = population[parent1_index]
    parent2:list = population[parent2_index]
    child = list()
    for i in range(simulation_steps):
        winning_chromosome = random.randint(0,space_dimension - 1)
        if winning_chromosome == 0:
            child.append(parent1[i])
        else:
            child.append(parent2[i])
    return child


def generate_random_index(crossing_population_count:int):
    index = random.randint(0,crossing_population_count - 1)
    return index
    

def set_tournament_index(crossing_population_count:int,indexes_of_competitors:list):
    indexes_of_competitors.append(generate_random_index(crossing_population_count))


def set_tournament_indexes(tournament_population:int,crossing_population_count:int,
                           indexes_of_competitors1:list,indexes_of_competitors2:list):
    for i in range(tournament_population):
        set_tournament_index(crossing_population_count, indexes_of_competitors1)
        set_tournament_index(crossing_population_count, indexes_of_competitors2)