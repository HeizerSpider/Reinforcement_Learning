import gym
import numpy as np

env = gym.make("MountainCar-v0")
env.reset()

print(env.observation_space.high) # sometimes we engage in some environments in which we dont know these values and hence we have to learn for awhile before we actually get to know these values
print(env.observation_space.low)
print(env.action_space.n) #how many actions we can actually take

#OS == obervation space
DISCRETE_OS_SIZE = [20] * len(env.observation_space.high) #observation space table size
discrete_os_win_size = (env.observation_space.high-env.observation_space.low) / DISCRETE_OS_SIZE

print(discrete_os_win_size)

q_table = np.random.uniform(low = -2, high = 0, size = (DISCRETE_OS_SIZE + [env.action_space.n]))
# gives every combination space and velocity , 20 by 20 by 3 actions that can be taken, with values between -2 and 0, and the values should be slowly tweaked and optimized over time
print(q_table.shape)
print(q_table)

'''

done = False

while not done:
    action = 2
    new_state, reward, done, _ = env.step(action) #state in this case is position and velocity
    print(reward, new_state)
    env.render()

env.close()

'''