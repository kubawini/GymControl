import gym
import algorithm


env2 = gym.make("CartPole-v1")
env2.action_space.seed(42)
env2.reset(seed=42)
_, solution = algorithm.run(env2)
print(algorithm.best_result)
print(algorithm.best_individual)

env = gym.make("CartPole-v1", render_mode="human")
env.action_space.seed(42)
observation, info = env.reset(seed=42)

for _ in range(5):
    env.reset(seed=42)
    for step in solution:
        observation, reward, terminated, truncated, info = env.step(step)

        if terminated or truncated:
            break

env.close()