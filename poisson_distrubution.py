import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

lamda_val=9.0

# lets find the prob for arriving 3 cars
prob_3=poisson.pmf(k=3,mu=lamda_val)
prob_9=poisson.pmf(k=9,mu=lamda_val)

print(f"The probability of getting 3 cars {prob_3:.4f} or {prob_3*100:.2f}")
print(f"The probability of getting 9 cars {prob_9:.4f} or {prob_9*100:.2f}")

x=np.arange(3,21)
y=poisson.pmf(x,mu=lamda_val)

plt.bar(x,y,color='purple',edgecolor='black',alpha=0.7)
plt.axvline(x=lamda_val,color='red',linestyle='--',linewidth=2,label=f"Average $\lambda={lamda_val}$")

plt.title("Expected distribution(Expecetd $\lambda$=9hrs/hr)",fontsize=14,fontweight='bold')
plt.xlabel("Number of cars Arriving K")
plt.ylabel('Probability P(X = k)')
plt.xticks(x)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.5)

plt.show()
