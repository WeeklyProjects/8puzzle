# 8puzzle
Hello! Welcome to my code. 
All of the python code is located in EightPuzzle.py

# Running the Code

## Command Line
To run the program with commands from the command line type "python EightPuzzle.py" (Note: you might need to type py or python3 depending on your computer. Additionally this assumes that you are in the 8Puzzle directory, if you are not you will need to include the file path of EightPuzzle.py in the command)

The program will ask you to enter a starting puzzle or you can use a random one by hitting enter.

## Command File 
To run the program with commands in a txt file, type "python EightPuzzle.py <filename>" (Note: you might need to type py or python3 depending on your computer. Additionally this assumes that you are in the 8Puzzle directory and that the test file is in the 8Puzzle, if you are not you will need to include the file path of EightPuzzle.py and the test file in the command). The output from the command file will print to the console and the file output.txt which should be automatically created in the 8Puzzle directory. 

## Available commands
After choosing a random puzzle, inputing a valid starting puzzle, or after you provide a txt file, you can use several commands:
    setState <state>                : Set the state of the of the puzzle
    printState                      : Print the current state of the puzzle
    move up                         : Move the blank puzzle piece up
    move down                       : Move the blank puzzle piece down
    move left                       : Move the blank puzzle piece left
    move right                      : Move the blank puzzle piece right
    heurestic <heuristic>           : Returns the value of the heurestic given (h1 or h2)
    scrambleState <n>               : Scrambles the state of the puzzle by making n random moves
    solve BFS <maxnodes>            : Performs a BFS algorithm on the current puzzle state until it reaches the goal state or reaches the node limit
    solve DFS <maxnodes>            : Performs a DFS algorithm on the current puzzle state until it reaches the goal state or reaches the node limit
    solve A* <heuristic> <maxnodes> : Performs a A* algorithm on the current puzzle state with the given heuristic (h1 or h2) until it reaches the goal state or reaches the node limit
    branch <acceptable> <maxnodes> <tolerance> <max-iterations> : Finds the branch factor of BFS, DFS, and A* with h1 and h2, then will return branch factors that have a depth within acceptable. 