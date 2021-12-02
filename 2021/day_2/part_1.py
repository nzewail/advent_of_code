def main():
    horizontal = 0
    depth = 0

    with open('day_2.txt', 'r') as f:
        for direction in f:
            pos, mag = direction.strip().split(" ")
            magnitude = int(mag)
            if pos == "forward":
                horizontal += magnitude
            if pos == "down":
                depth += magnitude
            if pos == "up":
                depth += magnitude * -1
        print(horizontal * depth)


if __name__ == '__main__':
    main()
