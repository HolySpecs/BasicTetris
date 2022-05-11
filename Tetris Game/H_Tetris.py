'''Importing Libraries'''
#Python libraries
import random, time, pygame, sys
#My libraries
import start_screen, main_menu
#Importing the necessary parts
from pygame.locals import *
#Importing from the other python files
from start_screen import *
from main_menu import *

#System setup
fps = 60           #Framerate of game
windowWidth = 800   #Width of game window
windowHeight = 700  #Height of game window
boxSize = 25        #Board scale
boardWidth = 10     #Board Width
boardHeight = 24    #Board Height
gameRunning = True

while gameRunning:
    game_intro()
    main_menu()