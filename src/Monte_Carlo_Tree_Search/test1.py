import gym
import numpy as np
import algorithm
import matplotlib.pyplot as plt
import random
import time

random.seed(10)

depths1 = np.linspace(1,9, num=9).astype(np.int32)
depths2 = np.linspace(10,100, num=10).astype(np.int32)
depths = [j for i in [depths1, depths2] for j in i]
number_of_trials = 50
results = [0] * len(depths)
times = [0] * len(depths)

env = gym.make("CartPole-v1")
env.action_space.seed(42)
env.reset(seed=42)

for i in range(len(depths)):
    sum = 0.0
    for j in range(number_of_trials):
        env.reset(seed=j)
        solution = list()
        start_time = time.time()
        root = algorithm.MonteCarloTreeSearchNode(state = algorithm.State(env, False, False), tree_depth=depths[i], simulation_no=2000)
        while not root.is_terminal_node() and len(solution) < 500:
            selected_node = root.best_action()
            solution.append(selected_node.parent_action)
            root = selected_node
        sum += len(solution)
        end_time = time.time()
        times[i] += end_time - start_time
    results[i] = sum/number_of_trials
    times[i] = times[i]/number_of_trials
    print('i: ' + str(i) + ', ' + str(results[i]) + ', ' + str(times[i]))
    

print(results)
print(times)

results = [170.14, 170.76, 170.0, 171.7, 173.48, 178.18, 178.68, 177.0, 178.76, 181.24, 187.06, 190.48, 185.12, 190.14, 186.0, 188.36, 188.68, 190.04, 187.6]
times = [6.6599882698059085, 6.664900107383728, 6.961694746017456, 6.9269925260543825, 6.37870726108551, 6.5481809759140015, 6.559151363372803, 6.509928331375122, 6.578293542861939, 6.67396957397461, 7.494065337181091, 7.496777925491333, 7.417356686592102, 7.475402402877807, 7.365702180862427, 7.4485310411453245, 7.441473937034607, 7.543283414840698, 7.422849912643432]

plt.plot(depths, results)
plt.grid()
plt.xlabel('Głębokość drzewa')
plt.ylabel('Wynik algorytmu')
plt.show()

plt.plot(depths, times)
plt.grid()
plt.xlabel('Głębokość drzewa')
plt.ylabel('Czas działania programu [s]')
plt.show()

