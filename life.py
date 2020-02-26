import pygame
import time

class Life:
    # create empty board
    def __init__(self, dimensions):
        self.size = dimensions;
        self.board = []
        for i in range(self.size[0]):
            self.board.append([])
            for j in range(self.size[1]):
                self.board[i].append(False)

    # bracket operator
    def __getitem__(self, key):
        return self.board[key[0]][key[1]]

    def __setitem__(self, key, value):
        self.board[key[0]][key[1]] = value

    # using keys for non-tiny boards (> 5x5) is not advised
    # and will be very slow

    # get set of all possible keys for these dimensions
    def getAllKeys(self):
        return range(2 ** (self.size[0] * self.size[1]))

    # assign life and dead cells based on number key
    def loadKey(self, key):
        bit = 0;
        for x in range(self.size[0]):
            for y in range(self.size[1]):
                self[x, y] = bool(key & (1 << bit))
                bit += 1

    # get number key corresponding to current arrangement of cells
    def getKey(self):
        bit = 0;
        key = 0;
        for x in range(self.size[0]):
            for y in range(self.size[1]):
                if self[x, y]:
                    key &= (1 << bit)
                bit += 1

    # current dimensions
    def getSize(self):
        return self.size;

    # get number of live cells among 8 immediate neighbors
    def getNeighbors(self, coords):
        return sum([\
            (1 if ((x != y) and self[self.wrapCoords((coords[0] + x, coords[1] + y))]) else 0)\
            for x in range(-1, 2) for y in range(-1, 2)])

    # out-of-bounds coordinates will wrap around the other side
    def wrapCoords(self, coords):
        return tuple([(coords[i] % self.size[i]) for i in range(2)])

    # execute the rules of Life n times
    def advance(self, n=1):
        didChange = False
        for i in range(n):
            oldBoard = self.clone()
            for x in range(self.size[0]):
                for y in range(self.size[1]):
                    isAlive = oldBoard[x, y];
                    neighbors = oldBoard.getNeighbors((x, y))
                    if(isAlive):
                        self[x, y] = neighbors == 2 or neighbors == 3
                    else:
                        self[x, y] = neighbors == 3
            if not didChange:
                didChange = oldBoard.isSame(self)
        return didChange

    # create copy of this board
    def clone(self):
        newBoard = Life(self.size)
        for x in range(self.size[0]):
            for y in range(self.size[1]):
                newBoard[x, y] = self[x, y]
        return newBoard

    # draw board to window
    def display(self, window):
        window = pygame.surface([window.get_size()[i] / self.size[i] for i in range(2)])
        window.fill((0, 0, 0))
        for x in range(self.size[0]):
            for y in range(self.size[1]):
                if self[x, y]:
                    pygame.draw.rect(window, (255, 255, 255), pygame.Rect((x * window[1], y * window[1]), window))

    # get number of live cells
    def getPopulation(self):
        return sum([\
            int(self[x, y])\
            for x in range(self.size[0]) for y in range(self.size[1])])

    # checks whether given board has same arrangement of cells as this one
    def isSame(self, other):
        if self.getSize() != other.getSize():
            return False;
        for x in range(self.size[0]):
            for y in range(self.size[1]):
                if self[x, y] != other[x, y]:
                    return False;   
        return True;

# intial parameters
windowSize = (600, 600)
boardSize = (3, 3)

# set up window
pygame.init();
window = pygame.display.set_mode(windowSize)

# create board
life = Life(boardSize)

# drawing takes a relatively long time, so speed up the process by not drawing every time
# this number determines how many times not to draw before drawing again
skipFrames = 10
count = 0

# loops through each possible initial conditions of the board
# this will take a very, very long time for a board much bigger than 4x4
for key in life.getAllKeys():

    # each configuration of the board has a number called the key
    # this loads the configuration corresponding to current key
    life.loadKey(key)

    # display board
    if count % (skipFrames + 1) == 0: 
        life.display(window)
        pygame.display.flip()
    count += 1

    ### YOUR CODE GOES HERE ###
    # will execute for each possible board

    # an example that prints the key number of all boards that haven't settled down after 2 steps:
    # remove the '##'s at the beginning of each line to run it
    ##life.advance(2) # go forward 2 steps
    ##oldLife = life.clone() # create a copy of the board
    ##life.advance() # make one of the boards go forward another step
    ##if not oldLife.isSame(life): # see if the board is different from one step ago
    ##    print(key)

    ### END OF YOUR CODE ###

# finish up
life.display(window)        
pygame.display.flip()

print("done")
exit();
