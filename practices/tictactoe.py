import argparse

def main():
    values = create_board()
    print_board(values)

def create_board():
    values = [2, 0, 1, 0, 0, 2, 0, 0, 0]
    return values

def print_board(values):
    for row in range(3):
        row_str = " "
        for col in range(3):
            i = row * 3 + col
            if values[i] == 0:
                row_str += " "
            elif values[i] == 1:
                row_str += "X"
            elif values[i] == 2:
                row_str += "O"
            if col < 2:
                row_str += "|"
        print(row_str)
        if row < 2:
            print("-------")


if __name__ == '__main__':
    """parser = argparse.ArgumentParser()
    parser.add_argument("numbers", type=int, help="Move to make")
    args = parser.parse_args()"""
    main()