import numpy as np

def main():
    with open('sample.txt') as f:
        number_order = f.readline().strip().split(",")
        f.readline()

        board = []
        boards = []
        for row in f:
            if row != "\n":
                board.append(list(filter(lambda x: x != "", row.strip().split(" "))))
            else:
                boards.append(np.array(board))
                board = []

        for num in number_order:
            for b in boards:
                selection = np.where(b == num, b)



if __name__ == '__main__':
    main()
