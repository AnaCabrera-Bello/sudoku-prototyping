### Cell class to represent each cell in the Sudoku grid

## Each cell has a value and a box
# value = the number stored in the cell (1-9, or 0 if empty)
# box = the 3x3 box the cell belongs to (1-9)
# box is autodetermined based on the cell's position in the grid
# includes setters and getters for value and box
# includes construtcor and destructor

class Cell:
    value: int
    box: int

    # create a list of the positions of each 3x3 box in the grid
    box1 = [[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
    box2 = [[0,3],[0,4],[0,5],[1,3],[1,4],[1,5],[2,3],[2,4],[2,5]]
    box3 = [[0,6],[0,7],[0,8],[1,6],[1,7],[1,8],[2,6],[2,7],[2,8]]
    box4 = [[3,0],[3,1],[3,2],[4,0],[4,1],[4,2],[5,0],[5,1],[5,2]]
    box5 = [[3,3],[3,4],[3,5],[4,3],[4,4],[4,5],[5,3],[5,4],[5,5]]
    box6 = [[3,6],[3,7],[3,8],[4,6],[4,7],[4,8],[5,6],[5,7],[5,8]]
    box7 = [[6,0],[6,1],[6,2],[7,0],[7,1],[7,2],[8,0],[8,1],[8,2]]
    box8 = [[6,3],[6,4],[6,5],[7,3],[7,4],[7,5],[8,3],[8,4],[8,5]]
    box9 = [[6,6],[6,7],[6,8],[7,6],[7,7],[7,8],[8,6],[8,7],[8,8]]
            
    # constructor to assign the value and sets box to 0
    def __init__(self, value = 0):
        self.value = value
        self.box = 0
        
    # destructor to delete the value and box
    def __del__(self):
        del self.value
        del self.box
    
    # value setter and getter
    def setValue(self, value):
        self.value = value

    def getValue(self):
        return self.value
    
    # box setter and getter
    def getBox(self):
        return self.box
    
    def setBox(self, row, col):
        if [row, col] in self.box1:
            self.box = 1
        elif [row, col] in self.box2:
            self.box = 2
        elif [row, col] in self.box3:
            self.box = 3
        elif [row, col] in self.box4:
            self.box = 4
        elif [row, col] in self.box5:
            self.box = 5
        elif [row, col] in self.box6:
            self.box = 6
        elif [row, col] in self.box7:
            self.box = 7
        elif [row, col] in self.box8:
            self.box = 8
        elif [row, col] in self.box9:
            self.box = 9
    