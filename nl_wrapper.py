import gym
import numpy as np
from language import learn_model

class BasicWrapper(gym.Wrapper):
    def __init__(self, env):
        super().__init__(env)
        self.env = env
        
    def step(self, action):
        next_state, reward, done, info = self.env.step(action)
        # modify ...
        return next_state, reward, done, info
        
class ObservationWrapper(gym.ObservationWrapper):
    def __init__(self, env):
        super().__init__(env)
    
    def observation(self, obs):
        # modify obs
        return obs
    
class RewardWrapper(gym.RewardWrapper):
    def __init__(self, env, trajectory, learn_model: learn_model):
        super().__init__(env)
        self.trajectory = trajectory
        self.learn_model = learn_model
    
    def reward(self, rew):
        # modify rew 
        return rew + self.get_nl_reward(self.trajectory)
    
    def get_nl_reward(trajectory):
        # get reward from NL
        return learn_model.get_nl_reward(trajectory)


    
class ActionWrapper(gym.ActionWrapper):
    def __init__(self, env):
        super().__init__(env)
    
    def action(self, act):
        # modify act
        return act