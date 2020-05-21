# Reinforcement Learning

### Types of Reinforcement Learning
- 1) Deep Q Learning (DQN)
- 2) Policy Gradient (PG)

Argument for PG over DQN:
We have presented asynchronous versions of four standard reinforcement  learning  algorithms and showed that they are able to train neural network  controllers on a variety of domains in a stable manner. Our results show that in our proposed framework stable training of neural networks through reinforcement learning is possible with both value-based and policy-based methods, off-policy as well as on-policy methods, and in discrete as well as continuous do-mains.  When trained on the Atari domain using 16 CPU cores, the  proposed  asynchronous  algorithms  train  faster than DQN trained on an Nvidia K40 GPU, with A3C surpassing the current state-of-the-art in half the training time. One of our main findings is  that  using  parallel  actor-learners to update a shared model had a stabilizing effect on the learning process of the three value-based methods we considered. While this shows that stable online Q-learning is possible without experience replay, which was used for this purpose in DQN, it does not mean that experience replay is not useful. Incorporating experience replay into the asynchronous reinforcement learning framework could substantially improve the data efficiency of these methods by reusing old data. This could in turn lead to much faster training times in domains like TORCS where interacting with the environment is more expensive than updating the model for the architecture we used. Combining  other existing reinforcement learning methods or recent advances in deep  reinforcement learning with our asynchronous framework presents many possibilities for immediate improvements to the methods we presented.  While our n-step methods operate in the forward view(Sutton & Barto, 1998) by using corrected n-step re-turns directly as targets, it has been more common to use the backward view to implicitly combine different returns through eligibility traces (Watkins, 1989; Sutton & Barto,1998; Peng & Williams, 1996). The asynchronous advantage actor-critic method could be potentially improved by using other ways of estimating the advantage function, such  as  generalized advantage estimation of (Schulmanet al., 2015b). All of the value-based methods we investigated could benefit from different ways of reducing over-estimation bias of Q-values (Van Hasselt et al., 2015; Belle-mare et al., 2016). Yet another, more speculative, direction is to try and combine the recent work on true online temporal difference methods (van Seijen et al., 2015) with non-linear function approximation. In addition to these algorithmic improvements, a number of complementary improvements to the neural network architecture are possible. The dueling architecture of (Wanget al., 2015) has been shown to produce more accurate estimates of Q-values by including separate streams for the state value and advantage in the network. The spatial softmax proposed by (Levine et al., 2015) could improve both value-based and policy-based methods by making it easier for the network to represent feature coordinates.

##### 1) DQN
- off-policy: Approximate Q and infer optimal policy

##### 2) PG
- on-policy: Directly optimizing the policy space
- In recent times, PG is more widely used as compared to DQN as PG works better than DQN when tuned well


Training protocol: Over one game, as long as the end outcome is a loss, then the entire game will be labelled as having a negative reward. How does this work if let's say the first 50 moves out of 1000 moves made (for example), were good? Will they not be considered/be considered as bad? You’re right - it would. However, when you consider the process over thousands/millions of games, then doing the first moves correctly makes you slightly more likely to win down the road, so on average you’ll see more positive than negative updates for the correct moves and your policy will end up doing the right thing.





I begin with firstly understanding a form of Reinforcement Learning, namely Q-Learning.  
The environment i worked with would be the mountaincar from open.ai gym. 
Main objective is to get the car to the top of the mountain.

3 actions (0, 1, 2 corresponding to left, still, right)  -action space
None of these matter to the model as it only wants to learn the order of actions that would lead to the best outcome.

Observations on the other hand are returned from resets and steps.
Observation space in this case was the general position as well as the velocity of the car (2 values).

At each step, we are able to get the state, reward as well as whether the environment is done. (Done when peak is reached, or reached limit of 200 steps)

There is a "Q" value per action possible per state.
Since there are 3 possible actions, each one has its own table, size of which I can determine (eg 20 by 20 by 3)

Links:

(Reinforcement Learning - Sutton and Barto)[https://www.youtube.com/playlist?list=PLnn6VZp3hqNvRrdnMOVtgV64F_O-61C1D]

(Epsilon Greedy Algorithm)[https://jamesmccaffrey.wordpress.com/2017/11/30/the-epsilon-greedy-algorithm/]

(Q Learning intro and Q table - Reinforcement learning with python)[https://pythonprogramming.net/q-learning-reinforcement-learning-python-tutorial/]

(Self-Driving cars with Carla and Python)[https://pythonprogramming.net/introduction-self-driving-autonomous-cars-carla-python/]