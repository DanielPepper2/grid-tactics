
class Player(object):
    def __init__(self, team):
        pass

    def make_move(self, type, xcoord, ycoord):
        pass

#-----------------------------------------------

class Human(Player):
    def __init__(self, team):
        self.team = team

    def make_move(self, grid):
        valid_move = False
        while not valid_move:
            print(f"Player {self.team} to move: ", end=' ')
            command = input().split(' ')[::-1]
            type = command.pop()
            if type == "q" or type == "r":
                return type, 0
            else:
                xcoord = int(command.pop())
                ycoord = int(command.pop())
                valid_move = grid.is_valid(self.team, type, xcoord, ycoord)
                cost = grid.tiles[xcoord][ycoord].unit.cost
                if valid_move:
                    return "", cost

#-----------------------------------------------------
