from random import randint
from collections import Counter


# Parameters - mainly to be used in future version
min = 0
max = 366
testsPer = 30
numPeople = 23


def generateArr(low, high, numPeople):
    arr = [randint(1, 365)for _ in range(numPeople)]
    arr = sorted(arr)
    return arr


def runTest(arr):
    match = False
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            match = True
            break
    print(match)


arr = generateArr(low, high, numPer)
runTest(arr)
