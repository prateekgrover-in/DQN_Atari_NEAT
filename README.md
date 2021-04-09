### Term Paper Assignment - Neural Networks and Fuzzy Logic


- **DQN_main.py** : Rewards and Average Maximum Action Values on Atari Games are calculated over episodes using OpenAI Gym Environment

- **plotGraphRewards.py** : Contains Python Script for creating Smoothened Average Rewards Graph from given .npy file.

- **plotGraphQValues.py** : Contains Python Script for creating Smoothened Average Maximum Action Values Graph from given .npy file.

- **Performance/** : Folder containing all 16 plots as mentioned in assignment, training the DQN over 4 Atari Games, namely : Breakout, Space Invaders, QBert and Beam Rider.

- To calculate Average Maximum Action Values, we needed specific states starting from which RL Agent tries to maximize the reward. These sample states are stored in **Sample_Images/**

- **NEAT Optimization/** : Folder contains Implementation of Genetic Algorithm that uses NEAT-Python Framework to optimize structure and hyperparameters of Neural Network used for Training RL Agent on Space Invaders.
