class Unit(object):

    def __init__(self, terrain):
        self.attack = 0
        self.defense = 0
        self.unit_type = ""
        self.attacked_counter = 0
        self.exceptions = [' ']
        self.cost = 0
        pass

    def change_attacked_counter(self, unit, pm):
        if unit.unit_type not in self.exceptions:
            if pm == "-":
                self.attacked_counter -= 1
            else:
                self.attacked_counter += 1

    def is_dead(self):
        if self.defense <= self.attacked_counter:
            return True
        else:
            return False

#----------------------------------

class Archer(Unit):
    def __init__(self, terrain):
        self.attack = 2
        self.defense = 3
        self.unit_type = "a"
        self.attacked_counter = 0
        self.cost = 2
        self.exceptions = [' ']

#----------------------------------

class Defender(Unit):
    def __init__(self, terrain):
        self.attack = 1
        self.defense = 4
        self.unit_type = "d"
        self.attacked_counter = 0
        self.exceptions = ["a"]
        self.cost = 2

#-----------------------------------

class Infantry(Unit):
    def __init__(self, terrain):
        self.attack = 1
        if terrain == "t":
            self.defense = 4
        else:
            self.defense = 3
            
        self.unit_type = "i"
        self.attacked_counter = 0
        self.cost = 1
        self.exceptions = [' ']
