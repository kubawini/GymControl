import gym
import pygame
from gym.utils.play import play
mapping = {(pygame.K_LEFT,): 0, (pygame.K_RIGHT,): 2}
play(gym.make("MountainCar-v0", render_mode="rgb_array"), keys_to_action=mapping)