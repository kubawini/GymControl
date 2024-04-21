import algorithm as alg
import gym

env = gym.make("CartPole-v1")
env.action_space.seed(42)
env.reset(seed=42)

solution = list()
root = alg.MonteCarloTreeSearchNode(state = alg.State(env, False, False))
while not root.is_terminal_node() and len(solution) < 500:
    selected_node = root.best_action()
    solution.append(selected_node.parent_action)
    root = selected_node

print("Solution length: " + str(len(solution)) + ", solution: " + str(solution))

env = gym.make("CartPole-v1", render_mode="human")
env.action_space.seed(42)
env.reset(seed=42)
i=0

for step in solution:
    observation, reward, terminated, truncated = env.step(step)
    i += 1
    if terminated or truncated:
        break

print('result: ' + str(i))
env.close()