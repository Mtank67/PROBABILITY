import matplotlib.pyplot as plt 
from  scipy.stats import binom
import numpy as np

n=8
p=0.8
# geneerate the x values;
x_values=np.arange(0,n+1)
y_values=binom.pmf(x_values,n,p)
for x,y in zip(x_values,y_values):
    print(f"P(X={x}) is equal to {y:.3f}")

# lets set the canvas now
plt.figure(figsize=(8,5))
plt.bar(x_values,y_values,color='orange',edgecolor='black')

plt.title(f"Binomial Distribution (n={n},p={p}): ",fontsize=14,fontweight='bold')
plt.xlabel("Number of heads (Random Variable X)",fontsize=12)
plt.ylabel("Probability",fontsize=12)
plt.xticks(x_values)
plt.grid(axis='y',linestyle='--',alpha=0.7)

plt.show()
