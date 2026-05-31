import numpy as np 
from scipy.stats import binom
import matplotlib.pyplot as plt
n_values=[10,50,200]
p=0.5


plt.figure(figsize=(15,5))
for i,n in enumerate(n_values,1):
    plt.subplot(1,3,i)
    # generate the x values for the given range
    x_values=np.arange(0,n+1)
    y_values=binom.pmf(x_values,n,p)

    plt.bar(x_values,y_values,color='teal',edgecolor='black',alpha=0.7)
    plt.xlabel("Number of Heads",fontsize=12,fontweight='bold')
    if i==1:
        plt.ylabel("Probability",fontsize=12,fontweight='bold')
    plt.title(f'Binomial Distribution (n = {n})', fontsize=12, fontweight='bold')

    if n==200:
        plt.xlim(70,130)
plt.tight_layout()
plt.show()

