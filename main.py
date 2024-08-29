import random
import sys


def startup():
    puzzle = []
    print("Welcome to the 8-puzzle solver.")
    check = True
    print("Please enter the starting state of the puzzle or hit enter to use a random puzzle")
    while check:
        fail = False
        start = input()
        if start == "":
            puzzle = random_puzzle()
            check = False
        else:
            nums = start.split()
            if len(nums) == 10:
                for n in nums:
                    if n.isdigit():
                        puzzle.append(int(n))
                    else:
                        fail = True
            if check_valid_puzzle(puzzle):
                check = False
            else:
                fail = True
        if fail:
            print("Invalid puzzle: Please enter a puzzle with 9 unique digits between 0 and 9 sperated by spaces:")
    return puzzle


def random_puzzle() -> list:
    puzzle = []
    possible = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    while len(possible) > 0:
        num = random.choice(possible)
        puzzle.append(num)
        possible.remove(num) 
    return puzzle


def check_valid_puzzle(puzzle):
    possible = []
    if len(puzzle) != 10:
        return False
    for p in puzzle:
        if p < 0 or p > 9:
            return False
        if p not in possible:
            possible.append(p)
        else:
            return False

    return True


def print_puzzle(puzzle):
    print(f"{puzzle[0]} {puzzle[1]} {puzzle[2]}\n{puzzle[3]} {puzzle[4]} {puzzle[5]}\n{puzzle[6]} {puzzle[7]} {puzzle[8]}")


if __name__ == "__main__":
    # Check for command line arguments, if file given, will execute commands from file
    if len(sys.argv) == 1:
        puzzle = startup()
        print("Starting Puzzle:\n")
        print_puzzle(puzzle)
    if len(sys.argv) == 2:
        print("Executing Commands:\n")
        # print_puzzle(sys.argv[1])
    else:
        print("Invalid input")
        sys.exit(1)
