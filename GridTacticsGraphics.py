from graphics import *

#-----------------------------------------------------------

def make_button(window, lx, rx, by, ty, colour, text):
    buttonlt = Point(lx, ty)
    buttonlb = Point(lx, by)
    buttonrt = Point(rx, ty)
    buttonrb = Point(rx, by)
    button_vertices = [buttonlt, buttonlb, buttonrb, buttonrt]
    button = Polygon(button_vertices)
    button.setFill(colour)
    button.setOutline('black')
    button.draw(window)

    midpoint = Point((lx + rx) / 2, (ty + by) / 2)
    button_text = Text(midpoint, text)
    button_text.setStyle('bold')
    button_text.setSize(18)
    button_text.draw(window)

#--------------------------------------------------------------

def draw_menu(window, menu):
    if menu == 'main':
        main_background = Image(Point(451,301), 'Extra\Background.gif')
        Image.draw(main_background,window)

        make_button(window, 341, 561, 101, 176, 'lime', 'New Game')
        make_button(window, 341, 561, 226, 301, 'cyan', 'Load Game')
        make_button(window, 341, 561, 351, 426, 'darkorange', 'Instructions')
        make_button(window, 341, 561, 476, 551, 'red', 'Quit')

    elif 'inst' in menu :

        inst_num = menu[4:]
        inst_background = Image(Point(451,301), "Extra\Page " + inst_num + ".gif")
        Image.draw(inst_background, window)

        make_button(window, 51, 201, 541, 591, 'red', 'Previous')
        make_button(window, 376, 551, 541, 591, 'cyan', 'Main Menu')
        make_button(window, 701, 851, 541, 591, 'lime', 'Next')

    elif 'newgame' in menu :

        newgame_page = menu[7:]

        if newgame_page == '1' :
            newgame_background = Image(Point(451,301), "Extra\Background.gif")
            Image.draw(newgame_background,window)
            make_button(window, 341, 561, 101, 176, 'lime', 'P v P')
            make_button(window, 341, 561, 226, 301, 'cyan', 'AI')
        elif newgame_page == '2' :
            newgame_background = Image(Point(451,301), "Extra\BackgroundMap.gif")
            Image.draw(newgame_background,window)
            make_button(window, 88, 263, 201, 376, 'white', '')
            make_button(window, 363, 538, 201, 376, 'white', '')
            make_button(window, 638, 813, 201, 376, 'white', '')

            classic_map = Image(Point(175, 276), "Extra\ClassicMap.gif")
            Image.draw(classic_map, window)

            button1_text = Text(Point(175, 357), "Classic")
            button1_text.setStyle('bold')
            button1_text.setSize(12)
            button1_text.draw(window)

            desert_map = Image(Point(725, 276), "Extra\Desert.gif")
            Image.draw(desert_map, window)

            button2_text = Text(Point(725, 357), "Desert")
            button2_text.setStyle('bold')
            button2_text.setSize(12)
            button2_text.draw(window)

            meadow_map = Image(Point(450, 276), "Extra\Meadow.gif")
            Image.draw(meadow_map, window)

            button3_text = Text(Point(450, 357), "Meadow")
            button3_text.setStyle('bold')
            button3_text.setSize(12)
            button3_text.draw(window)

        elif newgame_page == '3' :

            newgame_background = Image(Point(451,301), "Extra\BackgroundMap.gif")
            Image.draw(newgame_background,window)
            make_button(window, 88, 263, 201, 376, 'white', '')
            make_button(window, 363, 538, 201, 376, 'white', '')
            make_button(window, 638, 813, 201, 376, 'white', '')

            red_team = Image(Point(175, 276), "Extra\Red Team.gif")
            Image.draw(red_team, window)

            button1_text = Text(Point(175, 357), "Greek")
            button1_text.setStyle('bold')
            button1_text.setSize(12)
            button1_text.draw(window)



            orange_team = Image(Point(450, 276), "Extra\Orange Team.gif")
            Image.draw(orange_team, window)

            button3_text = Text(Point(450, 357), "Egyptian")
            button3_text.setStyle('bold')
            button3_text.setSize(12)
            button3_text.draw(window)

            blue_team = Image(Point(725, 276), "Extra\Atlantean Team.gif")
            Image.draw(blue_team, window)

            button2_text = Text(Point(725, 357), "Atlantean")
            button2_text.setStyle('bold')
            button2_text.setSize(12)
            button2_text.draw(window)
        elif newgame_page == '4' :

            newgame_background = Image(Point(451,301), "Extra\BackgroundMap.gif")
            Image.draw(newgame_background,window)
            make_button(window, 88, 263, 201, 376, 'white', '')
            make_button(window, 363, 538, 201, 376, 'white', '')
            make_button(window, 638, 813, 201, 376, 'white', '')

            red_team = Image(Point(175, 276), "Extra\Red Team.gif")
            Image.draw(red_team, window)

            button1_text = Text(Point(175, 357), "Greek")
            button1_text.setStyle('bold')
            button1_text.setSize(12)
            button1_text.draw(window)



            orange_team = Image(Point(450, 276), "Extra\Orange Team.gif")
            Image.draw(orange_team, window)

            button3_text = Text(Point(450, 357), "Egyptian")
            button3_text.setStyle('bold')
            button3_text.setSize(12)
            button3_text.draw(window)

            blue_team = Image(Point(725, 276), "Extra\Atlantean Team.gif")
            Image.draw(blue_team, window)

            button2_text = Text(Point(725, 357), "Atlantean")
            button2_text.setStyle('bold')
            button2_text.setSize(12)
            button2_text.draw(window)
    elif menu == 'start' :
        #clears window
        clear_window = Polygon([Point(0,0), Point(0,602), Point(902,602), Point(902,0)])
        clear_window.setFill('white')
        clear_window.setOutline('white')
        clear_window.draw(window)

        #Grid lines + letters
        for i in range(13):
            linex = 50 * (i + 1)
            vline = Line(Point(linex, 50), Point(linex, 550))
            vline.draw(window)
            if i != 12 :
                coordinate_let = Text(Point(linex + 25, 576), chr(ord('A') + i))
                coordinate_let.setSize(12)
                coordinate_let.setStyle('bold')
                coordinate_let.draw(window)

        for j in range(11):
            liney = 50 * (j + 1)
            hline = Line(Point(50, liney), Point(50 * 13, liney))
            hline.draw(window)
            if j != 10 :
                coordinate_let = Text(Point(25, liney + 25), str(j + 1))
                coordinate_let.setSize(12)
                coordinate_let.setStyle('bold')
                coordinate_let.draw(window)

        #buttons
        make_button(window, 701, 876, 126, 176, 'lime', 'Submit!')
        make_button(window, 701, 876, 276, 326, 'cyan', 'Save & Quit')
        make_button(window, 701, 876, 426, 476, 'red', 'End Game')

#-----------------------------------------------------------

def draw_unit(coordinates, player, unit_type, window) :
    if unit_type == 0 :
        gif_str = 'E.gif'
    elif unit_type == 1 :
        gif_str = str(player) + 'Infantry.gif'
    elif unit_type == 2 :
        gif_str = str(player) + 'Archer.gif'
    else :
        gif_str = str(player) + 'Defender.gif'

    #need to take into account map type and terrain,
    unit = Image(Point(coordinates.getX()*50 + 25, coordinates.getY()*50 + 25), 'Classic\\' + gif_str)
    unit.draw(window)
