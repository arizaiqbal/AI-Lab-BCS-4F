import numpy as np

states = ["Sunny", "Cloudy", "Rainy"]

transition = np.array([
    [0.6, 0.3, 0.1],  # Sunny
    [0.3, 0.4, 0.3],  # Cloudy
    [0.2, 0.3, 0.5]   # Rainy
])

current = 0
days = []

for i in range(10):
    current = np.random.choice([0,1,2], p=transition[current])
    days.append(states[current])

print("Weather for 10 days:")
print(days)

rainy_days = days.count("Rainy")
print("Rainy days:", rainy_days)

count = 0
trials = 10000

for _ in range(trials):
    current = 0
    rainy = 0
    for i in range(10):
        current = np.random.choice([0,1,2], p=transition[current])
        if states[current] == "Rainy":
            rainy += 1
    if rainy >= 3:
        count += 1

print("P(at least 3 rainy days):", count / trials)
