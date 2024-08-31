import random
import sys


def startup():
    puzzle = []
    print("Welcome to the 8-puzzle solver.")
    check = True
    print("Please enter the starting state of the puzzle or hit enter to use a random puzzle")

    while check:
        start = input()
        if start == "":
            puzzle = random_puzzle()
            check = False
        else:
            puzzle = set_state(start)
            if len(puzzle) != 0:
                check = False
    return puzzle


def set_state(input):
    fail = False
    puzzle = []
    nums = input.split()
    if len(nums) == 10:
        for n in nums:
            if n.isdigit():
                puzzle.append(int(n))
            else:
                fail = True
    else:
        fail = True
    if not (check_valid_puzzle(puzzle)):
        fail = True
    if fail:
        print("Error Invalid Puzzle State: Please enter a puzzle with 9 unique digits between 0 and 9 sperated by spaces")
        return []
    return puzzle


def random_puzzle() -> list:
    puzzle = []
    possible = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    while len(possible) > 0:
        num = random.choice(possible)
        puzzle.append(num)
        possible.remove(num) 
    print("Using Random Puzzle: ")
    print_puzzle(puzzle)
    return puzzle


def check_valid_puzzle(puzzle):
    possible = []
    if len(puzzle) != 9:
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


def move_up(puzzle):
    index0 = puzzle.index(0)
    if index0 > 2:
        puzzle[index0], puzzle[index0 - 3] = puzzle[index0 - 3], puzzle[index0]
    return puzzle


def move_down(puzzle):
    index0 = puzzle.index(0)
    if index0 < 6:
        puzzle[index0], puzzle[index0 + 3] = puzzle[index0 + 3], puzzle[index0]
    return puzzle


def move_left(puzzle):
    index0 = puzzle.index(0)
    if index0 % 3 != 0:
        puzzle[index0], puzzle[index0 - 1] = puzzle[index0 - 1], puzzle[index0]
    return puzzle


def move_right(puzzle):
    index0 = puzzle.index(0)
    if index0 % 3 != 2:
        puzzle[index0], puzzle[index0 + 1] = puzzle[index0 + 1], puzzle[index0]
    return puzzle


if __name__ == "__main__":
    # Check for command line arguments, if file given, will execute commands from file
    if len(sys.argv) == 1:
        puzzle = startup()
        print("Starting Puzzle:")
        print_puzzle(puzzle)
        print("Enter a command to move the blank space: (u)p, (d)own, (l)eft, (r)ight")
        command = input()
        if command == "u":
            puzzle = move_up(puzzle)
        elif command == "d":
            puzzle = move_down(puzzle)
        print_puzzle(puzzle)
    elif len(sys.argv) == 2:
        print("Executing Commands:\n")
        # print_puzzle(sys.argv[1])
    else:
        print("Invalid input")
        sys.exit(1)
