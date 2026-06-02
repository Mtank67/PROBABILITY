import math

def poisson_probability_manual(lambda_val, k):

    prob = ((lambda_val ** k) * math.exp(-lambda_val)) / math.factorial(k)
    return prob


expected_cars = 9.0
target_cars = 2

prob = poisson_probability_manual(expected_cars, target_cars)

print(f"Expected Average (Lambda): {expected_cars} cars/hr")
print(f"Target Exact Cars (k): {target_cars} cars/hr")
print(f"Calculated Probability: {prob:.6f} (or {prob * 100:.4f}%)")
