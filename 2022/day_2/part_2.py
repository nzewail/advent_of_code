import csv

scores = {
    "A": 1,
    "B": 2,
    "C": 3,
}
outcomes = {
    "X": 0,
    "Y": 3,
    "Z": 6,
}


def main():
    with open('day_2.txt', 'r') as f:
        reader = csv.reader(f, delimiter=" ")
        score = 0
        for row in reader:
            opp, you = row
            you_outcome = outcomes[you]
            opp_score = scores[opp]
            score += you_outcome
            if you_outcome == 3:
                score += opp_score
            elif you_outcome == 6:
                if opp_score == 1:
                    score += 2
                elif opp_score == 2:
                    score += 3
                elif opp_score == 3:
                    score += 1
            elif you_outcome == 0:
                if opp_score == 1:
                    score += 3
                elif opp_score == 2:
                    score += 1
                elif opp_score == 3:
                    score += 2
            print(score)
        print(score)


if __name__ == "__main__":
    main()
