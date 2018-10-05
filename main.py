from random import randint
import matplotlib.pyplot as plt
import numpy as np


# Parameters
max_people = 100
tests_per = 1000  # where tests_per >= 1


def main():
    results = np.arange(0, max_people, dtype=float)

    for j in range(max_people):
        sum = 0

        for k in range(tests_per):
            match = test_days(generate_birthdays(j))
            sum += match

        ratio = float(sum) / float(tests_per)
        results[j] = ratio
    print(results)
    graph(results, my_formula)


def generate_birthdays(num_people):
    return sorted([randint(1, max_people) for _ in range(num_people)])


def test_days(birthdays):
    match = 0

    for i in range(len(birthdays) - 1):
        if birthdays[i] == birthdays[i + 1]:
            match = 1
            break

    return match


def graph(results, formula):
    plt.plot(results, label="actual")

    x = np.array(range(0, 100))
    y = formula(x)
    plt.plot(y, label="theoretical")


    plt.xlabel("People in room")
    plt.ylabel("Percentage of tests with birthday match")
    plt.xlim(0, 100)
    plt.ylim(0, 1)
    plt.legend()
    plt.show()


def my_formula(x):
    return 1 - np.e**(-(x * x) / 730)


if __name__ == '__main__':
    main()
