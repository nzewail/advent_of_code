from collections import Counter, defaultdict

def find_bit(bits, keep_zero):
    bit_length = len(bits[0])
    for i in range(bit_length):
        c = Counter(map(lambda x: x[i], bits))
        print(c)

        if len(set(c.values())) == 1:
            if keep_zero:
                index = "0"
            else:
                index = "1"
        else:
            most_common = c.most_common(1)[0][0]
            if most_common == "1" and keep_zero == False:
                index = "1"
            elif most_common == "0" and keep_zero == False:
                index = "0"
            elif most_common == "1" and keep_zero == True:
                index = "0"
            elif most_common == "0" and keep_zero == True:
                index = "1"

        if len(bits) > 1:
            bits = list(filter(lambda x: x[i] == index, bits))
            print(bits)
    return bits[0]


def main():
    diagnostic_report = defaultdict(lambda: defaultdict(int))

    bits = []

    with open('day_3.txt', 'r') as f:
        for row in f:
            bits.append(row.strip())

    ox_bits = bits.copy()
    co2_bits = bits.copy()

    ox = find_bit(ox_bits, False)
    co2 = find_bit(co2_bits, True)

    print(int(co2, 2) * int(ox, 2))

if __name__ == '__main__':
    main()
