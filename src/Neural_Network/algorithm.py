import gym

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.optimizers.legacy import Adam

from rl.agents import DQNAgent
from rl.policy import BoltzmannQPolicy
from rl.memory import SequentialMemory

def construct_neural_network(env:gym.Env, layers=2, activation="relu", epochs=10000):
    states = env.observation_space.shape[0]
    actions = env.action_space.n

    model = Sequential()
    model.add(Flatten(input_shape=(1, states)))

    for _ in range(layers):
        model.add(Dense(24, activation=activation))

    model.add(Dense(actions, activation="linear"))

    agent = DQNAgent(
        model = model,
        memory = SequentialMemory(limit=50000, window_length = 1),
        policy = BoltzmannQPolicy(),
        nb_actions = actions,
        nb_steps_warmup = 10,
        target_model_update = 0.01
    )

    agent.compile(Adam(lr=0.001), metrics=["mae"])
    agent.fit(env, nb_steps=epochs, visualize=False, verbose=0)

    return agent
    

