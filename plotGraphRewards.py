import numpy as np
import matplotlib.pyplot as plt

all_rewards = np.load('Rewards_DQN_QBert.npy')

## Smoothening the Plot

start = 0
reward_plot_smooth = []
reward_plot_max = []
reward_plot_min = []
end = 50
x_axis = []

while (end < len(all_rewards)):
    cur = all_rewards[start : end]
    start = start + 10
    end = end + 10
    x_axis.append(end)
    reward_plot_smooth.append(1.0*sum(cur)/50.0)
    reward_plot_max.append(max(cur))
    reward_plot_min.append(min(cur))
    
plt.figure(figsize=(12,8)) 
plt.plot(x_axis, reward_plot_smooth)
plt.plot(x_axis, reward_plot_max)
plt.plot(x_axis, reward_plot_min)

plt.title("DQN on QBert")
plt.xlabel("Episodes")
plt.ylabel("Reward")
plt.legend(['Average Performance of Set', 'Max Reward in Batch', 'Min Reward in Batch'], loc ="upper right")
plt.grid()

plt.savefig('DQN_QBert.png')