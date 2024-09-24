"""
Written By Henry Odza
CaseID: hwo2
"""

import random
import sys
import heapq

random.seed(10)


class Puzzle():
    def __init__(self, puzzle):
        self.set_state(puzzle)

    def list_form(self):
        puzzle = ""
        for i in self.puzzle:
            puzzle += str(i) + " "
        return puzzle
    
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
        # self.print_puzzle()
        for _ in range(n):
            move = random.choice(self.check_moveable())

            if move == 0:
                # print("Moving Up...")
                self.move_up()
            elif move == 1:
                # print("Moving Down...")
                self.move_down()
            elif move == 2:
                # print("Moving Left...")
                self.move_left()
            elif move == 3:
                # print("Moving Right...")
                self.move_right()
            # self.print_puzzle()
    
    def print_puzzle(self):
        print(f"{self.puzzle[0]} {self.puzzle[1]} {self.puzzle[2]}\n{self.puzzle[3]} {self.puzzle[4]} {self.puzzle[5]}\n{self.puzzle[6]} {self.puzzle[7]} {self.puzzle[8]}")
    
    def set_state(self, input):
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
        if not (self.check_valid_puzzle(puzzle)):
            fail = True
        if fail:
            print("Error Invalid Puzzle State: Please enter a puzzle with 9 unique digits between 0 and 9 sperated by spaces")
            return 0
        self.puzzle = puzzle
        return 1

    def check_valid_puzzle(self, puzzle):
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
    
    def check_moveable(self):
        # 0 means up is possible, 1 means down is possible, 2 means left is possible, 3 means right is possible
        # Binary representation of possible moves, udlr, 1 is possible, 0 is not
        index0 = self.puzzle.index(0)
        if index0 == 0:
            return [1, 3]
        elif index0 == 1:
            return [1, 2, 3]
        elif index0 == 2:
            return [1, 2]
        elif index0 == 3:
            return [0, 1, 3]
        elif index0 == 4:
            return [0, 1, 2, 3]
        elif index0 == 5:
            return [0, 1, 2]
        elif index0 == 6:
            return [0, 3]
        elif index0 == 7:
            return [0, 2, 3]
        elif index0 == 8:
            return [0, 3]
        
    def check_goal(self):
        goal = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        return self.puzzle == goal
    
    def BFS(self, maxnodes):
        nodes = 1
        # if self.check_goal():
        #     return [nodes, 0, []]
        queue = [[self, ""]]
        while len(queue) > 0 and nodes <= maxnodes:
            # print("Issure might be that it is not splitting the current and prev_moves correctly")
            current, prev_moves = queue.pop(0)
            if current.check_goal():
                return [nodes, len(prev_moves), prev_moves]
            move = current.check_moveable()
            if 2 in move:
                new_puzzle = Puzzle(current.list_form())
                new_puzzle.move_left()
                queue.append([new_puzzle, prev_moves + "l"])
                nodes += 1
            
            if 3 in move:
                new_puzzle = Puzzle(current.list_form())
                new_puzzle.move_right()
                queue.append([new_puzzle, prev_moves + "r"])
                nodes += 1

            if 0 in move:
                new_puzzle = Puzzle(current.list_form())
                new_puzzle.move_up()
                queue.append([new_puzzle, prev_moves + "u"])
                nodes += 1
            
            if 1 in move:
                new_puzzle = Puzzle(current.list_form())
                new_puzzle.move_down()
                queue.append([new_puzzle, prev_moves + "d"])
                nodes += 1
        return -1
    
    def OldDFS(self, maxnodes):
        nodes = 1
        stack = [[self, ""]]
        while len(stack) > 0 and nodes <= maxnodes:
            current, prev_moves = stack.pop()
            # print(f"Current: {current.list_form()}, prev_moves: {prev_moves}")
            if current.check_goal():
                return [nodes, len(prev_moves), prev_moves]
            move = current.check_moveable()

            if 1 in move:
                new_puzzle = Puzzle(current.list_form())
                new_puzzle.move_down()
                stack.append([new_puzzle, prev_moves + "d"])
                nodes += 1

            if 0 in move:
                new_puzzle = Puzzle(current.list_form())
                new_puzzle.move_up()
                stack.append([new_puzzle, prev_moves + "u"])
                nodes += 1
            
            if 3 in move:
                new_puzzle = Puzzle(current.list_form())
                new_puzzle.move_right()
                stack.append([new_puzzle, prev_moves + "r"])
                nodes += 1

            if 2 in move:
                new_puzzle = Puzzle(current.list_form())
                new_puzzle.move_left()
                stack.append([new_puzzle, prev_moves + "l"])
                nodes += 1
            
        return -1
    
    def DFS(self, maxnodes):
        nodes = 1
        stack = [[self, ""]]
        visited = set()
        visited.add(self.list_form())
        while len(stack) > 0 and nodes <= maxnodes:
            current, prev_moves = stack.pop()
            if current.check_goal():
                return [nodes, len(prev_moves), prev_moves]
            move = current.check_moveable()
            if 1 in move:
                new_puzzle = Puzzle(current.list_form())
                new_puzzle.move_down()
                if new_puzzle.list_form() not in visited:
                    stack.append([new_puzzle, prev_moves + "d"])
                    visited.add(new_puzzle.list_form())
                    nodes += 1

            if 0 in move:
                new_puzzle = Puzzle(current.list_form())
                new_puzzle.move_up()
                if new_puzzle.list_form() not in visited:
                    stack.append([new_puzzle, prev_moves + "u"])
                    visited.add(new_puzzle.list_form())
                    nodes += 1
            
            if 3 in move:
                new_puzzle = Puzzle(current.list_form())
                new_puzzle.move_right()
                if new_puzzle.list_form() not in visited:
                    stack.append([new_puzzle, prev_moves + "r"])
                    visited.add(new_puzzle.list_form())
                    nodes += 1

            if 2 in move:
                new_puzzle = Puzzle(current.list_form())
                new_puzzle.move_left()
                if new_puzzle.list_form() not in visited:
                    stack.append([new_puzzle, prev_moves + "l"])
                    visited.add(new_puzzle.list_form())
                    nodes += 1
        return -1

    def h1(self):
        # Heuristic 1: Counts the number of misplaced tiles compared to the goal state.
        # The heuristic ignores the empty tile (0).    
        goal = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        return sum([1 for i in range(9) if self.puzzle[i] != goal[i] and self.puzzle[i] != 0])

    def h2(self):
        # Heuristic 2: Calculates the sum of the Manhattan distances of the tiles from their goal positions.
        # The heuristic ignores the empty tile (0).
        # This uses integer division to calculate the row, and modulo to calculate the column.
        goal = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        return sum([abs(i // 3 - goal.index(self.puzzle[i]) // 3) + abs(i % 3 - goal.index(self.puzzle[i]) % 3) for i in range(9) if self.puzzle[i] != 0])
    
    def heuristic(self, h):
        if h == 1:
            return self.h1()
        elif h == 2:
            return self.h2()
        else:
            return -1

    def A_star(self, heuristic, maxnodes):
        # A* Search Algorithm using the given heuristic function.
        # The heuristic function is passed as an argument.
        nodes = 1
        # if self.check_goal():
        #     return [nodes, 0, []]
        states = set()
        states.add(self.list_form())
        queue = []
        counter = 0
        heapq.heappush(queue, (self.heuristic(heuristic), counter, self, ""))
        while len(queue) > 0 and nodes <= maxnodes:
            f, c, current, prev_moves = heapq.heappop(queue)
            if current.check_goal():
                return [nodes, len(prev_moves), prev_moves]
            move = current.check_moveable()
            if 2 in move:
                new_puzzle = Puzzle(current.list_form())
                new_puzzle.move_left()
                if new_puzzle.list_form() not in states:
                    heapq.heappush(queue, (new_puzzle.heuristic(heuristic) + len(prev_moves) + 1, counter, new_puzzle, prev_moves + "l"))
                    states.add(new_puzzle.list_form())
                    nodes += 1            
                    counter += 1
            if 3 in move:
                new_puzzle = Puzzle(current.list_form())
                new_puzzle.move_right()
                if new_puzzle.list_form() not in states:
                    heapq.heappush(queue, (new_puzzle.heuristic(heuristic) + len(prev_moves) + 1, counter, new_puzzle, prev_moves + "r"))
                    states.add(new_puzzle.list_form())
                    nodes += 1
                    counter += 1

            if 0 in move:
                new_puzzle = Puzzle(current.list_form())
                new_puzzle.move_up()
                if new_puzzle.list_form() not in states:
                    heapq.heappush(queue, (new_puzzle.heuristic(heuristic) + len(prev_moves) + 1, counter, new_puzzle, prev_moves + "u"))
                    states.add(new_puzzle.list_form())
                    nodes += 1
                    counter += 1
            
            if 1 in move:
                new_puzzle = Puzzle(current.list_form())
                new_puzzle.move_down()
                if new_puzzle.list_form() not in states:
                    heapq.heappush(queue, (new_puzzle.heuristic(heuristic) + len(prev_moves) + 1, counter, new_puzzle, prev_moves + "d"))
                    states.add(new_puzzle.list_form())
                    nodes += 1
                    counter += 1
        return -1
    
    def branching_factor(self, depth, nodes, tolerance, max_iterations):
        b = 2.0 
        for _ in range(max_iterations):
            try:
                estimate = (1-b**(depth+1))/(1-b) - 1 - nodes
            except OverflowError:
                return -1
            if abs(estimate) < tolerance:
                return b
            try:
                b -= estimate/(((depth*b-depth-1)*(b**depth)+1)/((b-1)**2))
            except ZeroDivisionError:
                return -1
        print("Error: Max Iterations Reached")
        return -1
    
    def execute_command(self, command):
        if command == "":
            return 0
        elif command.startswith("setState"):
            state = self.set_state(str(command)[8:])
            if state == 1:
                print("Setting Puzzle State...")
                print("New Puzzle State:")
                self.print_puzzle()
        elif command == "printState":
            print("Current Puzzle State:")
            self.print_puzzle()
        elif command.startswith("move"):
            flag = True
            if command == "move up":
                self.move_up()
                print("Moving Up...")
            elif command == "move down":
                self.move_down()
                print("Moving Down...")
            elif command == "move left":
                self.move_left()
                print("Moving Left...")
            elif command == "move right":
                self.move_right()
                print("Moving Right...")
            else:
                print(f"Error: Invalid Move: {command}")
                flag = False
            if flag:
                print("New Puzzle State:")
                self.print_puzzle()
        elif command.startswith("scrambleState"):
            try:
                n = int(str(command)[14:])
                print("Scrambling...")
                self.scramble_state(n)
                print("New Puzzle State:")
                self.print_puzzle()
            except ValueError:
                print(f"Error: Invalid Scramble Value, please enter \"scrambleValue n\" where n is an integer: {command}")
        elif command.startswith("#") or command.startswith("//"):
            print(f"Comment: {command}")
        elif command.startswith("solve"):
            if command[6:].startswith("A*"):
                maxnodes = 1000
                try:
                    maxnodes = int(command[12:])
                except ValueError:
                    if len(command) > 9:
                        print("Error: Invalid Max Nodes Value. Using Default Value of 1000")
                if command[9:].startswith("h1"):
                    print("Solving using A* with Heuristic 1...")
                    result = self.A_star(1, maxnodes=maxnodes)
                    if result == -1:
                        print(f"Error: Max Nodes limit({maxnodes}) Reached")
                    else:
                        print(f"Nodes expanded: {result[0]}")
                        print(f"Solution Length: {result[1]}")
                        print("Move Sequence:")
                        for move in result[2]:
                            if move == "u":
                                print("Move Up")
                            elif move == "d":
                                print("Move Down")
                            elif move == "l":
                                print("Move Left")
                            elif move == "r":
                                print("Move Right")
                elif command[9:].startswith("h2"):
                    print("Solving using A* with Heuristic 2...")
                    result = self.A_star(2, maxnodes=maxnodes)
                    if result == -1:
                        print(f"Error: Max Nodes limit({maxnodes}) Reached")
                    else:
                        print(f"Nodes expanded: {result[0]}")
                        print(f"Solution Length: {result[1]}")
                        print("Move Sequence:")
                        for move in result[2]:
                            if move == "u":
                                print("Move Up")
                            elif move == "d":
                                print("Move Down")
                            elif move == "l":
                                print("Move Left")
                            elif move == "r":
                                print("Move Right")
                else:
                    print(f"Error: Invalid Heuristic Value: {command}")
            elif command[6:].startswith("BFS"):
                maxnodes = 1000
                try:
                    maxnodes = int(command[10:])
                except ValueError:
                    if len(command) > 9:
                        print("Error: Invalid Max Nodes Value. Using Default Value of 1000")
                print("Solving using BFS...")
                result = self.BFS(maxnodes)
                if result == -1:
                    print(f"Error: Max Nodes limit({maxnodes}) Reached")
                else:
                    print(f"Nodes expanded: {result[0]}")
                    print(f"Solution Length: {result[1]}")
                    print("Move Sequence:")
                    for move in result[2]:
                        if move == "u":
                            print("Move Up")
                        elif move == "d":
                            print("Move Down")
                        elif move == "l":
                            print("Move Left")
                        elif move == "r":
                            print("Move Right")
            elif command[6:].startswith("DFS"):
                maxnodes = 1000
                try:
                    maxnodes = int(command[10:])
                except ValueError:
                    if len(command) > 9:
                        print("Error: Invalid Max Nodes Value. Using Default Value of 1000")
                print("Solving using DFS...")
                result = self.DFS(maxnodes)
                if result == -1:
                    print(f"Error: Max Nodes limit({maxnodes}) Reached")
                else:
                    print(f"Nodes expanded: {result[0]}")
                    print(f"Solution Length: {result[1]}")
                    print("Move Sequence:")
                    for move in result[2]:
                        if move == "u":
                            print("Move Up")
                        elif move == "d":
                            print("Move Down")
                        elif move == "l":
                            print("Move Left")
                        elif move == "r":
                            print("Move Right")
            else: 
                print(f"Error: Invalid Solve Command: {command}")
        elif command.startswith("heuristic"):
            if command[10:] == "h1":
                print(f"Heuristic 1: {self.h1()}")
            elif command[10:] == "h2":
                print(f"Heuristic 2: {self.h2()}")
            else:
                print(f"Error: Invalid Heuristic Command: {command}")
        elif command.startswith("branchingFactor"):
            split = command.split()
            depth = 10
            nodes = 100
            tolerance = 0.01
            max_iterations = 1000
            try:
                depth = int(split[1])
                nodes = int(split[2])
                tolerance = float(split[3])
                max_iterations = int(split[4])
            except ValueError:
                if len(command) > 14:
                    print("Error: Invalid Parameters. Using Default Values")
            print(f"Branching Factor: {self.branching_factor(depth, nodes, tolerance, max_iterations)}")
        else:
            print(f"Error: Invalid Command {command}")
        print()
        return 1


def branch(acceptable_d, maxnodes, tolerance, max_iterations):
    good = []
    for i in range(6, 500):
        puzzle = Puzzle("0 1 2 3 4 5 6 7 8")
        puzzle.scramble_state(i)
        bfs = puzzle.BFS(maxnodes)
        dfs = puzzle.DFS(maxnodes)
        a1 = puzzle.A_star(1, maxnodes)
        a2 = puzzle.A_star(2, maxnodes)
        if bfs != -1:
            branch = puzzle.branching_factor(bfs[1], bfs[0], tolerance, max_iterations)
            if branch != -1:
                # print("BFS", bfs[1], bfs[0], branch)
                if bfs[1] in acceptable_d:
                    print("BFS", bfs[1], bfs[0], branch)
                    good.append(["BFS", bfs[1], bfs[0], branch])
        if dfs != -1:
            branch = puzzle.branching_factor(dfs[1], dfs[0], tolerance, max_iterations)
            if branch != -1:
                if dfs[1] in acceptable_d:
                    print("DFS", dfs[1], dfs[0], branch)
                    good.append(["DFS", dfs[1], dfs[0], branch])
        if a1 != -1:
            branch = puzzle.branching_factor(a1[1], a1[0], tolerance, max_iterations)
            if branch != -1:
                if a1[1] in acceptable_d:
                    print("A* h1", a1[1], a1[0], branch)
                    good.append(["a1", a1[1], a1[0], branch])
                    # puzzle.print_puzzle()
        if a2 != -1:
            branch = puzzle.branching_factor(a2[1], a2[0], tolerance, max_iterations)
            if branch != -1:
                if a2[1] in acceptable_d:
                    print("A* h2", a2[1], a2[0], branch)
                    good.append(["a2", a2[1], a2[0], branch])
    return good


def random_puzzle() -> list:
    puzzle = ""
    possible = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    while len(possible) > 0:
        num = random.choice(possible)
        puzzle += str(num) + " "
        possible.remove(num) 
    return puzzle
    

if __name__ == "__main__":
    # Check for command line arguments, if file given, will execute commands from file
    if len(sys.argv) == 1:
        print("Welcome to the 8-puzzle solver.")
        start = input("Please enter the starting state of the puzzle or hit enter to use a random puzzle: ")
        scramble = False
        if start == "":
            scramble = True
            start = random_puzzle()
        puzzle = Puzzle(start)
        if scramble:
            puzzle.scramble_state(10)
        print("Starting Puzzle:")
        puzzle.print_puzzle()
        print()
        flag = True
        while flag:
            command = input("Enter a command or hit enter to exit: ")
            if command.startswith("branch"):
                acceptable = [2,4,6,8,10,12]
                branch(acceptable, 5000, 0.01, 10000)
                pass
            else:
                state = puzzle.execute_command(command)
                if state == 0:
                    flag = False
                
    elif len(sys.argv) == 2:
        
        print(sys.argv[1])
        filename = sys.argv[1]
        if not filename.endswith(".txt"):
            print("Error: Please provide a .txt file.")
            sys.exit(1)
        random_p = random_puzzle()
        puzzle = Puzzle(random_p)
        print("Random Starting Puzzle:")
        puzzle.print_puzzle()
        print(f"Reading commands from file: {filename}")
        try:
            with open(filename, 'r') as file:
                commands = file.readlines()
            with open("output.txt", 'w') as file:
                file.write("Henry Odza\n")
                for command in commands:
                    command = command.strip()
                    print(f"Using Command: {command}")
                    puzzle.execute_command(command)
                    sys.stdout = file
                    print(f"Using Command: {command}")
                    puzzle.execute_command(command)
                    sys.stdout = sys.__stdout__
        
            print("Command output can be found in output.txt")
        except FileNotFoundError:
            print(f"File {filename} not found.")
    else:
        print("Invalid input")
        sys.exit(1)
