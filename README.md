# GymControl

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
Genetic algorithm has been implemented following the given scheme

```python
def run(env:gym.Env, hp:HyperParameters) -> list:
    population = initialize_population(hp.population_count, hp)
    scores = [0] * len(population)
    count_scores(population, scores, env, hp)
    save_best(population, scores, hp)
    iterations = 0
    for i in range(hp.generation_count):
        mutation(population,scores, env, hp)
        count_scores(population, scores, env, hp)
        save_best(population, scores, hp)
        if int(hp.best_result) >= 500:
            iterations = i
            break
    result = hp.best_result
    moves = hp.best_individual.copy()
    return result, moves, iterations
```



## Prerequsities
In order to run Python scrypts, you haave to download the packages in following versions:
1. tensorflow: 2.12.0
2. gym: 0.25.2
3. keras-rl2: 1.0.5

You can do this in Windows using single command

```bash
pip install tensorflow==2.12.0 gym==0.25.2 keras-rl2==1.0.5
```
