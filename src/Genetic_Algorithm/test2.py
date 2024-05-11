import gym
import numpy as np
import algorithm
import matplotlib.pyplot as plt
import random

random.seed(10)

population1 = [1]
population2 = np.linspace(10,100, num=10).astype(np.int32)
population3 = np.linspace(100, 2000, num=20).astype(np.int32)
population2 = [j for i in [population1, population2] for j in i] 
population = [j for i in [population2, population3] for j in i] 
number_of_trials = 10
results = [0] * len(population)

env = gym.make("CartPole-v1")
env.action_space.seed(42)
env.reset(seed=42)

hp = algorithm.HyperParameters(500, 189, 21, 2, 0.0)

for i in range(len(population)):
    print(i)
    hp.set_hyperparameters(pop_cnt=population[i])
    sum = 0.0
    for _ in range(number_of_trials):
        result, _, _ = algorithm.run(env, hp)
        sum += result
    results[i] = sum / number_of_trials
    hp.reset_algorithm()

print(results)

plt.plot(population, results)
plt.grid()
plt.xlabel('Liczebność populacji')
plt.ylabel('Wynik algorytmu')
plt.show()