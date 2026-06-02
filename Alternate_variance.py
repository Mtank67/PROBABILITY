import numpy as np 
import time 

dataset=np.random.rand(1000)
n=len(dataset)

start_time=time.time()

mu=sum(dataset)/n

squared_diff_sum=0
for x in dataset:
    squared_diff_sum+=(x-mu)**2
variance_1=squared_diff_sum/n
time_1=time.time()-start_time

print(f"Time taken with the traditional variation formula is {time_1}")

start_time=time.time()
sum_1=0
squared_sum=0
for x in dataset:
    sum_1+=x;
    squared_sum+=(x)**2
mu_square=(sum_1/n)**2
squared_sum_avg=squared_sum/n

variance_2=squared_sum_avg-mu_square
time_2=time.time()-start_time
print(f"Time taken with the alternate variance formula is {time_2}")


