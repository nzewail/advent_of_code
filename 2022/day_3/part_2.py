import csv
import re
import string


def main():
    with open('day_3.txt', 'r') as f:
        reader = csv.reader(f)
        total = 0
        group = []
        for row in reader:
            items = row[0]
            group.append(items)
            if len(group) == 3:
                shared_item = "".join({x for x in group[0] if x in group[1] and x in group[2]})
                index = string.ascii_lowercase.index(shared_item.lower()) + 1
                if re.match("[a-z]", shared_item):
                    total += index
                else:
                    total += index + 26
                group = []
        print(total)


if __name__ == "__main__":
    main()
