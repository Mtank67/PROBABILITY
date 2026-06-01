import numpy 
data=np.array([1,2,3,8,7])


# 1. Population Standard Deviation (Divide by N)
# Numpy defaults to Population
pop_std = np.std(data)
print(f"Population Standard Deviation: {pop_std:.2f}") # Output: 2.79

# 2. Sample Standard Deviation (Divide by n-1)
# Same as before, we use ddof=1 for Bessel's Correction
sample_std = np.std(data, ddof=1)
print(f"Sample Standard Deviation: {sample_std:.2f}") # Output: 3.11