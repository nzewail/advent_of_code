import csv


def main():
    with open('day_1.txt', 'r') as f:
        reader = csv.reader(f)
        calories_carried = []
        current_elf_calories = 0
        for row in reader:
            if not row:
                calories_carried.append(current_elf_calories)
                current_elf_calories = 0
            else:
                current_elf_calories += int(row[0])
        print(max(calories_carried))


if __name__ == "__main__":
    main()
