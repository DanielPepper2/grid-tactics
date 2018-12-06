class Terrain(object):
    def __init__(self):
        pass

#------------------------------

class Tree(Terrain):
    def __init__(self):
        self.bonus_def = 1
        self.obstruct = False

#-------------------------------

class Water(Terrain):
    def __init__(self):
        self.bonus_def = 0
        self.obstruct = True
