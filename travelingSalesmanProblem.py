#!/usr/bin/env python3

# The traveling salesman problem v1: brute force method
# Given a number of cities, incl start point
# A salesman must calculate the shortest route to go through all cities and return to start
# This program generates n cities randomly with x,y coords = [0,1)

import random
import math
from itertools import permutations

cityCount = int(input('How many cities to travel to? '))

class City:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

homeName = None
homeX = 0
homeY = 0
homeCity = City(homeName, homeX, homeY)

cityDict = {}
pathDict = {}

def main():
    cityGenerator()
    pathGenerator()
    distCompare()

# generates a dict of cities and x, y values for each and prints dict
def cityGenerator():
    global homeCity, homeName, homeX, homeY
    for i in range(1,int(cityCount+1)):
        x = random.random()
        y = random.random()
        name = i
        cityObj = City(name, x, y)
        cityDict.update({name: [x, y]})
    # randomly determines start (home) city, prints it and removes from dict
    homeIndex = random.randint(1, cityCount)
    homeName = homeIndex
    [homeX, homeY] = cityDict.get(homeIndex)
    homeCity = City(homeName, homeX, homeY)
    print(f'The home city is city no.{homeCity.name}')
    print(f'Its x coord is {homeCity.x}, and y coord is {homeCity.y}')
    del cityDict[homeName]
    print(f'The remaining cities are {cityDict}')

# generates all possible paths using permutation of no. of cities chosen
def pathGenerator():
    global homeName, homeX, homeY
    # permutate the dict of cities without home city
    pathPerm = permutations(cityDict)
    permList = list(pathPerm)
    # replace home city in dict of cities
    cityDict.update({homeName: [homeX, homeY]})
    for perm in permList:
        name = permList.index(perm) + 1
        cityPath = list(perm)
        # add home city to beginning and end of permutated path that excludes home city
        cityPath.insert(0, homeName)
        cityPath.append(homeName)
        print(f'Path no.{name} is {cityPath}')
        pathDist = 0
        for thisCityKey in cityPath:
            thisCityIndex = cityPath.index(thisCityKey)
            nextCityKey = cityPath[int(thisCityIndex + 1)]
            [thisCityX, thisCityY] = cityDict.get(thisCityKey)
            [nextCityX, nextCityY] = cityDict.get(nextCityKey)
            nextDistance = math.sqrt((nextCityX - thisCityX)**2 + (nextCityY - thisCityY)**2)
            # print(f'The distance from city {thisCityKey} to city {nextCityKey} is {nextDistance}')
            pathDist = pathDist + nextDistance
        print(f'The total path distance is {pathDist}')
        pathDict.update({pathDist: cityPath})

def distCompare():
    distCompare = []
    for pathDist in pathDict:
        distCompare.append(pathDist)
    distCompare.sort()
    print(f'The possible distances are {distCompare}')
    minDist = min(distCompare)
    print(f'Minimum distance is {minDist}')
    bestPath = pathDict.get(minDist)
    print(f'The best path is {bestPath}')

if __name__ == '__main__': main()
