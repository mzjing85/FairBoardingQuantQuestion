import random
import time
import os
import pandas as pd

points = []  # list to store the points
maxPoolSize = 100  # max pool size for passengers
numIterations = 1000  # iterations of the simulation
numSeats = 50  # number of seats available (should be less than maxPoolSize)

totalElapsedTime = [0 for _ in range(maxPoolSize)]  # cumulative elapsed time for each passenger count

for i in range(1, maxPoolSize + 1):
    cumulativeProb = [0 for _ in range(i)]  # cumulative probabilities for passengers
    elapsedTime = 0  # elapsed time accumulator

    for j in range(1, numIterations + 1):
        sample_size = min(numSeats, i)
        selected_indices = random.sample(range(i), sample_size)

        start = time.time()  # timer start for iteration

        for passenger in range(i):
            if passenger in selected_indices:
                cumulativeProb[passenger] = ((cumulativeProb[passenger] * (j - 1) + 1)) / j
            else:
                cumulativeProb[passenger] = (cumulativeProb[passenger] * (j - 1)) / j

        end = time.time()  # timer end for iteration
        elapsedTime += end - start

    for x in range(i):
        points.append([i, cumulativeProb[x]])

    totalElapsedTime[i - 1] = elapsedTime / numIterations  # avg elapsed time per iteration for i passengers

# Create output folder
output_folder = "generatedTestData"
os.makedirs(output_folder, exist_ok=True)

# Create DataFrame for probabilities
df_prob = pd.DataFrame(points, columns=['NumPassengers', 'Probability'])

# Create DataFrame for elapsed times
df_time = pd.DataFrame({
    'NumPassengers': [i + 1 for i in range(len(totalElapsedTime))],
    'AvgElapsedTime_s': totalElapsedTime
})

# Write to Excel files
prob_file = os.path.join(output_folder, "passenger_probabilities.xlsx")
time_file = os.path.join(output_folder, "elapsed_times.xlsx")

df_prob.to_excel(prob_file, index=False)
df_time.to_excel(time_file, index=False)

print(f"Files saved to {output_folder}:\n- {prob_file}\n- {time_file}")
