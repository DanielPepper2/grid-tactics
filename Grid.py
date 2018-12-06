import Tile
import Unit
from graphics import *
from GridTacticsGraphics import *

class Grid(object):
    def __init__(self, seed, sizex, sizey, window):
        self.x = sizex
        self.y = sizey
        self.tiles = []
        self.window = window
        for i in range(sizex):
            temp_arr = []
            for j in range(sizey):
                temp_arr.append(Tile.Tile(i,j))

            self.tiles.append(temp_arr)

        #now populate neighbours for each tile
        for i in range(sizex):
            for j in range(sizey):
                temp_neighbours = []
                for k in range( max(0, i - 2), min(sizex, i + 3)):
                    temp_neighb_arr = []
                    for l in range( max(0, j - 2), min(sizey, j + 3)):
                        temp_neighb_arr.append(self.tiles[k][l])

                    temp_neighbours.append(temp_neighb_arr)

                self.tiles[i][j].set_neighbours(temp_neighbours)


        self.generate_map(seed)

#------------------------------------------------

    def place_unit(self, player, unit, x, y):
        self.tiles[x][y].place_unit(player, unit)

    def put_terrain(self, terrain, x, y):
        self.tiles[x][y].fix_terrain(terrain)

#------------------------------------------
#make a more exciting generate map function

    def generate_map(self, seed):
        self.put_terrain("t", 2, 2)
        self.put_terrain("t", 9, 6)

#-------------------------------------------

    def draw_board(self):


        for i in range(self.x + 1):
            print("__", end=' ')

        print("_")
        for j in range(self.y):
            print("| ", end=' ')
            for i in range(self.x):
                if self.tiles[i][j].occupant == 0:
                    print("{} ".format(self.tiles[i][j].terrain), end=' ')
                else:
                    print("{} ".format(self.tiles[i][j].unit_type), end=' ')

            print("|")

        for i in range(self.x + 1):
            print("__", end=' ')

        print("_")

#---------------------------------------------

    def winner(self):
        counter = 0
        for i in range(self.x):
            for j in range(self.y):
                counter += self.tiles[i][j].owner()

        if counter < 0:
            return 2
        elif counter > 0:
            return 1
        else:
            return 0

#-------------------------------------------------

    def is_occupied(self, coordinates) :
        x_coord = int(coordinates.getX()) - 1
        y_coord = int(coordinates.getY()) - 1
        return self.tiles[x_coord][y_coord].is_occupied()
