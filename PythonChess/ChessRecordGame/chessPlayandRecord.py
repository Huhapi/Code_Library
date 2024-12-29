''' Daniel Hayes
3/18/23
This is the generated user interface for the chess program.'''
import pygame
import Pieces
import sys
import chessAI
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
    drawButtons(screen)


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

def drawButtons(screen):
    # Parameters the screen, the dictionary of images, and the piece to draw.
    # It draws the piece on the board in the position it is.

    locationOne = [800, 300]
    locationTwo = [800, 400]
    pic = pygame.transform.scale(pygame.image.load("C:\\Users\smidg\\.vscode\\BigProject\\images\\pic1.png"), (100,100))
    picTwo = pygame.transform.scale(pygame.image.load("C:\\Users\smidg\\.vscode\\BigProject\\images\\pic2.png"), (100,100))
    screen.blit(pic,locationOne)
    screen.blit(picTwo, locationTwo)

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
    # Initializing Toggle spots
    for spots in teams:
        connect.append(Pieces.Piece(spots.position,spots.name,spots.team))
    boardPositions = []
    boardPositions.append(connect) 
    #= [whiteTeam.copy(), blackTeam.copy()]
    #print(boardPositions)
    # Initialize PGN
    pgnBlack = ""
    # Initialize counter for moves.
    pgnMoves = 0
    # Initializing toggle counter
    toggle = 0
    # Move counter
    halfMoves = 0
    # Initialize Pygame
    pygame.init()

    # Set the window size
    window_size = (900, 800)

    # Create the window
    screen = pygame.display.set_mode(window_size)

    fps_controller = pygame.time.Clock()
    squareSize = 100
    # Setup Board squares
    setupBoard(screen, squareSize)
    # Load images
    images = loadImages(teams)
    # Initialize pieces
    drawPieces(screen,images,teams)
    pygame.display.flip()
    moves = []
    piece = Pieces.King([20,20],"K","D")
    lastMove = piece
    whiteTurn = True
    run = True
    movability = True
    while run:
        moved = False
        for event in pygame.event.get():
            # Quit the game if the player closes the window
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit() 
            if event.type == pygame.MOUSEBUTTONDOWN:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                if movability == True:
                    if len(moves) > 0:
                        if len(moves[0]) > 0:
                            for spots in moves:
                                if 700-spots[1]*100 < x < 800-spots[1]*100:
                                    if 700-spots[0]*100 < y < 800-spots[0]*100:
                                        if whiteTurn == True:
                                            if piece.team == "W":

                                                pgnMoves += 1
                                                shared = Pieces.Piece.sharedmove(piece,whiteTeam,blackTeam,lastMove,spots)
                                                pgnPrint = pgnloader.pgnSaver(piece.position,piece.name,spots,"W",pgnBlack,shared,pgnMoves)

                                                column = piece.position[1]
                                                Pieces.Piece.movePiece(piece,[spots[0],spots[1]])
                                                moved = True
                                                whiteTurn = False
                                                if piece.name == "P":
                                                    if piece.position[0] == 7:
                                                        Pieces.Pawn.promotion(piece)
                                                if not Pieces.King.kingattackedSquares(blackTeam,whiteTeam):
                                                    if Pieces.King.checkMate(blackTeam,whiteTeam):
                                                        print("You win!")
                                                else:
                                                    if Pieces.King.checkMate(blackTeam,whiteTeam):
                                                        print("This is a draw.")    
                                                
                                                
                                                dead = False
                                                for posit in blackTeam:
                                                    if piece.position == posit.position:
                                                        blackTeam.remove(posit)
                                                        teams.remove(posit)
                                                        dead = True
                                                if dead == False:
                                                    if piece.name == "P":
                                                        if column != piece.position[1]:
                                                            for spot in blackTeam:
                                                                if spot.position == lastc:
                                                                    blackTeam.remove(spot)
                                                                    teams.remove(spot)
                                                    elif piece.name == "K":
                                                        Pieces.Piece.castleRook(piece,column,whiteTeam)
                                                lastMove = piece
                                                lastc = piece.position                                      
                                            moves = []
                                            setupBoard(screen,squareSize)
                                            drawPieces(screen,images,teams)
                                            pygame.display.flip()                   
                                        else:
                                            if piece.team == "B":
                                                
                                                shared = Pieces.Piece.sharedmove(piece,blackTeam,whiteTeam,lastMove,spots)
                                                pgnBlack = pgnloader.pgnSaver(piece.position,piece.name,spots,"B",pgnPrint,shared,0)

                                                column = piece.position[1]
                                                Pieces.Piece.movePiece(piece,[spots[0],spots[1]])
                                                moved = True
                                                if piece.name == "P":
                                                    if piece.position[0] == 0:
                                                        Pieces.Pawn.promotion(piece)
                                                if not Pieces.King.kingattackedSquares(whiteTeam,blackTeam):
                                                    if Pieces.King.checkMate(whiteTeam,blackTeam):
                                                        print("You lose!")
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
                                            moves = []

# Piece move and highlighting.
                for item in teams:
                    if 700-item.position[1]*100 < x < 800-item.position[1]*100:
                        if 700-item.position[0]*100 < y < 800-item.position[0]*100:
                            if item.team == "W":      

                                setupBoard(screen,squareSize)
                                moves = Pieces.Piece.getpieceMoves(item,whiteTeam,blackTeam, lastMove)
                                highLightMoves(screen,moves,squareSize)
                                drawPieces(screen,images,teams)
                                piece = item

                            else:

                                setupBoard(screen,squareSize)
                                moves = Pieces.Piece.getpieceMoves(item,blackTeam,whiteTeam, lastMove)
                                highLightMoves(screen,moves,squareSize)
                                drawPieces(screen,images,teams)
                                piece = item
# Toggle Buttons
                if 800 < x < 900:   # x = 800, y = 400
                    if 300 < y < 400:   # 300
                        if halfMoves-toggle > 0:
                            movability = False
                            toggle += 1
                            #whiteTeam = boardPositions[halfMoves-toggle][0]
                            #blackTeam = boardPositions[halfMoves-toggle][1]
                            teams = boardPositions[halfMoves-toggle]
                            setupBoard(screen,squareSize)
                            drawPieces(screen,images,teams)
                            #print(boardPositions)
                            
                if 800 < x < 900:   # x = 800, y = 500
                    if 400 < y < 500:   # 400 
                        if toggle > 0:
                            movability = False
                            
                            toggle -= 1
                            #whiteTeam = boardPositions[halfMoves-toggle][0]
                            #blackTeam = boardPositions[halfMoves-toggle][1]
                            teams = boardPositions[halfMoves-toggle]
                            setupBoard(screen,squareSize)
                            drawPieces(screen,images,teams)
                if 800 < x < 900:   # x = 800, y = 200
                    if 200 < y < 300:   # 200 
                        print(moves)
                if 800 < x < 900:   # x = 800, y = 200
                    if 500 < y < 600:   # 200 
                        if whiteTurn == True:
                            pgnloader.writePgn(pgnBlack)
                        else:
                            pgnloader.writePgn(pgnPrint)

        # When back at position, moves can be made.
        # Teams is reset back to each team.

        if toggle == 0:
            teams = blackTeam+whiteTeam
            movability = True                    
        if moved == True:
            #connect = []
            #connect.append(whiteTeam.copy())
            #connect.append(blackTeam.copy())
            #[0,0],"R","W"
            parts = []
            for pos in teams:
                parts.append(Pieces.Piece(pos.position,pos.name,pos.team))
            boardPositions.append(parts)
            halfMoves += 1
                            

        pygame.display.update()   
        fps_controller.tick(24)


if __name__ == "__main__":
    main()
