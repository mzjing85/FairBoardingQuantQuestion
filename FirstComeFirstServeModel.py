#Modeling the First Come First Serve (FCFS) scheduling algorithm

points = [] #create an empty list to store the points
maxPoolSize = 100 #set the maximum pool size for passengers
numIterations = 20 #set the number of iterations for the simulation
numSeats = 50 #set the number of seats available (should be less than maxPoolSize)

for i in range(1, maxPoolSize + 1):

    cumulativeProb = [0 for _ in range(i)] # initialize cumulative probabilities for each passenger to 0

    for j in range(1, numIterations+1):
        # for i passengers, we are running j iterations of the simulation

        for passenger in range(i):
            if passenger < numSeats:
                cumulativeProb[passenger] = ((cumulativeProb[passenger] * (j - 1) + 1)) / j
            else:
                cumulativeProb[passenger] = (cumulativeProb[passenger] * (j - 1)) / j

    for x in range(i):
        points.append([i, cumulativeProb[x]])

#printing 
print("Starting Simulation: \n")
for point in points:
    print(f"Num Passengers: {point[0]}, Cumulative Probability: {point[1]:.4f}")