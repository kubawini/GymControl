import gym
import random

import numpy as np

# Hyper parameters
simulation_steps = 500
population_count = 200
crossing_population_count = int(population_count - population_count/10*4)
number_of_pairs = int(4 * population_count / 10)
tournament_population = 20
generation_count = 1000
space_dimension = 2
max_probability_of_mutation = 0.7
best_individual = None
best_result = 0
best_result_index = -1

import gym

def test():
    env2 = gym.make("CartPole-v1")
    env2.action_space.seed(42)
    env2.reset(seed=42)
    _, solution = run(env2)
    print(best_result)
    print(best_individual)

    env = gym.make("CartPole-v1", render_mode="human")
    env.action_space.seed(42)
    env.reset(seed=42)

    for _ in range(5):
        env.reset(seed=42)
        for step in solution:
            observation, reward, terminated, truncated = env.step(step)

            if terminated or truncated:
                break

    env.close()



### MAIN FUNCTION ###
def run(env:gym.Env) -> list:
    population = initialize_population(population_count)
    scores = [0] * len(population)
    count_scores(population, scores, env)
    save_best(population, scores)
    for i in range(generation_count):
        print('i: ' + str(i))
        mutation(population,scores, env)
        count_scores(population, scores, env)
        save_best(population, scores)
        global best_result
        print(f'{int(best_result)}')
        if int(best_result) >= 500:
            break
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

def mutation(population:list, scores:list, env:gym.Env):
    global best_result_index
    for i in range(len(population)):
        # if i == best_result_index:
        #     print(f'Skipping bes result {best_result_index}')
        #     print(scores[best_result_index])
        # else:
            individual_target_function = max(0, scores[i] - 10)
            individual = population[i]
            for j in range(len(individual)):
                rand = random.random()
                if j >= individual_target_function:
                    fulfill_random(individual, j)
                    break

def fulfill_random(individual:list, index:int):
    for i in range(index, simulation_steps):
        individual[i] = random.randint(0,1)

def count_score(individual:list, env:gym.Env):
    sum = 0
    for i in range(simulation_steps):
        step = individual[i]
        _, reward, terminated, truncated = env.step(step)
        sum += reward
        if terminated or truncated:
            break
    env.reset(seed=42)
    return sum


def count_scores(population:list, scores:list, env:gym.Env):
    for i in range(len(population)):
        scores[i] = count_score(population[i], env)

def save_best(population:list, scores:list):
    best_population_score = max(scores)
    best_population_index = scores.index(best_population_score)
    global best_result
    global best_individual
    global best_result_index
    print(f'Best in population {best_population_score}')
    if best_population_score > best_result:
        best_result_index = best_population_index
        best_result = best_population_score
        best_individual = population[best_population_index].copy()
    population[0] = best_individual.copy()
    scores[0] = best_result
    best_result_index = 0
    print(f'Best result: {best_result}')


test()