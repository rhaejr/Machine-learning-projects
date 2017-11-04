import gym
import random
import numpy as np
import tflearn
# import matplotlib.pyplot as plt
# get_ipython().magic('matplotlib inline')


# In[2]:


from tflearn.layers.core import input_data, dropout, fully_connected


# In[3]:


from tflearn.layers.estimator import regression
from statistics import mean, median
from collections import Counter


# In[4]:


LR = 1e-3
env = gym.make('CartPole-v0')


# In[5]:


env.reset()


# In[6]:


goal_steps = 500


# In[7]:


score_requirement = 50
initial_games = 10000

model = tflearn.DNN()


scores = []
choices = []
for each_game in range(10):
    score = 0
    game_memory = []
    prev_obs = []
    env.reset()
    for _ in range(goal_steps):
        env.render()

        if len(prev_obs) == 0:
            action = random.randrange(0, 2)
        else:
            action = np.argmax(model.predict(prev_obs.reshape(-1, len(prev_obs), 1))[0])

        choices.append(action)

        new_observation, reward, done, info = env.step(action)
        prev_obs = new_observation
        game_memory.append([new_observation, action])
        score += reward
        if done: break

    scores.append(score)