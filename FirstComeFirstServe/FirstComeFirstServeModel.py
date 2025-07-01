#Modeling the First Come First Serve (FCFS) scheduling algorithm

import time
import os
import pandas as pd


points = [] #create an empty list to store the points
maxPoolSize = 100 #set the maximum pool size for passengers
numIterations = 20 #set the number of iterations for the simulation
numSeats = 50 #set the number of seats available (should be less than maxPoolSize)
totalElapsedTime = [0 for _ in range(maxPoolSize)] # initialize cumulative probabilities for each passenger to 0

for i in range(1, maxPoolSize + 1):

    cumulativeProb = [0 for _ in range(i)] # initialize cumulative probabilities for each passenger to 0
    elapsedTime = 0 #initialize elapsed time

    for j in range(1, numIterations+1):
        # for i passengers, we are running j iterations of the simulation

        for passenger in range(i): # for passenger arrival
            start = time.time()
            if passenger < numSeats:
                cumulativeProb[passenger] = ((cumulativeProb[passenger] * (j - 1) + 1)) / j
                end = time.time() # passenger is seated
                elapsedTime += end - start
            else:
                cumulativeProb[passenger] = (cumulativeProb[passenger] * (j - 1)) / j
                end = time.time() # passenger is not seated
                elapsedTime += end - start

    for x in range(i):
        points.append([i, cumulativeProb[x]])
    
    totalElapsedTime[i-1] = (elapsedTime) / (i * numIterations) # average elapsed time for i passengers


# Create output folder
output_folder = "generatedTestData"
os.makedirs(output_folder, exist_ok=True)

# Create DataFrame for probabilities
df_prob = pd.DataFrame(points, columns=['NumPassengers', 'Probability'])

# Create DataFrame for elapsed times
df_time = pd.DataFrame({
    'NumPassengers': [i+1 for i in range(len(totalElapsedTime))],
    'AvgElapsedTime_ms': totalElapsedTime
})

# Write to Excel files
prob_file = os.path.join(output_folder, "passenger_probabilities.xlsx")
time_file = os.path.join(output_folder, "elapsed_times.xlsx")

df_prob.to_excel(prob_file, index=False)
df_time.to_excel(time_file, index=False)

print(f"Files saved to {output_folder}:\n- {prob_file}\n- {time_file}")


# #printing 
# print("Starting Simulation: \n")
# for point in points:
#     print(f"Num Passengers: {point[0]}, Cumulative Probability: {point[1]:.4f}")

# for i in range(len(totalElapsedTime)):
#     print(f"Average Elapsed Time for {i+1} Passengers: {totalElapsedTime[i]:.8f} seconds")