#!/usr/bin/env python3

# Monte Carlo Simulation: Dice Game
# Based on Investopedia: Creating a Monte Carlo Simulation
# investopedia.com/articles/investing/093015/create-monte-carlo-simulation-using-excel.asp\
# Here's how the dice game rolls:
#   The player throws three dice that have 6 sides 3 times.
#   If the total of the 3 throws is 7 or 11, the player wins.
#   If the total of the 3 throws is: 3, 4, 5, 16, 17 or 18, the player loses.
#   If the total is any other outcome, the player plays again and re-rolls the dice.
#   When the player throws the dice again, the game continues in the same way, except
#       that the player wins when the total is equal to the sum determined in the first round.
#   5,000 results are needed to prepare the Monte Carlo simulation.

import random

class dice:
    def roll(self):
        return random.randint(1,6)

dice1 = dice()
dice2 = dice()
dice3 = dice()

win = [7,11]
lose = [3,4,5,16,17,18]
wins = 0
losses = 0
noresult = 0

def main():
    global wins, losses, noresult
    simulationRuns = 5000
    singleSimRolls = 50
    rollTimes = 1
    for i in range(simulationRuns):
        print(f'Simulation {i+1}:')
        if goRoll(singleSimRolls, 1) == 'reroll':
            threeRoll(singleSimRolls, 2)
            win.pop(-1)
    print(f'No of wins = {wins}')
    print(f'Probability of win = {(wins / simulationRuns * 100):.1f}%')
    print(f'No of losses = {losses}')
    print(f'Probability of loss = {(losses / simulationRuns * 100):.1f}%')
    print(f'No of incomplete = {noresult}')
    print(f'Probability of incomplete = {(noresult / simulationRuns * 100):.1f}%')

def goRoll(singleSimRolls, rollTimes):
    global wins, losses, noresult
    rollSum = dice1.roll() + dice2.roll() + dice3.roll()
    print(f'Roll {rollTimes}: {rollSum}')
    if rollCheck(rollSum) == 'reroll':
        win.append(rollSum)
        rollSum = 0
        return 'reroll'
    elif rollCheck(rollSum) == 'win':
        wins +=1
        print(f'Won by rolling {rollSum} after {rollTimes} rolls')
        return 'win'
    elif rollCheck(rollSum) == 'lose':
        losses += 1
        print(f'Lost by rolling {rollSum} after {rollTimes} rolls')
        return 'lose'
        
def threeRoll(singleSimRolls, rollTimes):
    global wins, losses, noresult
    if rollTimes <= singleSimRolls:
        rollSum = dice1.roll() + dice2.roll() + dice3.roll()
        print(f'Roll {rollTimes}: {rollSum}')
        if rollCheck(rollSum) == 'win':
            print(f'Won by rolling {rollSum} after {rollTimes} rolls')
            wins += 1
            return 'win'
        elif rollCheck(rollSum) == 'lose':
            print(f'Lost by rolling {rollSum} after {rollTimes} rolls')
            losses += 1
            return 'lose'
        elif rollCheck(rollSum) == 'reroll':
            threeRoll(singleSimRolls, rollTimes + 1)
    elif rollTimes > singleSimRolls:
        print(f'Did not win or lose after {rollTimes} rolls')
        noresult += 1
        return 'noresult'

def rollCheck(rollSum = 0):
    global win, lose
    if rollSum in win:
        return 'win'
    elif rollSum in lose:
        return 'lose'
    else:
        return 'reroll'

if __name__ == '__main__': main()