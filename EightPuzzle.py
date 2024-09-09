"""
Written By Henry Odza
CaseID: hwo2
"""

import random
import sys
random.seed(0)


class Puzzle():
    def __init__(self, puzzle):
        self.puzzle = puzzle

    def move_up(self):
        index0 = self.puzzle.index(0)
        if index0 > 2:
            self.puzzle[index0], self.puzzle[index0 - 3] = self.puzzle[index0 - 3], self.puzzle[index0]
        
    def move_down(self):
        index0 = self.puzzle.index(0)
        if index0 < 6:
            self.puzzle[index0], self.puzzle[index0 + 3] = self.puzzle[index0 + 3], self.puzzle[index0]

    def move_left(self):
        index0 = self.puzzle.index(0)
        if index0 % 3 != 0:
            self.puzzle[index0], self.puzzle[index0 - 1] = self.puzzle[index0 - 1], self.puzzle[index0]
        
    def move_right(self):
        index0 = self.puzzle.index(0)
        if index0 % 3 != 2:
            self.puzzle[index0], self.puzzle[index0 + 1] = self.puzzle[index0 + 1], self.puzzle[index0]

    def scramble_state(self, n):
        self.puzzle = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        for _ in range(n):
            move = random.randint(0, 3)
            if move == 0:
                self.move_up()
            elif move == 1:
                self.move_down()
            elif move == 2:
                self.move_left()
            elif move == 3:
                self.move_right()

    
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
    if len(nums) == 9:
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
    return puzzle


def check_valid_puzzle(puzzle):
    possible = []
    if len(puzzle) != 9:
        return False
    for p in puzzle:
        if p < 0 or p > 8:
            return False
        if p not in possible:
            possible.append(p)
        else:
            return False

    return True


def print_puzzle(puzzle):
    print(f"{puzzle[0]} {puzzle[1]} {puzzle[2]}\n{puzzle[3]} {puzzle[4]} {puzzle[5]}\n{puzzle[6]} {puzzle[7]} {puzzle[8]}")




def execute_command(command, puzzle):
    if command == "":
        print("Thanks for playing!")
    elif command.startswith("setState"):
        temp = set_state(str(command)[8:])
        if len(temp) != 0:
            puzzle = temp
        print("New Puzzle State:")
        print_puzzle(puzzle)
    elif command == "printState":
        print("Current Puzzle State:")
        print_puzzle(puzzle)
    elif command.startswith("move"):
        flag = True
        if command == "move up":
            puzzle = move_up(puzzle)
            print("Moving Up...")
        elif command == "move down":
            puzzle = move_down(puzzle)
            print("Moving Down...")
        elif command == "move left":
            puzzle = move_left(puzzle)
            print("Moving Left...")
        elif command == "move right":
            puzzle = move_right(puzzle)
            print("Moving Right...")
        else:
            print(f"Error: Invalid Move: {command}")
            flag = False
        if flag:
            print("New Puzzle State:")
            print_puzzle(puzzle)
    elif command.startswith("scrambleState"):
        try:
            n = int(str(command)[14:])
            puzzle = scramble_state(puzzle, n)
            print("Scrambling...")
            print("New Puzzle State:")
            print_puzzle(puzzle)
        except ValueError:
            print(f"Error: Invalid Scramble Value, please enter \"scrambleValue n\" where n is an integer: {command}")
    elif command.startswith("#") or command.startswith("//"):
        pass
    else:
        print(f"Error: Invalid Command {command}")
    print()


def check_movable(puzzle):
    # Binary representation of possible moves, udlr, 1 is possible, 0 is not
    index0 = puzzle.index(0)
    if index0 == 0:
        return [0, 1, 0, 1]
    elif index0 == 1:
        return [0, 1, 1, 1]
    elif index0 == 2:
        return [0, 1, 1, 0]
    elif index0 == 3:
        return [1, 1, 0, 1]
    elif index0 == 4:
        return [1, 1, 1, 1]
    elif index0 == 5:
        return [1, 1, 1, 0]
    elif index0 == 6:
        return [1, 0, 0, 1]
    elif index0 == 7:
        return [1, 0, 1, 1]
    elif index0 == 8:
        return [1, 0, 1, 0]


def check_goal(puzzle):
    goal = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    return puzzle == goal


def DFS(puzzle, maxnodes):
    pass


def BFS(puzzle, maxnodes):
    visited = 0
    if check_goal(puzzle):
        return puzzle
    queue = [[puzzle,""]]
    while len(queue) > 0:
        current, pred = queue.pop(0)[0], queue.pop(0)[1]
        if check_goal(current):
            return current
        if visited < maxnodes:

            queue.extend([[move_left(current), pred+"l"], [move_right(current), pred+"r"], [move_up(current), pred+"u"], [move_down(current), pred+"d"]])
            visited += 4
    


if __name__ == "__main__":
    # Check for command line arguments, if file given, will execute commands from file
    if len(sys.argv) == 1:
        puzzle = startup()
        print("Starting Puzzle:")
        print_puzzle(puzzle)
        print()
        flag = True
        while flag:
            print("Enter a command or hit enter to exit")
            command = input()
            execute_command(command, puzzle)
                
    elif len(sys.argv) == 2:
        
        print(sys.argv[1])
        filename = sys.argv[1]
        if not filename.endswith(".txt"):
            print("Error: Please provide a .txt file.")
            sys.exit(1)
        puzzle = random_puzzle()
        print("Random Starting Puzzle:")
        print_puzzle(puzzle)
        print(f"Reading commands from file: {filename}")
        print("Executing Commands:\n")
        try:
            with open(filename, 'r') as file:
                commands = file.readlines()
            
            for command in commands:
                execute_command(command.strip(), puzzle)
        
        except FileNotFoundError:
            print(f"File {filename} not found.")
    else:
        print("Invalid input")
        sys.exit(1)
