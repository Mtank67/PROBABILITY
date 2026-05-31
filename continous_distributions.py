import numpy as np 
import scipy.integrate as integrate
import matplotlib.pyplot as plt
def f(x):
    return np.where(x>=0,np.exp(-x),0)
total_probaility,error_marigin=integrate.quad(f,0,np.inf)
print(f"Total probability under this curve is P(X=x) is: {total_probaility:.1f}")

lower_limit=1.9
upper_limit=2.1

prob_interval,error=integrate.quad(f,lower_limit,upper_limit)

print(f"\n Probability  of rain between {lower_limit} and {upper_limit} is {prob_interval:.3f}")
print(f"chances of rain is {prob_interval*100:.2f}%")

exact_prob,_=integrate.quad(f,2.0,2.0)
print(f"The exact prob for 2 inches of rain is is {exact_prob:.1f}")

# now comes the ineterseting part and that is plotting!
plt.figure(figsize=(8, 5))

x_values=np.linspace(0,5,5000)
y_values=[f(x) for x in x_values]

plt.plot(x_values,y_values,color='blue',linewidth=2,label='PDF:f(x)=exp(-x)')

x_fill=np.linspace(lower_limit,upper_limit,100)
y_fill=f(x_fill)# ye line agar use karni hai directly without using list comprehension
# toh humara function numpy array direct handle karna aana chaiye!
plt.fill_between(x_fill,y_fill,color='red',alpha=0.5,label='Area(probability) between 1.9 and 2.1')


# now we show a line at 2.0
plt.axvline(x=2.0,color='green',linestyle='--',label='Exact point X=2 (Area=0)')

plt.xlabel("Rainfall in inches",fontsize=12)
plt.ylabel("Probability Density function",fontsize=12)
plt.legend()
plt.show()