import gym
import algorithm


env2 = gym.make("CartPole-v1")
env2.action_space.seed(42)
env2.reset(seed=42)

hp = algorithm.HyperParameters()
solution = algorithm.run(env2, hp)
print(hp.best_result)
print(hp.best_individual)

env = gym.make("CartPole-v1", render_mode="human")
env.action_space.seed(42)
env.reset(seed=42)

for _ in range(5):
    env.reset(seed=42)
    for step in solution:
        observation, reward, terminated, truncated = env.step(step)

        if terminated or truncated:
            break

env.close()