import gym
import numpy as np
import algorithm
import matplotlib.pyplot as plt
import random

# random.seed(10)

layers = np.linspace(1,10, num=10).astype(np.int32)
# number_of_trials = 10
# results = [0] * len(layers)

# env = gym.make("CartPole-v1")
# env.action_space.seed(42)
# env.reset(seed=42)

# for i in range(len(layers)):
#     print('i: ' + str(i))
#     sum = 0.0
#     env.reset(seed=42)
#     agent = algorithm.construct_neural_network(env,layers=layers[i],epochs=10000)
#     result = agent.test(env, nb_episodes=10, visualize=False)

# print(results)


results = [350.4, 266, 226.1, 244, 142.9, 200.4, 161.3, 159.2, 243, 109.8]
plt.plot(layers, results)
plt.grid()
plt.xlabel('Liczba warstw')
plt.ylabel('Wynik algorytmu')
plt.show()