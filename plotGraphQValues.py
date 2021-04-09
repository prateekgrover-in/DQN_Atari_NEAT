import numpy as np
import matplotlib.pyplot as plt

q_values = np.load('Q_DQN_SpaceInvaders.npy')

## Smoothening the Plot

start = 0
q_plot_smooth = []
q_plot_max = []
q_plot_min = []
end = 50
x_axis = []

while (end < len(q_values)):
    cur = q_values[start : end]
    start = start + 10
    end = end + 10
    x_axis.append(end)
    q_plot_smooth.append(1.0*sum(cur)/50.0)
    q_plot_max.append(max(cur))
    q_plot_min.append(min(cur))

plt.figure(figsize=(12,8)) 
plt.plot(x_axis, q_plot_smooth)
plt.plot(x_axis, q_plot_max)
plt.plot(x_axis, q_plot_min)

plt.title("Average Maximium Action Value on Space Invaders")
plt.xlabel("Episodes")
plt.ylabel("Max Q Value")
plt.legend(['Average Performance of Set', 'Max Q Value in Batch', 'Min Q Value in Batch'], loc ="upper right")
plt.grid()

plt.savefig('Q_DQN_SpaceInvaders.png')