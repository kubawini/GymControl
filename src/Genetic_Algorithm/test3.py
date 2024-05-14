import gym
import numpy as np
import algorithm
import matplotlib.pyplot as plt
import random
import time

random.seed(10)

generations = np.linspace(0,47, num=48).astype(np.int32)
number_of_trials = 10
results = [0] * len(generations)
times = [0] * len(generations)

# env = gym.make("CartPole-v1")
# env.action_space.seed(42)
# env.reset(seed=42)

# hp = algorithm.HyperParameters(500, 189, 100, 2, 0.0)

# for i in range(len(generations)):
#     print(i)
#     hp.set_hyperparameters(gen_cnt=generations[i])
#     sum = 0.0
#     for _ in range(number_of_trials):
#         start_time = time.time()
#         result, _, _ = algorithm.run(env, hp)
#         stop_time = time.time()
#         elapsed_time = stop_time - start_time
#         times[i] += elapsed_time
#         sum += result
#     times[i] /= number_of_trials
#     results[i] = sum / number_of_trials
#     hp.reset_algorithm()

# print(results)
# print(times)

results = [75.0, 139.0, 142.0, 197.0, 222.0, 222.0, 222.0, 222.0, 222.0, 222.0, 223.0,260.0,265.0,276.0,276.0,276.0,276.0,292.0,292.0,307.0,343.0,346.0,369.0,379.0,379.0,392.0,392.0,393.0,394.0,408.0,412.0,436.0,436.0,451.0,452.0,453.0,456.0,459.0,459.0,459.0,474.0,474.0,484.0,494.0,494.0,494.0,497.0,500.0]

plt.plot(generations, results)
plt.grid()
plt.xlabel('Liczba iteracji')
plt.ylabel('Wynik algorytmu')
plt.show()

generations = np.linspace(0,500, num=51).astype(np.int32)
times = [0.08191759586334228, 0.4488193511962891, 0.8658603668212891, 1.3062872409820556, 1.6365981817245483, 2.062968707084656, 2.5954039096832275, 2.9182652711868284, 3.2956525087356567, 3.6093070268630982, 4.1212059497833256, 4.378488445281983, 4.821508049964905, 52.441236233711244, 5.790639019012451, 6.169832229614258, 6.549929237365722, 6.803604936599731, 7.391530203819275, 7.5911383628845215, 7.96315484046936, 8.823724269866943, 8.825568079948425, 10.949522972106934, 9.548493909835816, 9.978113436698914, 31.19572596549988, 10.528497767448425, 10.718588829040527, 11.0137382268905, 11.399067926406861, 11.013598155975341, 12.28177194595337, 11.913173007965089, 12.34157748222351, 12.846982550621032, 13.255335092544556, 14.129859375953675, 15.007797861099244, 14.70343177318573, 14.602487754821777, 15.407421278953553, 15.835548949241637, 16.523716068267824, 16.517084860801695, 16.626456665992738, 16.919294571876527, 17.3491651058197, 17.78481192588806, 18.233921313285826, 18.41005096435547]

plt.plot(generations, times)
plt.grid()
plt.xlabel('Liczba iteracji')
plt.ylabel('Czas działania programu [s]')
plt.show()

