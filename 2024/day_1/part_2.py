from collections import defaultdict

FILE_NAME = "input.txt"

def main():
    sim_score = 0
    with open(FILE_NAME, "r") as file:
        counts = defaultdict(int)
        keys = []
        for row in file:
            row = row.strip().split("   ")
            keys.append(int(row[0]))
            counts[int(row[1])] += 1
    for k in keys:
        sim_score += k * counts[k]
    print(sim_score)
    

if __name__ == "__main__":
    main()