import gym
import numpy as np
import algorithm
import matplotlib.pyplot as plt
import random
import time

random.seed(10)

simulation1 = np.linspace(10, 100, num=10).astype(np.int32)
simulation2 = np.linspace(200, 1000, num=9).astype(np.int32)
simulation3 = np.linspace(2000, 10000, num=9).astype(np.int32)
simulation2 = [j for i in [simulation1, simulation2] for j in i]
simulation = [j for i in [simulation2, simulation3] for j in i]
# number_of_trials = 50
results = [0] * len(simulation)
times = [0] * len(simulation)

# env = gym.make("CartPole-v1")
# env.action_space.seed(42)
# env.reset(seed=42)

# for i in range(len(simulation)):
#     sum = 0.0
#     for j in range(number_of_trials):
#         env.reset(seed=j)
#         solution = list()
#         start_time = time.time()
#         root = algorithm.MonteCarloTreeSearchNode(state = algorithm.State(env, False, False), tree_depth=100, simulation_no=simulation[i])
#         while not root.is_terminal_node() and len(solution) < 500:
#             selected_node = root.best_action()
#             solution.append(selected_node.parent_action)
#             root = selected_node
#         sum += len(solution)
#         end_time = time.time()
#         times[i] += end_time - start_time
#     results[i] = sum/number_of_trials
#     times[i] = times[i]/number_of_trials
#     print('i: ' + str(i) + ', ' + str(results[i]) + ', ' + str(times[i]))
    
results = [170.32, 172.08, 172.94, 174.92, 176.22, 176.68, 175.62, 177.5, 177.68,177.62, 179.8, 181.86,180.88,182.3, 183.64,183.46,184.48,183.4,182.9, 188.44,187.94,190.84,190.66,194.12,190.42,193.14,192.34, 195.42]
times = [ 3.5283501148223877, 3.760780386924744, 3.6209131574630735, 3.6814473724365233, 3.811529154777527,
 4.032632656097412, 3.9506906986236574, 3.980328850746155, 3.9740135574340822, 4.017467136383057, 4.299029788970947,
  4.562169990539551, 4.802239737510681, 5.018304357528686, 5.287590298652649, 5.5024704217910765, 6.201689004898071,
 7.57303023815155, 7.76596474647522, 8.640900959968567, 10.087054233551026, 12.949030814170838, 14.456000332832337,
  17.10669235229492, 19.05525074481964, 21.236824922561645, 23.251806635856628, 25.73065507888794]

print(results)
print(times)

plt.plot(simulation, results)
plt.grid()
plt.xlabel('Liczba symulacji')
plt.ylabel('Wynik algorytmu')
plt.show()

plt.plot(simulation, times)
plt.grid()
plt.xlabel('Liczba symulacji')
plt.ylabel('Czas działania programu [s]')
plt.show()

