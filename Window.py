import pygame

pygame.init()



def createWindow(width, height, title, window_color=(0,0,0)):
    window_dim = (width, height)
    window = pygame.display.set_mode(window_dim, 5)
    pygame.display.set_caption(title)
    window.fill(window_color)
    pygame.display.update()



#def setWindowModes(borderless=False, resizable=False):
    #OK so for some reason this is difficult for me idk why
    #if borderless:


def updateWindow():
    pygame.display.update()

def destroyWindow():
    pass
