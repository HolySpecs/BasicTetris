class System:
    def __init__(self):
        #System setup
        fps = 60           #Framerate of game
        windowWidth = 800   #Width of game window
        windowHeight = 700  #Height of game window
        boxSize = 25        #Board scale
        boardWidth = 10     #Board Width
        boardHeight = 24    #Board Height
        gameRunning = True

class PieceColours:
    def __init__(self):
        #Colours
        #name         R   G   B
        cyan =      ( 14,246,238) #I Piece
        blue =      (  0,  2,230) #J Piece
        orange =    (226,161, 35) #L Piece 
        yellow =    (245,251, 24) #O Piece
        green =     ( 42,233, 31) #S Piece
        purple =    (226, 34,217) #T Piece
        red =       (216, 11, 26) #Z Piece

class MenuColours:
    def __init__(self):
        #Colours used
        #              R    G    B
        white =     (255, 255, 255)
        black =     (  0,   0,   0)
        grey =      ( 50,  50,  50)
        red =       (255,   0,   0)
        green =     (  0, 255,   0)
        blue =      (  0,   0, 255)
        yellow =    (255, 255,   0)
        blueGrey =  ( 36,  63,  93)