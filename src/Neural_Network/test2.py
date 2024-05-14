import gym
import numpy as np
import algorithm
import matplotlib.pyplot as plt
import random

random.seed(10)

epochs = np.linspace(5000,100000, num=20)
# number_of_trials = 50
# results = [0] * len(epochs)

# env = gym.make("CartPole-v1")
# env.action_space.seed(42)
# env.reset(seed=42)

# for i in range(len(epochs)):
#     print('i: ' + str(i))
#     sum = 0.0
#     env.reset(seed=42)
#     agent = algorithm.construct_neural_network(env,epochs=epochs[i])
#     result = agent.test(env, nb_episodes=number_of_trials, visualize=True)

# print(results)


results = [380.28,243.6,192.14,251.6,245.98,288.2,180.58,241.46,263.1,253.84,500,500,500,494.14,461.44,500,500,500,500,500]
plt.plot(epochs, results)
plt.grid()
plt.xlabel('Liczba epok')
plt.ylabel('Wynik algorytmu')
plt.show()