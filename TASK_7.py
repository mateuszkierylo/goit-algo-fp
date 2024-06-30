import random
import matplotlib.pyplot as plt
import pandas as pd

# Number of simulations
num_throws = 1000000

# Simulate dice throws
sums = [0] * 13  # Index from 0 to 12, we will use index 2 to 12

for _ in range(num_throws):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    dice_sum = die1 + die2
    sums[dice_sum] += 1

# Calculate probabilities
probabilities = [s / num_throws for s in sums]

# Theoretical probabilities
theoretical_probs = {
    2: 1/36,
    3: 2/36,
    4: 3/36,
    5: 4/36,
    6: 5/36,
    7: 6/36,
    8: 5/36,
    9: 4/36,
    10: 3/36,
    11: 2/36,
    12: 1/36
}

# Create a DataFrame for better visualization
data = {
    'Sum': list(range(2, 13)),
    'Simulated Probability': [probabilities[i] for i in range(2, 13)],
    'Theoretical Probability': [theoretical_probs[i] for i in range(2, 13)]
}

df = pd.DataFrame(data)

# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(df['Sum'], df['Simulated Probability'], marker='o', linestyle='-', label='Simulated Probability')
plt.plot(df['Sum'], df['Theoretical Probability'], marker='x', linestyle='--', label='Theoretical Probability')
plt.xlabel('Sum of Two Dice')
plt.ylabel('Probability')
plt.title('Simulated vs Theoretical Probabilities of Dice Sums')
plt.legend()
plt.grid(True)
plt.show()

# Display the table
print(df)

# Save the results in a readme file
with open('/mnt/data/readme.md', 'w') as f:
    f.write("# Monte Carlo Simulation of Dice Throws\n\n")
    f.write("## Simulated Probabilities vs Theoretical Probabilities\n")
    f.write(df.to_markdown(index=False))
    f.write("\n\n## Conclusion\n")
    f.write("The Monte Carlo simulation closely matches the theoretical probabilities. The minor discrepancies are due to the random nature of the simulation and the finite number of throws. Increasing the number of throws would further reduce these discrepancies.")

import ace_tools as tools; tools.display_dataframe_to_user(name="Monte Carlo Simulation of Dice Throws", dataframe=df)
