import random 
def coin_flip_simulator(n):
    head_counts=0
    for _ in range(n):
        if random.choice(["Heads","Tails"])=="Heads":
            head_counts+=1
    probability=(head_counts/n)*100
    print(f"Total probability of appearing heads is {probability}")
coin_flip_simulator(100)
coin_flip_simulator(1000)
