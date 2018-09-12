from random import randint

# Parameters
upperLimit = 366 #366
testsper = 100  # where testsPer >=1


def main(upperlimit, testsper):
    results = [0 for x in range(upperlimit)]
    for j in range(upperlimit):
        sum = 0
        for k in range(testsper):
            match = testdays(generatearr(j))
            sum += match
        ratio = float(sum)/float(testsper)
        results[j] = ratio
    print(results)


def generatearr(numpeople):
    arr = [randint(1, 365)for _ in range(numpeople)]
    arr = sorted(arr)
    return arr


def testdays(arr):
    match = 0
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            match = 1
            break
    return match


if __name__ == '__main__':
    main(upperLimit, testsper)
