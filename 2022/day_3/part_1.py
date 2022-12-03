import csv
import re
import string


def main():
    with open('day_3.txt', 'r') as f:
        reader = csv.reader(f)
        total = 0
        for row in reader:
            items = row[0]
            num_items = len(items)
            num_items_per_rucksack = int(num_items / 2)
            first = items[:num_items_per_rucksack]
            second = items[num_items_per_rucksack:]
            shared_item = "".join({x for x in first if x in second})
            index = string.ascii_lowercase.index(shared_item.lower()) + 1
            if re.match("[a-z]", shared_item):
                total += index
            else:
                total += index + 26
        print(total)


if __name__ == "__main__":
    main()
