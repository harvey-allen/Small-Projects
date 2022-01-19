# Scientific Report- Squash Scoring methods
### Problem:
The problem set for investigation is to calculate, using simulation and suitable data, which scoring system is better for squash matches. To determine what defines better the criteria taken into account will involve weather a player of a higher ability wins more frequently in the game of squash using the PARS scoring system or the English method. Also, the relative affect the players abilities have on these methods. As well as touching upon the time efficiency of the matches for an audience.

### Method:
In order to simulate the problem a large scope of scenarios will be used with players of different abilities through the use of a CSV file, Player A will always have a higher ability however the difference in ability between the two players will vary. The games will be running through the English scoring system as well as the PARS method multiple times and the probability of the better player calculated. The results produced can then be used to produce a graphical representation of the data in order to determine the fairer method (where the better player has a higher probability of winning). This graph can then be analysed and thus a conclusion formed.

To calculate which scoring system is faster a series of random matches will be generated and then the points played calculated and averaged for each scoring system. If we assume that the time a point is taken to play is independent of the scoring system used whichever has the lowest average is the faster method.

#### The simulation process will run as follows:
1.	Individual player abilities are copied from a CSV file.
2.	Games are simulated for each scoring system multiple times.
3.	The probability of the better player winning for each match is calculated.
4.	A graph of the results is plotted against Player A’s Ability/ Player B’s Ability.

### Assumptions:
•	The player who starts the game serving is chose completely randomly each game and not pre-determined by the previous game played.

•	The match scoring system is not taken into account, for example the number of games in the match and the difference in games needed to win.

•	No external factors are taken into account that will affect the players performance on the day for example how much sleep they’ve had or what they have eaten. 

•	Each point averages out to take an equal amount of time to play.

### Results:
Results when calculating the average points played per game:
Average Points played per game (PARS):  15.371
Average Points played per game (English):  10.931

| Player A's Ability  | Player B's Ability | PARS Win Probability | English Win Probability |
| ------------- | ------------- | ----------- | ---------- |
| 74 | 26 | 0.98 | 0.98 |
| 70 | 30 | 1 | 0.99 |
| 66 | 34 | 0.94 | 0.98 |
| 62 | 38 | 0.88 | 0.91 |
| 58 | 42 | 0.77 | 0.79 |
| 54 | 46 | 0.66 | 0.71 |

### Conclusion:
The PARS scoring system is minorly superior as across a range of different skill levels, the player of higher ability almost always has a higher probability of winning throughout all the games simulated. Obviously with any randomly generated scenario it is possible to get some anomalies however these were able to mainly be negated though running the games a high amount of times. Another trend that became apparent in the graph is that the difference in probability each scoring system produced decreased as the difference in player ability became larger. This became clear after a similar pattern was observed in each test ran.

As proven by the results the English scoring system takes almost 2/3 of the time to play a game. Clearly despite the player only winning on points they serve on, playing to 9 had a drastic impact meaning the games consisted of far less points being played. This makes it far more appealing to an audience who want shorter, faster games.

Overall, the “better” scoring system is the English method depending on what criteria you rank in importance. The negligible difference in the fairness of the PARS system did not withstand over a range of player abilities and thus the shorter length of games the English method offers seems far more appealing for competitive squash matches.
