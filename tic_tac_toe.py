# Hello I'm Corey today is July 20th 2023 cool.
import random
# Objective: make a tic-tac-toe game

#Main function
def tic_tac_toe(user):
    #Make a new empty grid
    grid = init_grid()
    print("New Game")
    show_grid(grid)

    #Take a User Input and place and X at that point

    user == user_input(grid)
    grid = place_marker


# Features: 
# Needs to store the 3 by 3 grid
def init_grid():
    return list(range(1,10))

# Place Xs and Os on the grid
def place_marker(grid, symbol, index):
    grid[index-1] = symbol
    return grid

# Make a computer to play against
def conputer_move(grid):
    comp = random.randint(1,9)
    if type(grid[comp-1]) == int:
        return comp

# Take in user inputs
def user_input(grid):
    while True:
        user = input("Select a position from 1 - 9 ")
        if user.isnumeric() and int(user) >= 1 and int(user) <= 9 and type(grid[int(user)-1]) == int:
            return user
        else: 
            print("Invalid input try again ")
    

# Check if somebody wins
def check_win(grid):
    # Call winning_row on every possibility
    # if any produce a win, return that symbol
    # else return false
    winning_row(grid[0:3]) or \
    winning_row(grid[3:6]) or \
    winning_row(grid[6:9]) or \
    winning_row(grid[0:9:3]) or \
    winning_row(grid[1:9:3]) or \
    winning_row(grid[2:9:3]) or \
    winning_row(grid[0:4:8]) or \
    winning_row(grid[2:7:2]) 

# Check if a row has all Xs or Os
def winning_row(row):
    if row[0] == row[1] and row [1] == row[2]:
        return(row)
    else:
        return False

# Show the grid to the user
def show_grid(grid):
    print(f"| {grid[0]} | {grid[1]} | {grid[2]} |\n\
    -------------\n\
    | {grid[3]} | {grid[4]} | {grid[5]} |\n\
    -------------\n\
    | {grid[6]} | {grid[7]} | {grid[8]} |")


# Check if the game is drawn
def stalemate(grid):
    return all(isinstance(cell, str) for cell in grid)

# Restrictions:
# What if the game ends ina stalemate
# Illegal move (1-9)
# Illegal move (Already selected box)
# How does the computer pick moves\
