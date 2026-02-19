import random
trials = 100000
independent_success = 0
for _ in range(trials):
    coin = random.choice(["H", "T"])
    die = random.randint(1, 6)  
    if coin == "H" and die == 6:
        independent_success += 1
independent_probability = independent_success / trials
dependent_success = 0
for _ in range(trials):
    bag = ["R"] * 5 + ["B"] * 5
    first_pick = random.choice(bag)
    bag.remove(first_pick)
    second_pick = random.choice(bag)
    if first_pick == "R" and second_pick == "R":
        dependent_success += 1
dependent_probability = dependent_success / trials
print("Independent Event (Heads AND 6):")
print("Experimental Probability:", independent_probability)
print("Theoretical Probability:", 1/12)
print("\nDependent Event (Two Reds without replacement):")
print("Experimental Probability:", dependent_probability)
print("Theoretical Probability:", 2/9)
