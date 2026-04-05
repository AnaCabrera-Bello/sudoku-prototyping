import grid
import nicegui

# creating a valid grid and printing it
my_grid = grid.Grid()

if not my_grid.validGrid():
    while not my_grid.validGrid():
        del my_grid
        my_grid = grid.Grid()

my_grid.printGrid()


# creating the ui






