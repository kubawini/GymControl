import gym
import numpy as np
import algorithm
import matplotlib.pyplot as plt
import random
import time

random.seed(10)

population1 = [1]
population2 = np.linspace(10,100, num=10).astype(np.int32)
population3 = np.linspace(100, 2000, num=20).astype(np.int32)
population2 = [j for i in [population1, population2] for j in i] 
population = [j for i in [population2, population3] for j in i] 
number_of_trials = 50
results = [0] * len(population)
times = [0] * len(population)

# env = gym.make("CartPole-v1")
# env.action_space.seed(42)
# env.reset(seed=42)

# hp = algorithm.HyperParameters(500, 189, 21, 2, 0.0)

# for i in range(len(population)):
#     print(i)
#     hp.set_hyperparameters(pop_cnt=population[i])
#     sum = 0.0
#     for _ in range(number_of_trials):
#         start_time = time.time()
#         result, _, _ = algorithm.run(env, hp)
#         end_time = time.time()
#         sum += result
#         times[i] += end_time - start_time
#     results[i] = sum / number_of_trials
#     times[i] = times[i] / number_of_trials
#     hp.reset_algorithm()

# print(results)
# print(times)

results = [70.74, 77.46, 84.78, 96.7, 118.9, 98.46, 88.54, 89.8, 83.24, 82.5, 107.88, 93.04, 90.7, 111.34, 118.0, 145.96, 116.22, 123.36, 143.36, 141.0, 125.9, 139.44, 139.3, 171.32, 139.06, 137.84, 135.18, 137.04, 142.14, 144.16, 157.02]
times = [0.013407769203186036, 0.06123110771179199, 0.10611135482788087, 0.15142224311828614, 0.19973655700683593, 0.24562602519989013, 0.28960419178009034, 0.3544171667098999, 0.39194491386413577, 0.4479374885559082, 0.5153046894073486, 0.4837239122390747, 0.9841308832168579, 1.4719334602355958, 1.913467288017273, 2.3923243379592893, 2.829105567932129, 3.3623940181732177, 3.983450140953064, 4.145345268249512, 4.387325434684754, 5.168565192222594, 5.519268665313721, 5.936754860877991, 6.577352185249328, 7.065021481513977, 7.40872862815857, 7.917231612205505, 8.49653947353363, 8.734565858840943, 9.714995698928833]

plt.plot(population, results)
plt.grid()
plt.xlabel('Liczebność populacji')
plt.ylabel('Wynik algorytmu')
plt.show()

plt.plot(population, times)
plt.grid()
plt.xlabel('Liczebność populacji')
plt.ylabel('Czas działania programu [s]')
plt.show()