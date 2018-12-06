import Grid
import Unit
import Player
from GridTacticsGraphics import *

win = GraphWin("Grid Tactics", 902, 602)

#-------------------------------------------------------------

def within(point, x_min, x_max, y_min, y_max):
    return x_min <= point.getX() <= x_max and y_min <= point.getY() <= y_max

#-----------------------------------------------------------------

def Grid_Tactics(num_players, map, player_1_team, player_2_team):
    #put picture handles in terrain, tile?, player?

    player_one = Player.Human(1)
    player_two = Player.Human(2)
    players = [player_one, player_two]
    num_humans = 2
    turns = 1

    grid = Grid.Grid(1, 12, 10, win)

    gameover = False
    player_turn = 1
    prev_coordinates = Point(0,0)
    unit_type = 0
    unit_placed = False

    while not gameover:
        mouse_location = win.getMouse()
        if within(mouse_location, 701, 876, 426, 476):  #this stuff needs rework to account for varying board sizes
            gameover = True
        elif within(mouse_location, 51, 651, 51, 551): #mouse is within game board
            mouse_x = mouse_location.getX()
            mouse_y = mouse_location.getY()
            coordinates = Point(int(mouse_x / 50), int(mouse_y / 50))

            #check for unit placed, unoccupied square, same square
            same_square_click = coordinates == prev_coordinates
            square_unoccupied = not grid.is_occupied(coordinates) #need to check move without updating the grid
            if valid_move :
                prev_coordinates = coordinates
            #need to check if mouse is clicking same tile as its unit is in
            if unit_placed and prev_coordinates == coordinates:
                unit_type = (unit_type + 1 ) % 4
                draw_unit(coordinates, player_turn, unit_type, win) #make sure when calling this, that we are using instead of player_turn, the player team, need to change player class for this as well
            elif valid_move and not unit_placed :
                draw_unit(coordinates, player_turn, unit_type, win) #make sure when calling this, that we are using instead of player_turn, the player team, need to change player class for this as well
                unit_placed = True
        elif within(mouse_location, 701, 876, 276, 326): #mouse is on save and quit
            quit()
        elif within(mouse_location, 701, 876, 126, 176) and unit_placed: #mouse is on submit

            quit_type, cost = players[player_turn - 1].make_move(unit_placed, grid)

            #do this last
            unit_placed = False
            unit_type = 0
            prev_coordinates = Point(0,0)
            #update text in top right as well


        #if num_humans > 0:
        #    grid.draw_board()



        #line below is causing some issues, rework make_move function
        #quit_type, cost = players[player_turn - 1].make_move(grid)



        #if quit_type =="r":
        #    end_game(grid, True, player_turn)
        #elif quit_type == "q":
        #    end_game(grid, False, 0)

        #need some gameover condition

        #switches player turn
        #turns -= cost
        #if turns <= 0:

        #    player_turn = abs(2 - player_turn) + 1
        #    #arithmetic for higher valued pieces played
        #    turns = -turns
        #    turns += 1

        #update text at top (need new method)


    end_game(grid, False, 0)

#----------------------------------------------------
# needs rework
def end_game(grid, resign, player_turn):
    if resign:
        print(f"Player {abs(player_turn - 2) + 1} Wins by Resignation!")
    else:
        result = grid.winner()
        if result == 0:
            print("Draw!")
        else:
            print(f"Player {result} Wins!")
    #instead of quitting, consider going back to main menu
    quit()

#---------------------------------------------------

def menu():
    menu = 'main'

    draw_menu(win, menu)
    while True :

        mouse_location = win.getMouse()
        if menu == 'main' : #main menu buttons
            if within(mouse_location, 341, 561, 476, 551):
                quit()
            elif within(mouse_location, 341, 561, 351, 426):
                menu = 'inst1'
                draw_menu(win, menu)
            elif within(mouse_location, 341, 561, 226, 301):
                menu = 'loadgame'
                quit() #change this
            elif within(mouse_location, 341, 561, 101, 176):
                menu = 'newgame1'
                draw_menu(win, menu)
        elif 'inst' in menu :  #instruction menu buttons
            inst_num = int(menu[4:])
            if within(mouse_location, 51, 201, 541, 591):
                if inst_num == 1 :
                    menu = 'main'
                    draw_menu(win, menu)
                else :
                    inst_num -= 1
                    menu = 'inst' + str(inst_num)
                    draw_menu(win, menu)
            elif within(mouse_location, 701, 851, 541, 591):
                if inst_num == 12 :
                    menu = 'main'
                    draw_menu(win, menu)
                else :
                    inst_num += 1
                    menu = 'inst' + str(inst_num)
                    draw_menu(win, menu)
            elif within(mouse_location, 376, 551, 541, 591) :
                menu = 'main'
                draw_menu(win, menu)
        elif 'newgame' in menu : #newgame menu buttons
            newgame_page = menu[7:]
            if newgame_page == '1' :
                if within(mouse_location, 341, 561, 101, 176) :
                    num_players = 2
                elif within(mouse_location, 341, 561, 101, 176) :
                    num_players = 1
                menu = 'newgame2'
                draw_menu(win, menu)
            elif newgame_page == '2' :
                if within(mouse_location, 88, 263, 201, 376) :
                    map = 'classic'
                    menu = 'newgame3'
                    draw_menu(win, menu)
                elif within(mouse_location, 363, 538, 201, 376) :
                    map = 'meadow'
                    menu = 'newgame3'
                    draw_menu(win, menu)
                elif within(mouse_location, 638, 813, 201, 376) :
                    map = 'desert'
                    menu = 'newgame3'
                    draw_menu(win, menu)
            elif newgame_page == '3' :
                if within(mouse_location, 88, 263, 201, 376) :
                    player_1_team = 'red'
                    menu = "newgame4"
                    draw_menu(win, menu)
                elif within(mouse_location, 363, 538, 201, 376) :
                    player_1_team = 'orange'
                    menu = "newgame4"
                    draw_menu(win, menu)
                elif within(mouse_location, 638, 813, 201, 376) :
                    player_1_team = 'blue'
                    menu = "newgame4"
                    draw_menu(win, menu)
            elif newgame_page == '4' :
                if within(mouse_location, 88, 263, 201, 376) :
                    player_2_team = 'red'
                    menu = "start"
                    draw_menu(win, menu)
                    break
                elif within(mouse_location, 363, 538, 201, 376) :
                    player_2_team = 'orange'
                    menu = "start"
                    draw_menu(win, menu)
                    break
                elif within(mouse_location, 638, 813, 201, 376) :
                    player_2_team = 'blue'
                    menu = "start"
                    draw_menu(win, menu)
                    break
        elif menu == 'loadgame' :
            quit() #change this

    Grid_Tactics(num_players, map, player_1_team, player_2_team)

#----------------------------------------------------
#Program starts here

menu()
