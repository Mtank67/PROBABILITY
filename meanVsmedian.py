import numpy as np
from scipy import stats
dataset=[3,3,3,3,3,100]

mean_val=np.mean(dataset)
print(f"Mean of the data is {mean_val}")

median_val=np.median(dataset)
print(f"Median of the data is {median_val}")

result=stats.mode(dataset,keepdims=False)
#keepdims is bydefault false ,but we make it true because its suitable for broadcasting for numpy array(mean
#mode,median mein use karsakte hai mean = arr.mean(axis=1, keepdims=True) and then we do arr-mean

# maan lo default setting pe hai aur axis=0(default) aur shape (2,3) toh mean jo hai (3,) shape hoga axis 0 hat jayega
# maan lo sxis =1 hatoh (2,) ho jayega ! agar keep dims true hai toh (3,) kejagah (3,1) hoga aur (2,) ki jagah (1,2)

# this is an object have=ing two parmeters mode and count;
mode_val=result.mode

diff=abs(mean_val-median_val)
threshold=5

if diff> threshold:
    print("\n[ALERT] Data is highly skewed! The Mean is corrupted by an outlier.")
    print("Action: Use Median for imputation or remove the outlier before training the ML model.")
else:
    print("\n[OK] Mean and Median are close. Data looks somewhat Normally Distributed.")
