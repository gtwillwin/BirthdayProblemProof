from random import randint


# Parameters
max_people_tested = 366
tests_per = 100  # where tests_per >= 1


def main():
    results = [0 for x in range(max_people_tested)]

    for j in range(max_people_tested):
        sum = 0

        for k in range(tests_per):
            match = test_days(generate_birthdays(j))
            sum += match

        ratio = float(sum) / float(tests_per)
        results[j] = ratio

    print(results)


def generate_birthdays(num_people):
    return sorted([randint(1, max_people_tested) for _ in range(num_people)])


def test_days(birthdays):
    match = 0

    for i in range(len(birthdays) - 1):
        if birthdays[i] == birthdays[i + 1]:
            match = 1
            break

    return match


if __name__ == '__main__':
    main()