import gym
import random

import numpy as np

# Hyper parameters
class HyperParameters:
    def __init__(self, sim_st=500, pop_cnt=200, gen_cnt=1000, sp_dim=2, pr_mut=1):
        self.simulation_steps = sim_st
        self.population_count = pop_cnt
        self.generation_count = gen_cnt
        self.space_dimension = sp_dim
        self.probability_of_mutation = pr_mut
        self.best_individual = None
        self.best_result = 0
        self.best_result_index = -1

    def set_hyperparameters(self, sim_st=None, pop_cnt=None, gen_cnt=None, sp_dim=None, pr_mut=None):
        if not sim_st == None:
            self.simulation_steps = sim_st
        if not pop_cnt == None:
            self.population_count = pop_cnt
        if not gen_cnt == None:
            self.generation_count = gen_cnt
        if not sp_dim == None:
            self.space_dimension = sp_dim
        if not pr_mut == None:
            self.probability_of_mutation = pr_mut

    def reset_algorithm(self):
        self.best_individual = None
        self.best_result = 0

import gym

def test(hp:HyperParameters):
    env2 = gym.make("CartPole-v1")
    env2.action_space.seed(42)
    env2.reset(seed=42)
    _, solution = run(env2)
    print(hp.best_result)
    print(hp.best_individual)

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
def run(env:gym.Env, hp:HyperParameters) -> list:
    population = initialize_population(hp.population_count, hp)
    scores = [0] * len(population)
    count_scores(population, scores, env, hp)
    save_best(population, scores, hp)
    iterations = 0
    for i in range(hp.generation_count):
        mutation(population,scores, env, hp)
        count_scores(population, scores, env, hp)
        save_best(population, scores, hp)
        if int(hp.best_result) >= 500:
            iterations = i
            break
    result = hp.best_result
    moves = hp.best_individual.copy()
    return result, moves, iterations



### Main components ###
def initialize_population(count:int, hp:HyperParameters):
    population = list()
    for _ in range(hp.population_count):
        single = list()
        for _ in range(hp.simulation_steps):
            decision = random.randint(0,hp.space_dimension-1)
            single.append(decision)
        population.append(single)
    return population

def mutation(population:list, scores:list, env:gym.Env, hp:HyperParameters):
    for i in range(len(population)):
            individual_target_function = max(0, scores[i] - 10)
            individual = population[i]
            for j in range(len(individual)):
                rand = random.random()
                if j >= individual_target_function:
                    fulfill_random(individual, j, hp)
                    break

def fulfill_random(individual:list, index:int, hp:HyperParameters):
    for i in range(index, hp.simulation_steps):
        if(random.random() < hp.probability_of_mutation):
            individual[i] = random.randint(0,1)

def count_score(individual:list, env:gym.Env, hp:HyperParameters):
    sum = 0
    for i in range(hp.simulation_steps):
        step = individual[i]
        _, reward, terminated, truncated = env.step(step)
        sum += reward
        if terminated or truncated:
            break
    env.reset(seed=42)
    return sum


def count_scores(population:list, scores:list, env:gym.Env, hp:HyperParameters):
    for i in range(len(population)):
        scores[i] = count_score(population[i], env, hp)

def save_best(population:list, scores:list, hp:HyperParameters):
    best_population_score = max(scores)
    best_population_index = scores.index(best_population_score)
    if best_population_score > hp.best_result:
        hp.best_result_index = best_population_index
        hp.best_result = best_population_score
        hp.best_individual = population[best_population_index].copy()
    population[0] = hp.best_individual.copy()
    scores[0] = hp.best_result
    hp.best_result_index = 0



# test()