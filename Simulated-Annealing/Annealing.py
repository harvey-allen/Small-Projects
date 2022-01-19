import sys
import random
import math
import time

#Neighbourhood Function
def getNeighbour(state):
    randomCandidate = random.randint(0, 33)
    candidateSelection = state[(randomCandidate + 1)]
    #Swapping Adjacent Candidates
    state[(randomCandidate + 1)] = state[randomCandidate]
    state[randomCandidate] = candidateSelection
    return state, int(state[randomCandidate]), int(state[(randomCandidate + 1)])

#Cost Function Calculation
def getCost(state, graph):
    costValue = 0
    for edge in graph:
        if state.index(int(edge[0])) < state.index(int(edge[1])):
            costValue += int(graph[edge])
    return costValue

#Simulated Annealing Algorithm Parameters:
#x0 = Initial Solution 
#Ti = Initial Temperature (100)
#Tl = Temperature Length (25)
#f = Cooling Ratio (0.99)
#stoppingCriterion = Number of non improved states to stop algorithm (8)
def simulatedAnnealing(x0, graph, identification, Ti=100, Tl=25, f=0.99, stoppingCriterion=8):
    start = time.time()
    currentState = x0 #Construct Initial Solution
    currentTemp = Ti #Set Initial Temperature
    counter = 0
    #Outer Loop
    while counter < stoppingCriterion: #Stopping Criterion
        #Inner Loop
        Tl += 0.001 #Varying iterations at each temperature
        for i in range(1, round(Tl)):
            neighbourState = currentState[:]
            neighbour, swapA, swapB = getNeighbour(neighbourState) #Generate Random Neigbour
            #Compute Change Of Cost (Streamlined for efficiency)
            costDifference = 0
            if (str(swapA), str(swapB)) in graph.keys():
                costDifference = int(graph[(str(swapA), str(swapB))])
            elif (str(swapB), str(swapA)) in graph.keys():
                costDifference = - int(graph[(str(swapB), str(swapA))])
            #Check Acceptance
            if costDifference <= 0:
                currentState = neighbour
                counter = 0
            else:
                q = random.uniform(0, 1)
                if q < math.exp(-costDifference / currentTemp):
                    currentState = neighbour
                    counter = 0
                else:
                    counter += 1
        currentTemp = currentTemp*f #Set new temperature
    end = time.time()
    solution = currentState
    finalCost = getCost(solution, graph)
    finalTime = str((end - start)*1000)[:6]
    #Final Results
    return solution, finalCost, finalTime
    

def main(data):
    #Data Structures
    allData = []
    identifier = []
    tournementGraph = []
    efficientGraph = {}
    identification = {}
    #Formatting Data
    results = open(data, "r")
    resultsLength = int(results.read(2)) + 1
    x0 = list(range(1, resultsLength)) #Initial Solution
    for line in results:
        allData.append(line)
    for x in allData[1:resultsLength]:
        x = x[:-2].split(",")
        identifier.append(x)
    for x in allData[resultsLength+1:]:
        x = x[:-1].split(",")
        tournementGraph.append(x)
    for edge in tournementGraph:
        efficientGraph[(edge[1], edge[2])] = edge[0]
    for x in identifier:
        identification[int(x[0])] = x[1]
    #Run Algorithm
    optimalSolution = [0, 100, 0]
    for i in range(1, 25):
        solution, cost, time = simulatedAnnealing(x0, efficientGraph, identification)
        if cost < optimalSolution[1]:
            optimalSolution = [solution, cost, time]
    #Print Results
    print(" ")
    print("Final Ranking:")
    print(" ")
    position = 1
    for result in optimalSolution[0]:
        print(str(position) + ": " + identification[result] + " (" + str(result) + ")")
        position += 1
    print(" ")
    print("Kemeny Score: " + str(optimalSolution[1]))
    print(" ")
    print("Runtime: " + optimalSolution[2] + "ms")
    print(" ")
    
#Run from command line
if __name__ == "__main__":
    main(sys.argv[2])

    
