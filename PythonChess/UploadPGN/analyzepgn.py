''' Daniel Hayes
3/18/23
This is the generated user interface for the chess program.'''
import pygame
import ChessRecordGame.Pieces as Pieces
import sys
import pgnloader


def initializeWhitepieces():
    # This function has no parameter, it initializes white pieces.
    # It returns a list of White Pieces.
    whiteTeam = []
    rookOne = Pieces.Rook([0,0],"R","W")
    whiteTeam.append(rookOne)
    knightOne = Pieces.Knight([0,1],"N","W") 
    whiteTeam.append(knightOne)
    bishopOne = Pieces.Bishop([0,2],"B","W") 
    whiteTeam.append(bishopOne)
    wking = Pieces.King([0,3],"K","W") 
    whiteTeam.append(wking)
    queen = Pieces.Queen([0,4],"Q","W") 
    whiteTeam.append(queen)
    bishopTwo = Pieces.Bishop([0,5],"B","W") 
    whiteTeam.append(bishopTwo)
    knightTwo = Pieces.Knight([0,6],"N","W") 
    whiteTeam.append(knightTwo)
    rookTwo = Pieces.Rook([0,7],"R","W") 
    whiteTeam.append(rookTwo)

    for x in range(0,8,1):
        whiteTeam.append(Pieces.Pawn([1,x],"P","W"))
    return(whiteTeam)

def initializeBlackpieces():
    # This function has no parameter, it initializes black pieces.
    # It returns a list of Black Pieces.
    blackTeam = []
    rookOne = Pieces.Rook([7,0],"R","B")
    blackTeam.append(rookOne)
    knightOne = Pieces.Knight([7,1],"N","B") 
    blackTeam.append(knightOne)
    bishopOne = Pieces.Bishop([7,2],"B","B") 
    blackTeam.append(bishopOne)
    bking = Pieces.King([7,3],"K","B") 
    blackTeam.append(bking)
    queen = Pieces.Queen([7,4],"Q","B") 
    blackTeam.append(queen)
    bishopTwo = Pieces.Bishop([7,5],"B","B") 
    blackTeam.append(bishopTwo)
    knightTwo = Pieces.Knight([7,6],"N","B") 
    blackTeam.append(knightTwo)
    rookTwo = Pieces.Rook([7,7],"R","B") 
    blackTeam.append(rookTwo)

    for x in range(0,8,1):
        blackTeam.append(Pieces.Pawn([6,x],"P","B"))
    return(blackTeam)

def removePiece(piece, friendlyTeam):
    friendlyTeam.pop(piece)

def drawPieces(screen,images, teams):
    # This function draws the pieces on board.
    # It takes in the list of pieces for both teams.
    for pos in teams:
        location = [700-pos.position[1]*100,700-pos.position[0]*100]
        pic = images[str(pos.team)+str(pos.name)]
        screen.blit(pic,location)


def highLightMoves(screen, moves, squareSize):
    # Takes in the screen, the list of lists of coordinates and square size to highlights them.
    highlight = pygame.Surface((squareSize,squareSize)) 
    highlight.fill(pygame.Color("green"))
    if len(moves) > 0:
        if len(moves[0]) > 0:
            for move in moves:
                screen.blit(highlight, (700-move[1] * squareSize, 700-move[0] * squareSize))

def loadImages(teams):
    # This function loads the images into a dictionary.
    # Parameters are the teams
    # Returns a dictionary of the scaled images.
    images = {}
    piecelist = []
    add = True
    for piece in teams:
        add = True
        for pos in piecelist:
            if pos == str(piece.team)+str(piece.name):
                add = False   
        if add == True:
            images[str(piece.team)+str(piece.name)] = pygame.transform.scale(pygame.image.load("C:\\Users\smidg\\.vscode\\BigProject\\images\\" + str(piece.team)+str(piece.name) + ".png"), (100,100))
            piecelist.append(str(piece.team)+str(piece.name))
    return(images)

#def drawPiece(screen,images,piece):
    # Parameters the screen, the dictionary of images, and the piece to draw.
    # It draws the piece on the board in the position it is.

    #location = [700-piece.position[1]*100,700-piece.position[0]*100]
    #pic = images[str(piece.team)+str(piece.name)]
    #screen.blit(pic,location)

def setupBoard(screen,squareSize):
    # Parameters are the current pygame screen and the length of the side of the squares.
    # Prints the checkered chess board.
    
    white = pygame.Color(255, 255, 255)
    screen.fill(pygame.Color("darkblue"))
    for square in range(64):
        if square%2 == 0:
            if 7 < square < 15 or 23 < square < 31 or 39 < square < 47 or 55 < square < 63:
                x = int(((1+square%8)*squareSize))
                y = (int(square/8))*squareSize
                pygame.draw.rect(screen,white,pygame.Rect(x,y,squareSize,squareSize))
            else: 
                x = int((square%8*squareSize))
                y = (int(square/8))*squareSize
                pygame.draw.rect(screen,white,pygame.Rect(x,y,squareSize,squareSize))

    pygame.display.update()

def main():
    # Plays the game, initializes pygame window. 
    # Uses classes and functions to play chess.
    blackTeam = initializeBlackpieces()
    whiteTeam = initializeWhitepieces()
    teams = blackTeam+whiteTeam
    connect = []
    connect.append(whiteTeam.copy())
    connect.append(blackTeam.copy())
    boardPositions = []
    boardPositions.append(connect)
    # Initialize Pygame
    pygame.init()

    # Set the window size
    window_size = (800, 800)

    # Create the window
    screen = pygame.display.set_mode(window_size)

    clock = pygame.time.Clock()

    fps_controller = pygame.time.Clock()
    squareSize = 100
    # Setup Board squares
    setupBoard(screen, squareSize)
    # Load images
    images = loadImages(teams)
    # Receiving in moves from PGN file
    themoves = pgnloader.movelist()
    print(themoves)
    counter = 0
    # Initialize pieces
    drawPieces(screen,images,teams)
    pygame.display.flip()
    moves = []
    piece = Pieces.King([20,20],"K","D")
    lastMove = piece
    lastc = piece.position

    whiteTurn = True
    run = True
    column = piece.position[1]
    while run:
        found = False

        if len(themoves) > counter:
            if whiteTurn == False:
                
                track = counter
                for parts in blackTeam:
                    if found == False:
                        if parts.name == themoves[counter][0]:

                            moves = Pieces.Piece.getpieceMoves(parts, blackTeam, whiteTeam, lastMove)      
                            piece = parts

                            for cords in moves:
                                if found == False:
                                    if len(themoves[counter]) == 2:
                                        if cords == themoves[counter][1]:
                                            column = piece.position[1]
                                            Pieces.Piece.movePiece(piece,cords)
                                            drawPieces(screen,images,teams)
                                            #pygame.time.delay(250)
                                            found = True
                                            counter += 1
                                    elif len(themoves[counter]) == 3:
                                        if piece.position[1] == themoves[counter][1]:
                                            if cords == themoves[counter][2]:
                                                column = piece.position[1]
                                                Pieces.Piece.movePiece(piece,cords)
                                                drawPieces(screen,images,teams)
                                                #pygame.time.delay(250)
                                                found = True
                                                counter += 1 
                if track == counter:
                    pygame.time.delay(2500)

                if piece.name == "P":
                    if piece.position[0] == 0:
                        Pieces.Pawn.promotion(piece)
                        
                if not Pieces.King.kingattackedSquares(whiteTeam,blackTeam):
                    if Pieces.King.checkMate(whiteTeam,blackTeam):
                        print("Checkmate! White wins.")
                    else:
                        if Pieces.King.checkMate(whiteTeam,blackTeam):
                            print("This is a draw.") 
                whiteTurn = True

                dead = False
                for posi in whiteTeam:
                    if piece.position == posi.position:
                        whiteTeam.remove(posi)
                        teams.remove(posi)
                        dead = True
                if dead == False:
                    if piece.name == "P":
                        if column != piece.position[1]:
                            for pie in whiteTeam:
                                if pie.position == lastc:   
                                    whiteTeam.remove(pie)
                                    teams.remove(pie)
                    elif piece.name == "K":
                        Pieces.Piece.castleRook(piece, column, blackTeam)
                lastMove = piece
                lastc = piece.position
                setupBoard(screen,squareSize)
                drawPieces(screen,images,teams)
                pygame.display.flip()
                clock.tick(30)
                moves = []
            else:

                track = counter
                for part in whiteTeam:
                    print(part.name,themoves[counter][0])
                    if found == False:
                        if part.name == themoves[counter][0]:

                            moves = Pieces.Piece.getpieceMoves(part, whiteTeam,blackTeam, lastMove)
                            piece = part

                            for cords in moves:
                                if len(themoves[counter]) == 2:
                                    if cords == themoves[counter][1]:
                                        
                                        column = piece.position[1]
                                        Pieces.Piece.movePiece(piece,cords)
                                        drawPieces(screen,images,teams)
                                        #pygame.time.delay(250)
                                        found = True
                                        counter += 1
                                elif len(themoves[counter]) == 3:
                                    if piece.position[1] == themoves[counter][1]:
                                        if cords == themoves[counter][2]:
                                            column = piece.position[1]
                                            Pieces.Piece.movePiece(piece,cords)
                                            drawPieces(screen,images,teams)
                                            #pygame.time.delay(250)
                                            found = True
                                            counter += 1 
                #if track == counter:
                    #pygame.time.delay(2500)
                if piece.name == "P":
                    if piece.position[0] == 0:
                        Pieces.Pawn.promotion(piece,themoves[counter])
                        counter+=1
                if not Pieces.King.kingattackedSquares(blackTeam,whiteTeam):
                    if Pieces.King.checkMate(blackTeam,whiteTeam):
                        print("Checkmate! Black wins.")
                    else:
                        if Pieces.King.checkMate(blackTeam,whiteTeam):
                            print("This is a draw.") 
                whiteTurn = False

                dead = False
                for posi in blackTeam:
                    if piece.position == posi.position:
                        blackTeam.remove(posi)
                        teams.remove(posi)
                        dead = True
                if dead == False:
                    if piece.name == "P":
                        if column != piece.position[1]:
                            for pie in whiteTeam:
                                if pie.position == lastc:   
                                    whiteTeam.remove(pie)
                                    teams.remove(pie)
                    elif piece.name == "K":
                        Pieces.Piece.castleRook(piece, column, whiteTeam)
                lastMove = piece
                lastc = piece.position
            setupBoard(screen,squareSize)
            drawPieces(screen,images,teams)
            pygame.display.flip()
            moves = []

        clock.tick(30)

        for event in pygame.event.get():
            # Quit the game if the player closes the window
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit() 
            if event.type == pygame.MOUSEBUTTONDOWN:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]                                

                for item in teams:
                    if 700-item.position[1]*100 < x < 800-item.position[1]*100:
                        if 700-item.position[0]*100 < y < 800-item.position[0]*100:
                            if item.team == "W":      
                                
                                setupBoard(screen,squareSize)
                                moves = Pieces.Piece.getpieceMoves(item,whiteTeam,blackTeam,lastMove)
                                highLightMoves(screen,moves,squareSize)
                                drawPieces(screen,images,teams)
                            else:

                                setupBoard(screen, squareSize)
                                moves = Pieces.Piece.getpieceMoves(item, blackTeam, whiteTeam, lastMove)
                                highLightMoves(screen, moves, squareSize)
                                drawPieces(screen, images, teams)

        connect = []
        connect.append(whiteTeam.copy())
        connect.append(blackTeam.copy())
        boardPositions.append(connect)
        pygame.display.update()   
        fps_controller.tick(24)


if __name__ == "__main__":
    main()
