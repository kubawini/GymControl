import numpy as np
from collections import defaultdict
import gym
import copy


class MonteCarloTreeSearchNode():
    def __init__(self, state, parent=None, parent_action=None, tree_depth=5, simulation_no=10):
        self.state = state
        self.parent = parent
        self.parent_action = parent_action
        self.children = []
        self._number_of_visits = 0
        self._results = defaultdict(int)
        self._results[1] = 0
        self._results[-1] = 0
        self._untried_actions = None
        self._untried_actions = self.untried_actions()
        self.tree_depth = tree_depth
        self.simulation_no = simulation_no
        return
    
    def untried_actions(self):
        self._untried_actions = self.state.get_legal_actions()
        return self._untried_actions
    
    def q(self):
        wins = self._results[1]
        loses = self._results[-1]
        return wins - loses
    
    def n(self):
        return self._number_of_visits
    
    def expand(self):	
        action = self._untried_actions.pop()
        next_state = self.state.move(action) # IMPORTANTE
        child_node = MonteCarloTreeSearchNode(next_state, parent=self, parent_action=action)
        self.children.append(child_node)
        return child_node 
    
    def is_terminal_node(self):
        return self.state.is_game_over() # IMPORTANTE
    
    def rollout(self):
        current_rollout_state = self.state
        i = 0
        while not current_rollout_state.is_game_over() and i < self.tree_depth:
            possible_moves = current_rollout_state.get_legal_actions()
            action = self.rollout_policy(possible_moves)
            current_rollout_state = current_rollout_state.move(action)
            i += 1
        return current_rollout_state.game_result()
    
    def backpropagate(self, result):
        self._number_of_visits += 1.
        self._results[result] += 1.
        if self.parent:
            self.parent.backpropagate(result)

    def is_fully_expanded(self):
        return len(self._untried_actions) == 0
    
    def best_child(self, c_param=0.1):  
        choices_weights = [(c.q() / c.n()) + c_param * np.sqrt((2 * np.log(self.n()) / c.n())) for c in self.children]
        return self.children[np.argmax(choices_weights)]
    
    def rollout_policy(self, possible_moves):
        return possible_moves[np.random.randint(len(possible_moves))]
    
    def _tree_policy(self):
        current_node = self
        i = 0
        while not current_node.is_terminal_node() and i < self.tree_depth:
            if not current_node.is_fully_expanded():
                return current_node.expand()
            else:
                current_node = current_node.best_child()
            i += 1
        return current_node
    
    def best_action(self):
        for i in range(self.simulation_no):
            v = self._tree_policy()
            reward = v.rollout()
            v.backpropagate(reward)
        return self.best_child(c_param=0.)
    

class State():
    
    def __init__(self, env:gym.Env, terminated:bool, truncated:bool):
        self._env = env
        self._terminated = terminated
        self._truncated = truncated
        return

    def get_legal_actions(self): 
        return list([0, 1])

    def is_game_over(self):
        if self._terminated or self._truncated:
            return True
        return False

    def game_result(self):
        if self.is_game_over():
            return -1
        return 1

    def move(self,action):
        new_env = copy.deepcopy(self._env)
        observation, reward, terminated, truncated = new_env.step(action)
        next_state = State(new_env, terminated, truncated)
        return next_state
