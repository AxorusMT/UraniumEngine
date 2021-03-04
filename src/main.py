#
import Function
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import Window
import pygame

pygame.init()

#Window.setWindowBorderlessMode(True)
#Window.setWindowResizableMode(True)
Window.createWindow(600, 600, "Uranium Engine Demo window", (0, 0, 255))
#Window.updateWindow()
run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

Function.quitProgram(True)
