# 8puzzle
Hello! Welcome to my code. 
All of the python code is located in EightPuzzle.py

# Running the Code

## Command Line
To run the program with commands from the command line type "python EightPuzzle.py" (Note: you might need to type py or python3 depending on your computer. Additionally this assumes that you are in the 8Puzzle directory, if you are not you will need to include the file path of EightPuzzle.py in the command)

The program will ask you to enter a starting puzzle or you can use a random one by hitting enter.

## Command File 
To run the program with commands in a txt file, type "python EightPuzzle.py <filename>" (Note: you might need to type py or python3 depending on your computer. Additionally this assumes that you are in the 8Puzzle directory and that the test file is in the 8Puzzle, if you are not you will need to include the file path of EightPuzzle.py and the test file in the command)

## Available commands
After choosing a random puzzle, inputing a valid starting puzzle, or after you provide a txt file, you can use several commands:
    setState <state>    : Set the state of the of the puzzle
    printState          : Print the current state of the puzzle
    move up             : Move the blank puzzle piece up
    move down           : Move the blank puzzle piece down
    move left           : Move the blank puzzle piece left
    move right          : Move the blank puzzle piece right
    scrambleState <n>   : Scrambles the state of the puzzle by making n random moves