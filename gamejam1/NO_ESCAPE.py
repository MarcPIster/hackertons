#!/usr/bin/env python3
from Assets.Code import screen, gameloop
from Assets.Code import mainmenu, instructionmenu, settingsmenu, pausemenu, chooselv, endscreen, highscore
import pygame

def open_windows():
    case = 0
    vol = 0.3
    map_nbr = 0
    mute = 0
    old_vol = vol
    score = 0
    while (case != 3):
        if (case == 0):
            case, vol  = mainmenu.main_menu(vol)
        elif case == 1:
            case = endscreen.end_screen()
        elif case == 2: 
            case = instructionmenu.instruction()
        elif case == 4:
            case, vol, mute, old_vol = settingsmenu.settings_menu(vol, mute, old_vol) 
        elif case == 5:
            case = highscore.highscore_menu(score)  
        elif case == 6: #open game loop from mainmenu
            case = 0
            window = screen.create_window(1280, 720)
            case, vol, map_nbr, old_vol, mute = gameloop.game_loop(window, case, vol, map_nbr, old_vol, mute)
        elif case == 7:
            case, map_nbr = chooselv.choose_lvl(map_nbr)

def main():
    print("start main menu")
    open_windows()

if __name__ == '__main__':
    pygame.init()
    main()