import gym
import algorithm

env = gym.make("CartPole-v1")
env.action_space.seed(42)
env.reset(seed=42)

agent = algorithm.construct_neural_network(env,epochs=1000)
result = agent.test(env, nb_episodes=10, visualize=True)
print(result)
env.close()

