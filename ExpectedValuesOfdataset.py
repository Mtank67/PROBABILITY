import numpy as np
def analyze_binomial_experiment(n_trials,success):
    n=n_trials
    p=success

    ex_mean=n*p
    ex_var=n*p*(1-p)

    return ex_mean,ex_var

n=10
p=0.4

E_X,Var_x=analyze_binomial_experiment(n,p)
deviation=np.sqrt(Var_x)
print(f"The number of trials for the experiment is:{n}")
print(f"The accuracy of each shot is: {p}")
print(f"The expected value is: {E_X}")
print(f"The variance with respect to the mean is {Var_x}")
print(f"The standard deviation of the set is {deviation}")