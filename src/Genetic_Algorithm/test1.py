import gym
import numpy as np
import algorithm
import matplotlib.pyplot as plt
import random

random.seed(10)

probabilities = np.linspace(0,1, num=21)
number_of_trials = 10
results = [0] * 21

env = gym.make("CartPole-v1")
env.action_space.seed(42)
env.reset(seed=42)

hp = algorithm.HyperParameters(500, 189, 21, 2, 0.0)

for i in range(len(probabilities)):
    hp.set_hyperparameters(pr_mut=probabilities[i])
    sum = 0.0
    for _ in range(number_of_trials):
        result, _, _ = algorithm.run(env, hp)
        sum += result
    results[i] = sum / number_of_trials
    hp.reset_algorithm()

print(results)

plt.plot(probabilities, results)
plt.grid()
plt.xlabel('Prawdopodobieństwo mutacji')
plt.ylabel('Wynik algorytmu')
plt.show()