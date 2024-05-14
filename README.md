# GymControl

## Prerequsities
In order to run Python scrypts, you haave to download the packages in following versions:
1. tensorflow: 2.12.0
2. gym: 0.25.2
3. keras-rl2: 1.0.5

You can do this in Windows using single command

```bash
pip install tensorflow==2.12.0 gym==0.25.2 keras-rl2==1.0.5
```

## About project

This is a project for Introduction to Evolutionary Algorithms (faculty of Mathematics and Information Science). Program solves gym library task Cart Pole, located under the <a href="https://www.gymlibrary.dev/environments/classic_control/cart_pole/"> link</a>. Problem is solved using three algorithms: evolutionary algorithm, neural network and Monte Carlo Tree Search. The aim of the problem is to balance the pole by moving cart left or right. Formally, there is given a space of actions one can take.

| Number | Action |
| ------ | ------ |
| 0      | Move the cart left |
| 1      | Move the cart right |

You can take these actions based on observation space elements.

| Number | Observation | Min | Max |
| ------ | ----------- | --- | --- |
| 0 | Cart position | $`-4.8`$ | $`4.8`$ |
| 1 | Cart velocity | $`-\infty`$ | $`\infty`$ |
| 2 | Pole angle | $`-0.418`$ | $`0.418`$ |
| 3 | Pole angular velocity | $`\-infty`$ | $`\infty`$ |

Moreover, there is given a reward/penalty system which gives you 1 for every fram when pole doesn't fall and 0 for the moment when pole falls.

Below there is an example of what a simulation looks like.

![image](https://github.com/kubawini/GymControl/assets/93740269/5cf2a348-d903-4eca-8091-2b5d63ae6651)

## Genetic algorithm
Genetic algorithm has been implemented following the given scheme (it's just the scheme - full implementation can be viewed in /src/Genetic_Algorith/algorithm.py file).

```python
def run(env:gym.Env, hp:HyperParameters) -> list:
    population = initialize_population(hp.population_count, hp)
    for i in range(hp.generation_count):
        mutation(population, env, hp)
        count_scores(population, env, hp)
        save_best(population, hp)
        if int(env.terminated):
            break
    moves = hp.best_individual.copy()
    return moves
```

In summary it returns a list of 0s and 1s which correspond to moves that a cart is supposed to make. The algorithm involves only mutation - no crossing or selection. In each step, the best solution is preserved. Only last 10 steps before terminating and all steps after the pole falls can be modified. Turns out that this simple scheme gives quite good results as steps that occur at first stages become later irrelevant.

The algorithm with default parameters reaches maximum number of simulation steps (500) in about 40 on average iterations which is considered to be quite a good result.

![test3](https://github.com/kubawini/GymControl/assets/93740269/fa7ceea9-d33d-448d-b74f-c42f67bdcc10)

## Neural Network
Neural Network is constructed with two layers containing 24 neurons each with $`\textit{relu}`$ activation function. The network makes decisions based on the observation space. The Deep Q-Network Agent (DQNAgent) with the Adam optimiser was used to train the network. The performance of the network was investigated for different number of training epochs.

![test7](https://github.com/kubawini/GymControl/assets/93740269/07433813-f6cc-4c1b-b407-26417e4ae555)

Turns out, that neural network returns optimal solution after about 50000 epochs (several minutes of training). Moreover, the moves made by cart seem to be much more intelligent than those returned by genetic algorithm.

## Monte Carlo Tree Search
Monte Carlo Tree Search has been implemented according to instructions listed under following <a href="https://ai-boson.github.io/mcts/"> link</a> and adapted to Cart Pole requirements. The algorithm turned out to be the worst of all, not managing to overcome the barrier of 200 steps in reasonable time.

![test11](https://github.com/kubawini/GymControl/assets/93740269/25cd26d8-51e0-4b1d-916a-24006dd9c6cd)
