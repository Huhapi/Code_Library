'''Daniel Hayes
3/18/23
Class to create Piece objects.'''

class Piece:
    # This class will be the underlying piece objects in the game.

    def __init__(self, position, name, team):
        # Initialize piece values.
        self.position = position
        self.moved = 0
        self.name = name
        self.team = team

    def moveUp(self, team, enemyTeam):
        # This function has parameters the object in itself, list of lists own team, and list of lists enemy team.
        # It returns the positions upwards a piece can move (rook or queen) 
        x = self.position[0]+1
        move = True
        capture = True
        moveSquares = []

        while x < 8:
            for pos in team+enemyTeam:
                if [x, self.position[1]]== pos.position:
                    if pos.team != self.team:
                        capture = False
                    else:
                        move = False
            if move == True:
                if capture == False:
                    moveSquares.append([x, self.position[1]])
                    x = 8
                else:
                    moveSquares.append([x, self.position[1]])
                x += 1
            else:
                x = 8
        return(moveSquares)


    def moveDown(self, team, enemyTeam):
        # This function has parameters the object in itself, list of lists own team, and list of lists enemy team.
        # It returns the positions downwards a rook or queen can move. 
        x = self.position[0]-1
        move = True
        capture = True
        moveSquares = []

        while x >= 0:
            for pos in team+enemyTeam:
                if [x, self.position[1]]== pos.position:
                    if pos.team != self.team:
                        capture = False
                    else:
                        move = False
            if move == True:
                if capture == False:
                    moveSquares.append([x, self.position[1]])
                    x = -1
                else:
                    moveSquares.append([x, self.position[1]])
                x -= 1
            else:
                x = -1
        return(moveSquares)
    
    def moveLeft(self, team, enemyTeam):
        # This function has parameters the object in itself, list of lists own team, and list of lists enemy team. 
        # It returns the positions left a rook or queen can move.
        y = self.position[1]-1
        move = True
        capture = True
        moveSquares = []

        while y > -1:
            for pos in team+enemyTeam:
                if [self.position[0], y]== pos.position:
                    if pos.team != self.team:
                        capture = False
                    else:
                        move = False
            if move == True:
                if capture == False:
                    moveSquares.append([self.position[0], y])
                    y = -1
                else:
                    moveSquares.append([self.position[0], y])
                y -= 1
            else:
                y = -1
        return(moveSquares)
    
    def moveRight(self, team, enemyTeam):
        # This function has parameters the object in itself, list of lists own team, and list of lists enemy team. 
        # It returns the positions right a rook or queen can move.

        y = self.position[1]+1
        move = True
        capture = True
        moveSquares = []

        while y < 8:
            for pos in team+enemyTeam:
                if [self.position[0], y]== pos.position:
                    if pos.team != self.team:
                        capture = False
                    else:
                        move = False
            if move == True:
                if capture == False:
                    moveSquares.append([self.position[0], y])
                    y = 8
                else:
                    moveSquares.append([self.position[0], y])
                y += 1
            else:
                y = 8
        return(moveSquares)


    def moveUpright(self, team, enemyTeam):
        # This function has parameters the object in itself, list of lists own team, and list of lists enemy team.
        # It returns the positions a bishop or queen can move up right.
        x = self.position[0]+1
        y = self.position[1]+1
        moveSquares = []
        capture = True
        move = True

        while x < 8 and y < 8:
            for pos in team+enemyTeam:
                if [x,y] == pos.position:
                    if pos.team != self.team:
                        capture = False
                    else:
                        move = False
            if move == True:
                if capture != True:
                    moveSquares.append([x, y])
                    x = 8
                else:
                    moveSquares.append([x, y])
            else:
                x = 8
            x += 1
            y += 1
        return(moveSquares)
                    

    def moveDownleft(self, team, enemyTeam):
        # This function has parameters the object in itself, list of lists own team, and list of lists enemy team.
        # It returns the positions a bishop or queen can move down left.
        x = self.position[0]-1
        y = self.position[1]+1
        moveSquares = []
        capture = True
        move = True

        while x > -1 and y < 8:
            for pos in team+enemyTeam:
                if [x,y] == pos.position:
                    if pos.team != self.team:
                        capture = False
                    else:
                        move = False
            if move == True:
                if capture != True:
                    moveSquares.append([x, y])
                    y = 8
                else:
                    moveSquares.append([x, y])
            else:
                y = 8
            x -= 1
            y += 1
        return(moveSquares)

    def moveUpleft(self, team, enemyTeam):
        # This function has parameters the object in itself, list of lists own team, and list of lists enemy team.
        # It returns the positions a biship or queen can move up left.
        x = self.position[0]+1
        y = self.position[1]-1
        moveSquares = []
        capture = True
        move = True

        while x < 8 and y > -1:
            for pos in team+enemyTeam:
                if [x,y] == pos.position:
                    if pos.team != self.team:
                        capture = False
                    else:
                        move = False
            if move == True:
                if capture != True:
                    moveSquares.append([x, y])
                    x = 8
                else:
                    moveSquares.append([x, y])
            else:
                x = 8
            x += 1
            y -= 1
        return(moveSquares)


    def moveDownright(self, team, enemyTeam):
        # This function has parameters the object in itself, list of lists own team, and list of lists enemy team.
        # It returns the positions a bishop or queen can move down right.
        x = self.position[0]-1
        y = self.position[1]-1
        moveSquares = []
        capture = True
        move = True

        while x > -1 and y > -1:
            for pos in team+enemyTeam:
                if [x,y] == pos.position:
                    if pos.team != self.team:
                        capture = False
                    else:
                        move = False
            if move == True:
                if capture != True:
                    moveSquares.append([x, y])
                    x = -1
                else:
                    moveSquares.append([x, y])
            else:
                x = -1
            x -= 1
            y -= 1
        return(moveSquares)
    
    def spotChecker(moves, friendlyTeam):
        #This function takes in moves on the board, and it's team list of piece objects.
        #It returns a list of moves where teammates are not.
        moveList = []
        
        for coordinates in moves:
            move = True
            for pos in friendlyTeam:
                if coordinates == pos.position:
                    move = False
            if move == True:
                moveList.append(coordinates)
        return(moveList)
    
    def castleRook(self, column, team):
        # This function takes in: a piece object through self
        #                       The Y position of the king prior to moving
        #                       The list of objects for that piece team.
        # Changes the rook position but returns nothing.
        if self.team == "B":
            if self.position[1]-column == 2:
                for it in team:
                    if it.position == [7,7]:
                        it.position = [7,4]
            elif column - self.position[1]  == 2:
                for them in team:
                    if them.position == [7,0]:
                        them.position = [7,2]
        else:
            if self.position[1]-column == 2:
                for it in team:
                    if it.position == [0,7]:
                        it.position = [0,4]
            elif column - self.position[1]  == 2:
                for them in team:
                    if them.position == [0,0]:
                        them.position = [0,2]

    def sharedmove(piece, team, enemyteam,lastMove,theMove):
        # This function takes in the piece which is being moved, it's team - list of piece objects,
        # the enemy team, list of piece objects, the last move, the move to check.
        # Returns a boolean, whether this piece shares a move with another on it's team.
        for mates in team:
            if piece.name == mates.name:
                if piece != mates:
                    moves = Piece.getpieceMoves(piece,team,enemyteam,lastMove)
                    for spots in moves:
                        if spots == theMove:
                            return True
        return False
    
    def movePiece(self,coordinates,y = 0):
        # This function will make a piece move to desired coordinates.
        # Parameters Piece and coordinates

        self.position = coordinates
        self.moved += y+1

    def getpieceMoves(self, team, enemyTeam,lastMove):
        # This function take in a piece object and both teams,
        # lists of pieces, and the lastMove
        # Returns possible moves for that piece.

        if self.name == "R":

            moves = Rook.rookMoves(self,team,enemyTeam)

        elif self.name == "P":

            moves = Pawn.pawnMoves(self,team,enemyTeam,lastMove)

        elif self.name == "B":

            moves = Bishop.bishopMoves(self,team,enemyTeam)

        elif self.name == "Q":

            moves = Queen.queenMoves(self,team,enemyTeam)

        elif self.name == "N":

            moves = Knight.knightMoves(self,team,enemyTeam)

        elif self.name == "K":

            moves = King.kingMoves(self,team,enemyTeam)
        
        return moves

class Pawn(Piece):
   
    def promotion(self,name=["Q"]):
        # This function takes in a pawn object and promotes it to a Queen. 
        self.name = name[0]

    def pawnMoves(self, team, enemyTeam, lastmovedPiece, check = 0):
        # Parameters are the piece object, and both list of lists team piece object. 
    # This function returns possible pawn moves as lists of lists depending on the team, location and other pieces locations.
        # The direction it moves depends on which team it is on.
        blocked = False
        if self.team == "W":
            pMoves = pawnAttacks(self, enemyTeam,lastmovedPiece)
            for pos in team+enemyTeam:
                # If there is a piece in the sqare a pawn wants to move it cannot move there.
                if pos.position == [self.position[0]+1,self.position[1]]:
                   blocked = True
            # Since the return function was not used, moving one step was possible, now to check if two steps possible
            if blocked == False:
                if self.position[0] == 1:
                    for pos in team+enemyTeam:
                        if pos.position == [self.position[0]+2,self.position[1]]:
                            pMoves.append([self.position[0]+1,self.position[1]])
                            blocked = True
                    if blocked == False:
                        pMoves.append([self.position[0]+1,self.position[1]])
                        pMoves.append([self.position[0]+2,self.position[1]])
                else:
                    pMoves.append([self.position[0]+1,self.position[1]])
        else:
            pMoves = pawnAttacks(self, enemyTeam,lastmovedPiece)
            for pos in team+enemyTeam:
                if pos.position == [self.position[0]-1,self.position[1]]:
                    blocked = True
            if blocked == False:    
                if self.position[0] == 6:
                    for pos in team+enemyTeam:
                        if pos.position == [self.position[0]-2,self.position[1]]:
                            blocked = True
                            pMoves.append([self.position[0]-1,self.position[1]])
                    if blocked == False:
                        pMoves.append([self.position[0]-1,self.position[1]])
                        pMoves.append([self.position[0]-2,self.position[1]])
                else:
                    pMoves.append([self.position[0]-1,self.position[1]])

        for spots in team:
            if spots.name == "K":
                king = spots

        finalPmoves = []
        theSpot = self.position
        if check == 0:
            for pos in pMoves:
                self.position = pos
                if King.kingattackedSquares(team, enemyTeam, self, king.position):
                    finalPmoves.append(pos)
            self.position = theSpot
            return(finalPmoves)
        else:
            return pMoves

            
def pawnAttacks(self, enemyTeam,lastMovedPiece):
# This function take in the pawn object in question, the list of pieces enemy team, the last move coordinates, and last piece moved.
# It returns a list of lists attack squares for the piece.
    moves = []

    if self.team == "W":
        if self.position[0] == 4:
                if lastMovedPiece.name == "P":
                    if lastMovedPiece.moved == 1:
                        if lastMovedPiece.position[0] == 4:
                            if lastMovedPiece.position[1] == self.position[1]-1 or lastMovedPiece.position[1] == self.position[1]+1:
                                moves.append([self.position[0]+1,lastMovedPiece.position[1]])
        for pos in enemyTeam:
            if [self.position[0]+1,self.position[1]-1] == pos.position:
                moves.append([self.position[0]+1,self.position[1]-1])
            if [self.position[0]+1,self.position[1]+1] == pos.position:
                moves.append([self.position[0]+1,self.position[1]+1])
        return(moves)
    elif self.team == "B":
        if self.position[0] == 3:
                if lastMovedPiece.name == "P":
                    if lastMovedPiece.moved == 1:
                        if lastMovedPiece.position[0] == 3:
                            if lastMovedPiece.position[1] == self.position[1]-1 or lastMovedPiece.position[1] == self.position[1]+1:
                                moves.append([self.position[0]-1,lastMovedPiece.position[1]])
        for pos in enemyTeam:
            if [self.position[0]-1,self.position[1]-1] == pos.position:
                moves.append([self.position[0]-1,self.position[1]-1])
            if [self.position[0]-1,self.position[1]+1] == pos.position:
                moves.append([self.position[0]-1,self.position[1]+1])
        
        return(moves)

def enPassant(self, lastMovedPiece):
    pass

class Knight(Piece):


    def knightMoves(self, team, enemyTeam, check = 0):
    # This function determines possible knight moves.
    # Parameters are the piece in question, and the list of teams.
    # Returns a list of possible moves.
        xrbig = self.position[0]+2
        xlbig = self.position[0]-2
        xlsmall = self.position[0]-1
        xrsmall = self.position[0]+1
        yrsmall = self.position[1]+1
        ylsmall = self.position[1]-1
        ylbig = self.position[1]-2
        yrbig = self.position[1]+2
        moveList = []
        # Tracking knight moves that are on the board.
        if -1 < xrbig < 8:
            if -1 < yrsmall < 8:
                moveList.append([xrbig,yrsmall])
            if -1 < ylsmall < 8:
                moveList.append([xrbig,ylsmall])
        if -1 < xlbig < 8:
            if -1 < yrsmall < 8:
                moveList.append([xlbig,yrsmall])
            if -1 < ylsmall < 8:
                moveList.append([xlbig,ylsmall])
        if -1 < xrsmall < 8: 
            if -1 < yrbig < 8:
                moveList.append([xrsmall,yrbig])
            if -1 < ylbig < 8:
                moveList.append([xrsmall,ylbig])
        if -1 < xlsmall < 8:
            if -1 < yrbig < 8:
                moveList.append([xlsmall,yrbig])
            if -1 < ylbig < 8:
                moveList.append([xlsmall,ylbig])

        nMoves = Piece.spotChecker(moveList,team)

        for spots in team:
            if spots.name == "K":
                king = spots

        finalNmoves = []
        theSpot = self.position
        if check == 0:
            for pos in nMoves:
                self.position = pos
                if King.kingattackedSquares(team, enemyTeam,self, king.position):
                    finalNmoves.append(pos)
            self.position = theSpot
            return(finalNmoves)
        else:
            return nMoves
    
    
class Bishop(Piece):


    def bishopMoves(self, team, enemyTeam, check = 0):
    # This function determines possible bishop moves.
    # Parameters are the piece in question, and the list of teams.
    # Returns a list of possible moves.
        bishopMoves = self.moveUpleft(team, enemyTeam)+self.moveDownleft(team, enemyTeam)+self.moveDownright(team, enemyTeam)+self.moveUpright(team, enemyTeam)
        
        for spots in team:
            if spots.name == "K":
                king = spots

        finalBmove = []
        theSpot = self.position
        if check == 0:
            for pos in bishopMoves:
                self.position = pos
                if King.kingattackedSquares(team, enemyTeam, self, king.position):
                    finalBmove.append(pos)
            self.position = theSpot
            return(finalBmove)
        else:
            return bishopMoves
        
           
class Rook(Piece):


    def rookMoves(self, team, enemyTeam, check = 0):
    # This function determines possible Rook moves.
    # Parameters are the piece in question, and the list of teams.
    # Returns a list of possible moves.

        rookm = self.moveUp(team, enemyTeam)+self.moveDown(team, enemyTeam)+self.moveLeft(team, enemyTeam)+self.moveRight(team, enemyTeam)

        for spots in team:
            if spots.name == "K":
                king = spots

        finalRmove = []
        theSpot = self.position
        if check == 0:
            for pos in rookm:
                self.position = pos
                if King.kingattackedSquares(team, enemyTeam, self, king.position):
                    finalRmove.append(pos)
            self.position = theSpot
            return(finalRmove)
        else:
            return rookm
        
class Queen(Piece):


    def queenMoves(self, team, enemyTeam, check = 0):
    # This function determines possible queen moves.
    # Parameters are the piece in question, and the lists of teams.
    # Returns a list of possible moves.
        queenMoves = self.moveUp(team, enemyTeam)+self.moveDown(team, enemyTeam)+self.moveLeft(team, enemyTeam)+self.moveRight(team, enemyTeam)+self.moveUpright(team, enemyTeam)+self.moveDownleft(team, enemyTeam)+self.moveDownright(team, enemyTeam)+self.moveUpleft(team, enemyTeam) 

        finalQueenMoves = []

        for posi in team:
            if posi.name == "K":
                king = posi

        theSpot = self.position

        if check == 0:
            for pos in queenMoves:
                self.position = pos
                if King.kingattackedSquares(team, enemyTeam,self, king.position):
                    finalQueenMoves.append(pos)
            self.position = theSpot
            return(finalQueenMoves)
        else:
            return queenMoves

class King(Piece):
        

        def kingMoves(self, team, enemyTeam):
        # This function determines possible Rook moves.
        # Parameters are the piece in question, and the list of teams.
        # Returns a list of possible moves.
            moves = []

            for x in range(-1,2):
                for y in range(-1,2):
                    if x != 0 or y != 0:
                        if -1 < (self.position[0]+x) < 8:
                            if -1 < (self.position[1]+y) < 8:
                                moves.append([self.position[0]+x,self.position[1]+y])
            # Accounts for board space
            castlingS = False
            castlingL = False

            if self.moved == 0:
                for piece in team:
                    if piece.name == "R":
                        if piece.moved == 0:
                            if piece.position == [self.position[0],self.position[1]-3]:
                                castlingS = True
                            if piece.position == [self.position[0],self.position[1]+4]:
                                castlingL = True
                for pieces in team+enemyTeam:
                    if pieces.position == [self.position[0],self.position[1]-1] or pieces.position == [self.position[0],self.position[1]-2]:
                        castlingS = False
                    if pieces.position == [self.position[0],self.position[1]+1] or pieces.position == [self.position[0],self.position[1]+2] or piece.position == [self.position[0],self.position[1]+3]:
                        castlingL = False
                if not King.kingattackedSquares(team,enemyTeam,self,self.position):
                    castlingL = False
                    castlingS = False
                     
                if self.team == "W":
                    if castlingS == True:
                        if len(moves)> 0:
                            for places in moves:
                                if places == [0,2]:
                                    moves.append([0,1])
                    if castlingL == True:
                        if len(moves)> 0:
                            for posits in moves:
                                if posits == [0,4]:
                                    moves.append([0,5])
                else:
                    if castlingS == True:
                        if len(moves)> 0:
                            for dots in moves:
                                if dots == [7,2]:
                                    moves.append([7,1])
                    if castlingL == True:
                        if len(moves)> 0:
                            for coords in moves:
                                if coords == [7,4]:
                                    moves.append([7,5])
  
            ########Need to encorporate enemy attack squares here############
            #spot checker accounts for friendly Pieces
            safeSpots = []
            x = Piece.spotChecker(moves,team)
            coreSpot = self.position
            for spots in x:
                self.position = spots
                if King.kingattackedSquares(team,enemyTeam,self,spots):
                    safeSpots.append(spots)
            self.position = coreSpot
            
            return(safeSpots)
        
        def kingattackedSquares(team, enemyTeam, self= Pawn([10,10],"K","D"), move = 0):
            # This function takes in the king piece, it's team, a list of piece objects and enemy team, another list of objects.
            # It returns total possible king moves, a list of coordinates.

            samesquare = False
            for things in enemyTeam:
                if self.position == things.position:
                    moveback = things.position
                    piece = things
                    samesquare = True
                    things.position = [11,11]

            enemymoves = []
            for pieces in enemyTeam:

                if pieces.name == "R": 
                    enemymoves = enemymoves+Rook.rookMoves(pieces, enemyTeam, team,1)

                elif pieces.name == "P":
                    lastMove = Bishop([12,12],"W","W")           
                    enemymoves = enemymoves+Pawn.pawnMoves(pieces, enemyTeam, team, lastMove,1)

                elif pieces.name == "B":
                    enemymoves = enemymoves+Bishop.bishopMoves(pieces, enemyTeam, team,1)
                                    
                elif pieces.name == "Q":
                    enemymoves = enemymoves+Queen.queenMoves(pieces, enemyTeam, team,1)
                                        
                elif pieces.name == "N":
                    enemymoves = enemymoves+Knight.knightMoves(pieces, enemyTeam, team,1)

                elif pieces.name == "K":
                    
                    for x in range(-1,2):
                        for y in range(-1,2):
                            if x != 0 or y != 0:
                                if -1 < (pieces.position[0]+x) < 8:
                                    if -1 < (pieces.position[1]+y) < 8:
                                        enemymoves.append([pieces.position[0]+x,pieces.position[1]+y])

            if samesquare == True:
                piece.position = moveback

            if move != 0:
                for spots in enemymoves:
                    if spots == move:
                        return(False)
            else:
                for king in team:
                    if king.name == "K":
                        move = king.position
                for spots in enemymoves:
                    if spots == move:
                        return(False)
                
            return(True)
        
        def checkMate(team, enemyTeam):
            # When the king is attacked, this function is called to check for checkmate and determine the game is over.
            # Parameters: team - list of piece and enemyTeam - list of pieces.
            
            moves = []
            for piece in team:
                if piece.name == "R": 
                    moves = moves+Rook.rookMoves(piece, team, enemyTeam)

                elif piece.name == "P":
                    lastMove = Bishop([12,12],"W","W")           
                    moves = moves+Pawn.pawnMoves(piece, team, enemyTeam, lastMove)

                elif piece.name == "B":
                    moves = moves+Bishop.bishopMoves(piece, team, enemyTeam)
                                    
                elif piece.name == "Q":
                    moves = moves+Queen.queenMoves(piece, team, enemyTeam)
                                        
                elif piece.name == "N":
                    moves = moves+Knight.knightMoves(piece, team, enemyTeam)

                elif piece.name == "K":
                    moves = moves+ King.kingMoves(piece, team, enemyTeam)

            if moves == []:
                return(True)
            else:
                return(False)                

            




