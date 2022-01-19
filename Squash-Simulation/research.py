import random, csv
import matplotlib.pyplot as plt

def gamePARS(ra, rb):
    p = ra/(ra+rb) #Probability that A wins a point
    #Initialises the variables
    raScore = 0
    rbScore = 0
    gameIncomplete = True
    #Has to have a score equal or larger than 11 and a difference of 2 for the game to end
    while not ((raScore >= 11 and raScore >= (rbScore + 2)) or (rbScore >= 11 and rbScore >= (raScore + 2))):
            r = random.random()
            if r < p:
                raScore += 1
            else:
                rbScore += 1
    return (raScore, rbScore)

def gameEnglish(ra, rb):
        p = ra/(ra+rb) #Probability that A wins a point
        #Initialises the variables
        raScore = 0
        rbScore = 0
        serveFirst = random.randint(0, 1)
        if serveFirst == 1:
            raServe = True
        else:
            raServe = False
        gameIncomplete = True
        #Has to have a score equal or larger than 9 and a difference of 2 for the game to end
        while not ((raScore >= 9 and raScore >= (rbScore + 2)) or (rbScore >= 9 and rbScore >= (raScore + 2))):
                r = random.random()
                if r < p:
                    if raServe:
                        raScore += 1
                    else:
                        raServe = True
                else:
                    if not raServe:
                        rbScore += 1
                    else:
                        raServe = False
        return (raScore, rbScore)

def calcPARS(ra, rb, n):
    #Initialises the variables
    raWins = 0
    rbWins = 0
    gamesPlayed = 0
    pointsPlayed = 0
    while gamesPlayed < n: #Loops for a set number of games taken as a parameter
        result = gamePARS(ra, rb)
        pointsPlayed += (result[0] + result[1])
        if result[0] > result[1]:
            raWins += 1
            gamesPlayed += 1
        else:
            rbWins += 1
            gamesPlayed += 1
    probability = raWins/gamesPlayed # Calculates the probability
    return ("{0:.2f}".format(probability), pointsPlayed) #Formats the result to 2 decimal places

def calcEnglish(ra, rb, n):
    #Initialises the variables
    raWins = 0
    rbWins = 0
    gamesPlayed = 0
    pointsPlayed = 0
    while gamesPlayed < n: #Loops for a set number of games taken as a parameter
        result = gameEnglish(ra, rb)
        pointsPlayed += (result[0] + result[1])
        if result[0] > result[1]:
            raWins += 1
            gamesPlayed += 1
        else:
            rbWins += 1
            gamesPlayed += 1
    probability = raWins/gamesPlayed # Calculates the probability
    return ("{0:.2f}".format(probability), pointsPlayed) #Formats the result to 2 decimal places

def readCSV(file):
    #Initialises the variables
    abilitysList = []
    abilitysReturn = []
    #Opens the csv file
    with open(file) as csvfile:
        rdr = csv.reader(csvfile)
        for row in rdr: #Loops through each line
            abilitysList.append(row)
        abilitysList = abilitysList[1:] #Removes the initial line
    for x in abilitysList:
        x = x[:-1] #Removes the blank value from the end of the list
        abilityTemp = []
        for value in x:
            abilityTemp.append(int(value))
        abilitysReturn.append(tuple(abilityTemp)) #Adds the integer vales as tuples to a list
    return abilitysReturn

def simulation():
    games = readCSV('scores.csv')
    resultsPARS = []
    resultsEnglish = []
    resultsX = []
    for game in games:
        #Plots the graph/ Retrives the data
        resultsPARS.append(float(calcPARS(game[0], game[1], 100)[0]))
        resultsEnglish.append(float(calcEnglish(game[0], game[1], 100)[0]))
        resultsX.append(game[0]/game[1])
        resultsPARSSorted = sorted(resultsPARS)
        resultsEnglishSorted = sorted(resultsEnglish)
        resultsXSorted = sorted(resultsX)
    #Draws and sets the labels on the graph
    plt.plot(resultsXSorted, resultsPARSSorted, label = "PARS")
    plt.plot(resultsXSorted, resultsEnglishSorted, label = "English", color = "red")
    plt.ylabel('Probability that player A beats player B')
    plt.xlabel("Ra/Rb (Player A's ability divided by Player B's ability)")
    plt.legend()
    plt.show()

simulation()

def timeTaken():
    resultsPARS = []
    resultsEnglish = []
    for x in range(0, 10):
        #Abilitys are randomly generated
        ra = random.randint(0, 100)
        rb = random.randint(0, 100)
        resultsPARS.append(float(calcPARS(ra, rb, 100)[1]))
        resultsEnglish.append(float(calcEnglish(ra, rb, 100)[1]))
    #Averages calculated
    averagePARS = sum(resultsPARS)/1000
    averageEnglish = sum(resultsEnglish)/1000
    print("Average Points played per game (PARS): ", averagePARS)
    print("Average Points played per game (English): ", averageEnglish)

timeTaken()
