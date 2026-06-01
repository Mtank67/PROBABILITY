import numpy as np
import matplotlib.pyplot as plt

set_1=[2,2,3,3]
set_2=[0,0,5,5]

mean_1=np.mean(set_1)
mean_2=np.mean(set_2)

var_1=np.var(set_1)
var_2=np.var(set_2)

print(f"The mean of the set 1 is {mean_1}")
print(f"The mean of the set 2 is {mean_2}")

print(f"Set 1 - Mean: {mean_1} | Variance: {var_1}")
print(f"Set 2 - Mean: {mean_2} | Variance: {var_2}")

plt.figure(figsize=(10, 3))

plt.scatter(set_1, [1]*len(set_1), color='red', s=100, label=f'Set 1 (Low Variance: {var_1})',zorder=5)

plt.scatter(set_2, [2]*len(set_2), color='blue', s=100, label=f'Set 2 (High Variance: {var_2})',zorder=2)

# Plot the Mean line (Green)
plt.axvline(x=2.5, color='green', linestyle='--', linewidth=2, label='Mean = 2.5')

plt.title('Visualizing Data Spread (Variance)', fontsize=14, fontweight='bold')
plt.yticks([1, 2], ['Set 1', 'Set 2'])
plt.ylim(0.5, 2.5)
plt.legend()
plt.grid(axis='x', linestyle='--', alpha=0.7)

plt.show()

