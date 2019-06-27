#!/usr/bin/env python3

# a recreation of a game in the British game show Countdown
# details: https://en.wikipedia.org/wiki/Countdown_(game_show)#Numbers_round
# summary: contestants pick six numbers and a random three digit target number is generated
# contestants then try to reach the target number through a sequential calculation
# using the chosen base six numbers and the operators +, -, *, /
# this program generates the target number based on a user input of
# how many 'small' (1-10) and 'large' (25, 50, 75, 100) numbers to include in the base six

import random

countList = []
countListTemp = ()
numCount = 0
totalNumCount = 6
newVal = 0
result = 0
operationRecord = []
smallNumbers = [1,2,3,4,5,6,7,8,9,10] * 2
largeNumbers = [25,50,75,100]

# requests user input 7 numbers
# calls generator1 which calls operation, generator 2, generatorAll
# returns to main after generatorAll completes and calls returnResult
# prints operationRecord to show user how result is derived
def main():
    global numCount, countList, totalNumCount, countListTemp, operationRecord
    baseSelector()
    countListTemp = tuple(countList)
    y = input('Hit Enter to get the target number. ')
    if y == '':
        generator1()
    else:
        while y!= '':
            y = input('Please hit Enter to get the target number.')
        generator1()
    while result > 999:
        countList = list(countListTemp)
        numCount = totalNumCount
        operationRecord = []
        print(f'restarted countList is {countList}')
        generator1()
    returnResult()
    z = input('Baffled? Hit Enter to see answer key. ')
    if z == '':
        print(' '.join(operationRecord), f' = {result}')
    else:
        while z!= '':
            z = input('Please hit Enter to see answer key.')
        print(' '.join(operationRecord), f' = {result}')
    print('Thank you for trying, at least.')
    rerun = input('Hit Enter if you have nothing better to do and want to try again. Hit Any Key + Enter to end.')
    if rerun == '':
        print('\n\n\n\n\n\n\n\n')
        globalReset()
        main()
    else:
        print('Go live your life then.')

def baseSelector():
    global smallNumbers, largeNumbers, numCount, countList
    print('Small numbers are 1 through 10 (two sets). \nLarge numbers are 25, 50, 75, 100.\nThese numbers are shuffled.')
    xSmall = int(input('How many small numbers would you like? '))
    xLarge = int(totalNumCount - xSmall)
    y = input(f'You will have {xLarge} large numbers. Hit Enter to proceed or Any Key + Enter to reselect. ')
    if y == '':
        for i in range(1, int(xSmall+1)):
            baseNumberIndex = random.randint(0,int(len(smallNumbers) - 1))
            baseNumber = smallNumbers[baseNumberIndex]
            countList.append(baseNumber)
            numCount += 1
            smallNumbers.remove(baseNumber)
        for i in range(1, int(xLarge+1)):
            baseNumberIndex = random.randint(0,int(len(largeNumbers) - 1))
            baseNumber = largeNumbers[baseNumberIndex]
            countList.append(baseNumber)
            numCount += 1
            largeNumbers.remove(baseNumber)
        print(f'Your base numbers are: {countList}')
    else: baseSelector()

# generator1: generate first number to populate result
def generator1():
    global numCount, countList, operationRecord, totalNumCount, result
    for x in countList:
        i1 = random.randint(0,totalNumCount-1)
        x = countList[i1] if x else generator1()
        result = x
        print(f'The first value is {result}')
        operationRecord.append(str(x))
        numCount -= 1
        countList.remove(x)
        print('The list is now: ', countList)
        generatorAll()
        break

# generatorAll: loops to pick 2nd, 3rd, 4th, 5th...nth value from list
# updates result till base list is empty
def generatorAll():
    global numCount, countList, newVal, result, operationRecord, totalNumCount
    for x in countList:
        if numCount <= int(totalNumCount-1) and numCount > 0:
            numCountIndex = int(int(numCount) - 1)
            i = random.randint(0,numCountIndex)
            print(f'i is {i}')
            x = countList[i]
            newVal = x
            print(f'newVal is now {newVal}')
            operator(result, newVal)
            operationRecord.append(str(newVal))
            numCount -= 1
            countList.remove(x)
            print(f'numCount is now {numCount}')
            print('The list is now: ', countList)
            generatorAll()

# operator generates random operations to perform on the new value generated
# checks that result is a positive integer; if not, performs operator again
def operator(z,zz):
    global result
    operateCode = random.randint(1,4)
    if operateCode == 1:
        result = int(z + zz)
        print(f'The result is now {z} + {zz} = {result}')
        operationRecord.append(' + ')
    elif operateCode == 2:
        if z - zz > 0:
            result = int(z - zz)
            print(f'The result is now {z} - {zz} = {result}')
            operationRecord.append(' - ')
        else:
            operator(z,zz)
    elif operateCode == 3:
        result = int(z * zz)
        print(f'The result is now {z} * {zz} = {result}')
        operationRecord.append(' * ')
    elif operateCode == 4:
        if z % zz == 0:
            result = int(z / zz)
            print(f'The result is now {z} / {zz} = {result}')
            operationRecord.append(' / ')
        else:
            operator(z,zz)

def returnResult():
    global result, countList, countListTemp
    print(f'\n\n\n\n\n\n\n\n\n\n\nYour set is {countListTemp}.\nThe target to achieve is {result}. Your 30s begins now.')
    
# Resets all objects to allow program to run again given user input to reset
def globalReset():
    global countList, countListTemp, operationRecord, smallNumbers, largeNumbers
    countList = []
    countListTemp = ()
    operationRecord = []
    smallNumbers = [1,2,3,4,5,6,7,8,9,10] * 2
    largeNumbers = [25,50,75,100]

if __name__ == '__main__': main()