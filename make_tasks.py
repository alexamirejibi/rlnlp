
import gym 
# from gym.utils.play import play
import random
import sys
sys.path.insert(0, 'language/')
import language.nl_wrapper as nlw
# import atari wrappers
from stable_baselines3.common.atari_wrappers import AtariWrapper
from stable_baselines3.common.vec_env import VecFrameStack
from language.task_wrapper import TaskWrapper
from language.tasks import *
from language.play import play
import numpy as np
from ale_py import ALEInterface
import pickle
import time 

env = gym.make("ALE/MontezumaRevenge-v5")
height, width, channels = env.observation_space.shape
actions = env.action_space.n

# env = AtariWrapper(env)
#env = nlw.BasicWrapper(env)
task = ClimbDownRightLadder
env = TaskWrapper(env, task=task, instruction='Climb down the ladder, go right and jump over the gap to the right')

env.reset()
save_name = 'task_states/task_5.pkl'
play(env, zoom=5)
start_pos = env.agent_pos()
state = env.clone_state()
with open(save_name, 'wb') as outp:  # Overwrites any existing file.
    pickle.dump(state, outp, pickle.HIGHEST_PROTOCOL)
env.reset()

# --- load pickle ---
with open(save_name, 'rb') as inp:
    newState = pickle.load(inp)
env.restore_state(newState)
env.step(0)
# ------------------------------------------------------------------
play(env, zoom=5)
end_pos = env.agent_pos()

print("start: ", start_pos)
print("end: ", end_pos)

# for episode in range(1, episodes+1):
#     state = env.restore_state(newState) 
#     start_lives = 6
#     env.step(0)
#     done = False
#     score = 0 
#     dead = False

#     while not (done or dead):
#         if env.lives < 6:
#             dead = True
#         print(env.lives)
#         env.render()
#         action = env.env.action_space.sample()
#         n_state, reward, done, info = env.step(action)
#         score+=reward
#         time_steps += 1
#         #time.sleep(0.01)
#     print('Episode:{} Score:{}'.format(episode, score))
#     print(env.agent_pos())
#     print(env.has_key())
#     print(env.room())
# print(time_steps)
# env.close()