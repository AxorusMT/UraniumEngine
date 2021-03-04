import os
import pygame

def disableStartUpMessage():
    pass #FIXME: make this damn function work.

def quitProgram(display_quit_msg=False):
    if display_quit_msg:
        print("Exited Game")
    pygame.quit()
