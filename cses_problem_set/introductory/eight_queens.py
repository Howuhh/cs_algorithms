from pprint import pprint


def check_box(x, y, queens):

    for (x_q, y_q) in queens:
        if x_q == x or y_q == y or abs(x_q - x) == abs(y_q - y):
            return False

    return True


def count_queens(board):
    combs = []

    def _count(y, queens):
        if len(queens) == 8:
            combs.append(queens)
            return

        for i in range(8):
            if not board[i][y] or not check_box(i, y, queens):
                continue

            new_queens = queens + [(i, y)]
            _count(y + 1, new_queens)

    _count(0, [])
    return combs


def main():
    board = []

    for i in range(8):
        row = [True if s == "." else False for s in input()]

        board.append(row)

    combs = count_queens(board)
    print(len(combs))


if __name__ == "__main__":
    main()