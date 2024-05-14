import gym
import numpy as np
import algorithm
import matplotlib.pyplot as plt
import random

random.seed(10)

activations = ['relu', 'sigmoid', 'softmax', 'tanh', 'gelu']
# number_of_trials = 20
# results = [0] * len(activations)

# env = gym.make("CartPole-v1")
# env.action_space.seed(42)
# env.reset(seed=42)

# for i in range(len(activations)):
#     print('i: ' + str(i))
#     sum = 0.0
#     env.reset(seed=42)
#     agent = algorithm.construct_neural_network(env,activation=activations[i])
#     result = agent.test(env, nb_episodes=number_of_trials, visualize=True)

# print(results)
results = [193.5, 189.6, 9.2, 196, 288.3]

plt.bar(activations, results)
plt.xlabel('Funkcja aktywacji')
plt.ylabel('Wynik algorytmu')
plt.show()