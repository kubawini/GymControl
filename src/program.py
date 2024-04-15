import gym

env = gym.make("Acrobot-v1", render_mode="human")
env.action_space.seed(42)

observation, info = env.reset(seed=42)

for _ in range(1000):
    step = env.action_space.sample()
    observation, reward, terminated, truncated, info = env.step(step)

    if terminated or truncated:
        observation, info = env.reset()

env.close()