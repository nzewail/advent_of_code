import csv

scores = {
    "A": 1,
    "B": 2,
    "C": 3,
    "X": 1,
    "Y": 2,
    "Z": 3,
}


def main():
    with open('day_2.txt', 'r') as f:
        reader = csv.reader(f, delimiter=" ")
        score = 0
        for row in reader:
            opp, you = row
            you_score = scores[you]
            opp_score = scores[opp]
            score += you_score
            if you_score == opp_score:
                score += 3
            elif abs(you_score - opp_score) == 1 and you_score > opp_score:
                score += 6
            elif abs(you_score - opp_score) == 2 and you_score < opp_score:
                score += 6
        print(score)


if __name__ == "__main__":
    main()
