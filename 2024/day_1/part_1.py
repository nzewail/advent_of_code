FILE_NAME = "input.txt"

def main():
    distance = 0
    with open(FILE_NAME, "r") as f:
        side_1 = []
        side_2 = []
        for row in f:
            row = row.strip().split("   ")
            side_1.append(int(row[0]))
            side_2.append(int(row[1]))
        sorted_side_1 = sorted(side_1)
        sorted_side_2 = sorted(side_2)
        for x, y in zip(sorted_side_1, sorted_side_2):
            distance += abs(x - y)
    print(distance)

if __name__ == "__main__":
    main()
