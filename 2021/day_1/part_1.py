def main():
    with open('day_1.txt', 'r') as f:
        prev = 0
        increases = -1
        for i in f:
            measure = int(i.strip())
            if measure > prev:
                print(f"{measure} is larger than {prev}")
                increases += 1
            prev = measure
        print(increases)


if __name__ == '__main__':
    main()
