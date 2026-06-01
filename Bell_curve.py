# first task is to plot the bell curve and then the task is to mark the region!
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

mu=0
sigma=1

x=np.linspace(mu-4*sigma,mu+4*sigma,1000)
y=norm.pdf(x,mu,sigma)

plt.figure(figsize=(12,6))
plt.plot(x,y,color='black',linewidth=2,label="Normal Curve")

# coloring different regions
x_68=x[(x>=mu-sigma)&(x<=mu+sigma)]
y_68=norm.pdf(x_68,mu,sigma)
plt.fill_between(x_68,y_68,color='dodgerblue',alpha=0.8,label='68% ($\pm 1\sigma$)')

x_95_left=x[(x>=mu-2*sigma)&(x<=mu-sigma)]
y_95_left=norm.pdf(x_95_left,mu,sigma)
plt.fill_between(x_95_left,y_95_left,color='mediumseagreen',alpha=0.8,label='95% ($\pm2\sigma$)')

x_95_right=x[(x>=mu+sigma)&(x<=mu+2*sigma)]
y_95_right=norm.pdf(x_95_right,mu,sigma)
plt.fill_between(x_95_right,y_95_right,color='mediumseagreen',alpha=0.8)

x_99_left=x[(x>=mu-3*sigma)&(x<=mu-2*sigma)]
y_99_left=norm.pdf(x_99_left,mu,sigma)
plt.fill_between(x_99_left,y_99_left,color='tomato',alpha=0.8,label='99.7%($\pm3\sigma$)')

x_99_right=x[(x>=mu+2*sigma)&(x<=mu+3*sigma)]
y_99_right=norm.pdf(x_99_right,mu,sigma)
plt.fill_between(x_99_right,y_99_right,color='tomato',alpha=0.8)

plt.text(0,0.15,"68%",horizontalalignment='center',fontsize=14,color='white',fontweight='bold')
plt.text(-1.5,0.05,'13.5%', horizontalalignment='center', fontsize=12, color='white', fontweight='bold')
plt.text(1.5,0.05,'13.5%', horizontalalignment='center', fontsize=12, color='white', fontweight='bold')

plt.title('The 68-95-99.7% Empirical Rule', fontsize=16, fontweight='bold')
plt.xlabel('Standard Deviations from Mean ($\mu$)', fontsize=12)
plt.ylabel('Probability Density', fontsize=12)

plt.xticks(np.arange(mu - 4*sigma, mu + 5*sigma, sigma), 
           ['-4$\sigma$', '-3$\sigma$', '-2$\sigma$', '-1$\sigma$', 'Mean', '1$\sigma$', '2$\sigma$', '3$\sigma$', '4$\sigma$'])

plt.legend(loc='upper right')
plt.grid(axis='y', linestyle='--', alpha=0.5)

plt.show()