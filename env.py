import gymnasium as gym
from gymnasium import spaces
import numpy as np

class CustomEnv(gym.Env):
    def __init__(self):
        super(CustomEnv, self).__init__()
        
        # Define action and observation space
        # They must be gym.spaces objects
        # Example for using discrete actions:
        self.action_space = spaces.Discrete(2)
        
        # Example for using box observation space:
        self.observation_space = spaces.Box(low=0, high=1, shape=(3,), dtype=np.float32)
        
        # Initialize state
        self.state = np.zeros(3)
        
    def step(self, action):
        # Execute one time step within the environment
        self.state = self.state + action  # Example state transition
        reward = 1.0  # Example reward
        done = False  # Example condition to end the episode
        info = {}  # Additional information
        
        return self.state, reward, done, info
    
    def reset(self):
        # Reset the state of the environment to an initial state
        self.state = np.zeros(3)
        return self.state
    
    def render(self, mode='human'):
        # Render the environment to the screen
        print(f'State: {self.state}')
    
    def close(self):
        # Perform any necessary cleanup
        pass

# Example usage
if __name__ == "__main__":
    env = CustomEnv()
    env.reset()
    for _ in range(10):
        action = env.action_space.sample()
        state, reward, done, info = env.step(action)
        env.render()
        if done:
            break
    env.close()