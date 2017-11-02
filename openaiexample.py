import gym
import random
import numpy as np
import tflearn


# In[2]:

from tflearn.layers.core import input_data, dropout, fully_connected


# In[3]:

from tflearn.layers.estimator import regression
from statistics import mean, median
from collections import Counter

LR = 1e-3
env = gym.make('CartPole-v0')
env.reset()
goal_steps = 500
score_requiremnts = 50
initial_games = 10000

def some_randdom_games_first():
    for episode in range(5):
        env.reset()
        for t in range(goal_steps):
            env.render()
            action = env.action_space.sample()
            observation, reward, done, info = env.step(action)
            if done:
                break

# some_randdom_games_first()

def initial_population():
    


