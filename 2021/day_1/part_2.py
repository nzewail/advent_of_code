def main():
    with open('day_1.txt', 'r') as f:
        increases = -1
        prev_3 = [0, 0, 0]
        cur_3 = []
        next_3 = []
        sec_next_3 = []
        for i, m in enumerate(f):
            measure = int(m.strip())
            cur_3.append(measure)
            if i > 0:
                next_3.append(measure)
            if i > 1:
                sec_next_3.append(measure)
            print(f"cur 3: {cur_3}")
            print(f"prev 3: {prev_3}")
            print(f"next 3: {next_3}")
            if len(prev_3) == 3 and len(cur_3) == 3:
                print(f"comparing {sum(prev_3)} to {sum(cur_3)}")
                if sum(cur_3) > sum(prev_3):
                    increases += 1
                prev_3 = cur_3.copy()
                cur_3 = next_3.copy()
                next_3 = sec_next_3.copy()
                sec_next_3 = []
        print(increases)


if __name__ == '__main__':
    main()
