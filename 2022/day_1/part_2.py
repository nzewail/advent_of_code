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
        calories_carried.append(current_elf_calories)
        top_3 = sorted(calories_carried, reverse=True)[:3]
        print(sum(top_3))


if __name__ == "__main__":
    main()
