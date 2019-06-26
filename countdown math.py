#!/usr/bin/env python3
import random

countList = []
numCount = 0
v1 = 0
v2 = 0
newVal = 0
result = 0
operationRecord = []

# requests user input 7 numbers
# calls generator1 which calls operation, generator 2, generatorAll
# returns to main after generatorAll completes and calls returnResult
# prints operationRecord to show user how result is derived
def main():
    global numCount
    global countList
    while numCount < 7:
        x = int(input('Give a number: '))
        countList.append(x)
        numCount += 1
    y = input('Hit "Enter" to proceed. ')
    if y == '':
        generator1()
    else:
        while y!= '':
            y = input('Please hit "Enter" to proceed.')
        generator1()
    returnResult()
    z = input('Hit "Enter" to see answer key. ')
    if z == '':
        print(' '.join(operationRecord), f' = {result}')
    else:
        while z!= '':
            z = input('Please hit "Enter" to see answer key.')
        print(' '.join(operationRecord), f' = {result}')

# generator1 and 2: generate first pair of numbers to populate result
def generator1():
    global numCount
    global countList
    global v1
    global operationRecord
    for x in countList:
        i1 = random.randint(0,6)
        x = countList[i1] if x else generator1()
        v1 = x
        print(f'The first value is {v1}')
        operationRecord.append(str(x))
        numCount -= 1
        countList.remove(x)
        generator2()
        print('The list is now: ', countList)
        break

def generator2():
    global numCount
    global countList
    global v2
    global result
    for x in countList:
        i2 = random.randint(0,5)
        x = countList[i2] if x else generator2()
        v2 = x
        print(f'The second value is {v2}')
        operator(v1,v2)
        operationRecord.append(str(x))
        numCount -= 1
        countList.remove(x)
        print('The list is now: ', countList)
        generatorAll()
        break

# generatorAll: loops to generate newVal and update result until user input list is empty
def generatorAll():
    global numCount
    global countList
    global newVal
    global result
    for x in countList:
        if numCount <= 5 and numCount > 0:
            numCountIndex = int(int(numCount) - 1)
            i = random.randint(0,numCountIndex)
            print(f'i is {i}')
            x = countList[i] if x else generatorAll()
            newVal = x
            print(f'newVal is now {newVal}')
            operator(result, newVal)
            operationRecord.append(str(newVal))
            numCount -= 1
            countList.remove(x)
            print(f'numCount is now {numCount}')
            print('The list is now: ', countList)
            generatorAll()

# operator generates random operations to perform on the newVal
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
    global result
    print(f'\n\n\n\n\n\n\n\n\n\n\nThe result to achieve is {result}.')

if __name__ == '__main__': main()