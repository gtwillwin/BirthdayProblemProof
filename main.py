from random import randint
from collections import Counter

# Parameters
upperLimit = 366
testsPer = 30  # where testsPer >=1


def main(upperLimit, testsPer):
    results = [0 for x in range(upperLimit)]
    for j in range(upperLimit):
        sum = 0
        for k in range(testsPer):
            match = testDays(generateArr(j))
            sum += match
        avg = sum/testsPer
        results[j] = avg
    print(results)


def generateArr(numPeople):
    arr = [randint(1, 365)for _ in range(numPeople)]
    arr = sorted(arr)
    return arr


def testDays(arr):
    match = 0
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            match = 1
            break
    return match


if __name__ == '__main__':
    main(upperLimit, testsPer)
