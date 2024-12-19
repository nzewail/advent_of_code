import re

INPUT_FILE = "input.txt"
REGEX = r"mul\(\d+,\d+\)"


def main():
    sum = 0
    with open(INPUT_FILE, "r") as f:
        input = f.read()
        matches = re.findall(REGEX, input)
        for match in matches:
            nums = re.findall(r"\d+", match)
            sum += int(nums[0]) * int(nums[1])
        print(sum)


if __name__ == "__main__":
    main()
