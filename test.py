import gym
env = gym.make('MsPacman-v0')
env.reset()
for _ in range(2000):
    env.render()
    a = env.action_space.sample()
    env.step(a)
