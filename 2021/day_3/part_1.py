from collections import defaultdict


def main():
    diagnostic_report = defaultdict(lambda: defaultdict(int))
    gamma = ""
    epsilon = ""

    with open('day_3.txt', 'r') as f:
        for row in f:
            for i, x in enumerate(row.strip()):
                diagnostic_report[i][x] += 1

    for index, value in diagnostic_report.items():
        gamma += max(value, key=value.get)
        epsilon += min(value, key=value.get)

    print(int(gamma, 2) * int(epsilon, 2))

if __name__ == '__main__':
    main()
