import gym
import numpy as np
import algorithm
import matplotlib.pyplot as plt
import random
import time

random.seed(10)

generations = np.linspace(0,500, num=51).astype(np.int32)
number_of_trials = 10
results = [0] * len(generations)
times = [0] * len(generations)

env = gym.make("CartPole-v1")
env.action_space.seed(42)
env.reset(seed=42)

hp = algorithm.HyperParameters(500, 189, 100, 2, 0.0)

for i in range(len(generations)):
    print(i)
    hp.set_hyperparameters(gen_cnt=generations[i])
    sum = 0.0
    for _ in range(number_of_trials):
        start_time = time.time()
        result, _, _ = algorithm.run(env, hp)
        stop_time = time.time()
        elapsed_time = stop_time - start_time
        times[i] += elapsed_time
        sum += result
    times[i] /= number_of_trials
    results[i] = sum / number_of_trials
    hp.reset_algorithm()

print(results)
print(times)

plt.plot(generations, results)
plt.grid()
plt.xlabel('Liczba iteracji')
plt.ylabel('Wynik algorytmu')
plt.show()

plt.plot(generations, times)
plt.grid()
plt.xlabel('Liczba iteracji')
plt.ylabel('Czas działania programu [s]')
plt.show()

