import Unit

class Tile(object):
    def __init__(self, x, y):
        self.terrain = "_"
        self.unit = None
        self.occupant = 0
        self.attacked = [0,0]
        self.xcoord = x
        self.ycoord = y
        self.neighbours = None
        self.unit_type = ""

    def set_neighbours(self, neighbours):
        #need to set neighbours after grid has been formed.
        self.neighbours = neighbours

    def fix_terrain(self, terrain):
        #set function that fixes terrain at startup
        self.terrain = terrain

    def is_occupied(self):
        if self.occupant != 0 or self.terrain == "w":
            return True
        else:
            return False

#--------------------------------------------------------

    def notify_neighbours(self, pm):
        for i in range(len(self.neighbours)) :
            for j in range(len(self.neighbours[i])):
                self.neighbours[i][j].notify(self.occupant, self.unit, self.xcoord, self.ycoord, pm)

#---------------------------------------------------------

    def dead(self):
        self.attacked[self.occupant - 1] -= 1
        self.occupant = 0
        self.unit_type = ""
        self.unit = None

#----------------------------------------------------------

    def notify(self, player, unit, x, y, pm):
        #don't notify yourself
        if x == self.xcoord and y == self.ycoord:
            return

        #get notified of changes on neighbouring tiles
        distance = max(abs(self.xcoord - x), abs(self.ycoord - y))
        if distance <= unit.attack:
            if self.occupant > 0 and self.occupant != player:
                self.unit.change_attacked_counter(unit, pm)
                if self.unit.is_dead():
                    self.notify_neighbours("-")
                    self.dead()

            if pm == "-":
                self.attacked[player - 1] -= 1
            else :
                self.attacked[player - 1] += 1

#-----------------------------------------------------------

    def place_unit(self, player, unit):
        self.unit = unit
        self.occupant = player
        self.attacked[player - 1] += 1
        self.unit_type = unit.unit_type

        #initialize attacked_counter for new unit
        for i in range(len(self.neighbours)):
            for j in range(len(self.neighbours[i])):
                if self.neighbours[i][j].occupant == abs(player -2) + 1:
                    distance = max(abs( 2 - i ), abs(j - 2))
                    if distance <= self.neighbours[i][j].unit.attack:
                        self.unit.change_attacked_counter(self.neighbours[i][j].unit, "+")

        #notify neighbours of new piece placement
        self.notify_neighbours("+")

        if self.unit.is_dead():
            self.notify_neighbours("-")
            self.dead()
#-------------------------------------------------------------

    def owner(self):
        if self.occupant != 0:
            return (-2) * self.occupant + 3
        elif self.attacked[0] == self.attacked[1]:
            return 0
        elif self.attacked[0] < self.attacked[1]:
            return -1
        else:
            return 1
