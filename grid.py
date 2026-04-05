# Grid class to generate a valid sudoku grid
    # The grid will be a 9x9 matrix of Cell objects

import random
from cell import Cell

class Grid:
    grid: list[list[Cell]]
    
    # constructor to create a grid
    def __init__(self):
        # create a 9x9 grid of Cell objects with value 0
        self.grid = [[Cell(0) for _ in range(9)] for _ in range(9)]

        # populate the grid with the box numbers and values
        for row in range(9):
            for col in range(9):
                self.grid[row][col].setBox(row, col)

                # generate a random value for the cell
                vals_to_check = self.makeVals()
                val = random.choice(vals_to_check)

                # check if the value is valid for the cell
                while not self.validRow(row, val) or not self.validCol(col, val) or not self.validBox(self.grid[row][col].getBox(), val):
                    vals_to_check.remove(val)
                    if len(vals_to_check) == 0:
                        print("Did not generate valid grid")
                        return
                    val = random.choice(vals_to_check)
                
                self.grid[row][col].setValue(val)

    # destructor to delete the grid
    def __del__(self):
        del self.grid

    # function to check if a value is already in the row
    def validRow(self, row, value):
        for i in range(9):
            if self.grid[row][i].getValue() == value:
                return False
        return True
    
    # function to check if a value is already in the column
    def validCol(self, col, value):
        for i in range(9):
            if self.grid[i][col].getValue() == value:
                return False
        return True
    
    # function to make values to check
    def makeVals(self):
        return [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # function to check if a value is already in the box
    def validBox(self, box, value):
        if box == 1: 
            box_to_check = Cell.box1
        elif box == 2: 
            box_to_check = Cell.box2
        elif box == 3: 
            box_to_check = Cell.box3
        elif box == 4: 
            box_to_check = Cell.box4
        elif box == 5: 
            box_to_check = Cell.box5
        elif box == 6: 
            box_to_check = Cell.box6
        elif box == 7: 
            box_to_check = Cell.box7
        elif box == 8: 
            box_to_check = Cell.box8
        elif box == 9: 
            box_to_check = Cell.box9

        for i in range(9):
            r = box_to_check[i][0]
            c = box_to_check[i][1]
            if self.grid[r][c].getValue() == value:
                return False
        return True

    # function to print the grid
    def printGrid(self):
        for row in range(9):
            for col in range(9):
                print(self.grid[row][col].getValue(), end=" ")
            print()

    # check if the grid is valid
    def validGrid(self):
        for row in range(9):
            for col in range(9):
                if self.grid[row][col].getValue() == 0:
                    return False
        return True
    