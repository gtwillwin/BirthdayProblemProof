from random import randint
import matplotlib.pyplot as plt
import numpy as np


# Parameters
max_people = 100
tests_per = 5001  # where tests_per >= 1


def main():
    results = np.zeros((tests_per, max_people), dtype=float)

    for j in range(max_people):
        sum = 0

        for k in range(1, tests_per):
            match = test_days(generate_birthdays(j))
            sum += match
            results[k, j] = sum/k

    graph(results, my_formula, 100) #


def generate_birthdays(num_people):
    return sorted([randint(1, 365) for _ in range(num_people)])


def test_days(birthdays):
    match = 0

    for i in range(len(birthdays) - 1):
        if birthdays[i] == birthdays[i + 1]:
            match = 1
            break

    return match


def graph(results, formula, dif):
    i = 0
    while i < tests_per:
        if i % dif == 0:
            plt.plot(results[i], label="experimental")

            x = np.array(range(0, 100))
            y = formula(x)
            plt.plot(y, label="theoretical")

            plt.xlabel("Number of people")
            plt.ylabel("Tests with birthday match")
            plt.xlim(0, 100)
            plt.ylim(0, 1)
            plt.legend()
            plt.title("Birthday Problem Theoretical Probability vs Empirical Test")
            plt.text(80, 0.83, "Tests run: ", horizontalalignment='center', verticalalignment='center')
            plt.text(90, 0.83, i, horizontalalignment='center', verticalalignment='center')
            name = str(i)+".png"
            plt.savefig(name)
            plt.show()

        i += 1


def my_formula(x):
    return 1 - np.e**(-(x * x) / 730)


if __name__ == '__main__':
    main()