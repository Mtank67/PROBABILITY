import matplotlib.pyplot as plt
from collections import Counter

outcomes=[1,3,4,5,6,6]
total_outcomes=len(outcomes)
counts=Counter(outcomes)
# this will build the dictionary mentioning the frequency of each of the value:

probability_distribution={x:count/total_outcomes for x, count in counts.items()}

print("Probability distribution for the random variable X(unfair dice) is: ")
for x in range(1,7):
    prob=probability_distribution.get(x,0.0)
    print(f"The probability P(X={x}) is {prob:.2f}")

# prob greater P(X>5)
prob_greater_equal_5=probability_distribution.get(5,0.0)+probability_distribution.get(6,0.0)
print(f"\n P(X>=5) is equal to {prob_greater_equal_5:.2f}")

x_values=range(1,7)
y_values=[probability_distribution.get(x,0.0) for x in x_values]

plt.figure(figsize=(8,5))

plt.bar(x_values,y_values,color='skyblue',edgecolor='black')

plt.xlabel("Dice Outcomes(Random variabl X)",fontsize=12)
plt.ylabel("Probaility P(X=x)",fontsize=12)
plt.title("Probability distribution of unfair Dice",fontsize=14,fontweight='bold')

plt.ylim(0,0.5)
plt.grid(axis='y',linestyle='--',alpha=0.7)

plt.show()
