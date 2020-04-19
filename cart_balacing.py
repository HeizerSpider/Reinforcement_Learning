import gym
env = gym.make('CartPole-v0') # can be replaced with  MountainCar-v0, MsPacman-v0 (requires the Atari dependency), or Hopper-v1 
print(env.action_space)
#> Discrete(2)
print(env.observation_space)
#> Box(4,)
for i_episode in range(20):
    observation = env.reset()
    for t in range(100):
        env.render()
        print(observation)
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break
env.close()