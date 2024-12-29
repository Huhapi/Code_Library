""" Daniel Hayes
4/5/2023
This python file is for testing the piece moves in the class Pieces."""
import PlayRNGComputer.Pieces as Pieces
import PlayRNGComputer.chessPlayRNG as chessPlayRNG

def testpawnMoves(piece, friendlyTeam, enemyTeam, lMove, expected):
    # This function tests possible pawn moves function.
    x = Pieces.Pawn.pawnMoves(piece,friendlyTeam,enemyTeam,lMove)
    if x == expected:
        print("Correct")
    else:
        print("Incorrect pawnMoves")
        print(x)

def testmovePiece(piece, coordinates,expected):
    Pieces.Piece.movePiece(piece,coordinates)
    if expected == piece.position:
        print("Correct")
    else:
        print("Incorrect movePiece")
        print(piece.position)

def testmoveUp(piece, friendlyTeam, enemyTeam, expected):
    # This function will test the moveUp function in Pieces.
    # Parameters: Piece to move, List of Friendly Pieces, List of enemy Pieces, and expected return values.
    x = Pieces.Piece.moveUp(piece,friendlyTeam,enemyTeam)
    
    if x == expected:
        print("Correct.")
    else:
        print("Incorrect moveUp")
        print(x)

def testmoveDown(piece, friendlyTeam, enemyTeam, expected):
    # This function will test the moveDown function in Pieces.
    # Parameters: Piece to move, List of Friendly Pieces, List of enemy Pieces, and expected return values.

    if Pieces.Rook.moveDown(piece,friendlyTeam,enemyTeam)== expected:
        print("correct")
    else:
        print("Incorrect moveDown")
        print(Pieces.Piece.moveDown(piece,friendlyTeam,enemyTeam))

def testmoveLeft(piece, friendlyTeam, enemyTeam, expected):
    # This function will test the moveLeft function in Pieces.
    # Parameters: Piece to move, List of Friendly Pieces, List of enemy Pieces, and expected return values.
    x = Pieces.Piece.moveLeft(piece,friendlyTeam,enemyTeam)
    if x == expected:
        print("correct")
    else:
        print("Incorrect moveLeft")
        print(x)

def testmoveRight(piece, friendlyTeam, enemyTeam, expected):
    # This function will test the moveRight function in Pieces.
    # Parameters: Piece to move, List of Friendly Pieces, List of enemy Pieces, and expected return values.
    x = Pieces.Piece.moveRight(piece,friendlyTeam,enemyTeam)
    if x == expected:
        print("Correct")
    else:
        print("Incorrect moveRight")
        print(x)

def testmoveUpright(piece, friendlyTeam, enemyTeam, expected):
    # This function will test the moveUpright function in Pieces.
    # Parameters: Piece to move, List of Friendly Pieces, List of enemy Pieces, and expected return values.
    x = Pieces.Piece.moveUpright(piece,friendlyTeam,enemyTeam)
    if x == expected:
        print("Correct")
    else:
        print("Incorrect moveUpright")
        print(x)

def testmoveDownright(piece, friendlyTeam, enemyTeam, expected):
    # This function will test the moveDownright function in Pieces.
    # Parameters: Piece to move, List of Friendly Pieces, List of enemy Pieces, and expected return values.
    x = Pieces.Piece.moveDownright(piece,friendlyTeam,enemyTeam)
    if x == expected:
        print("Correct")
    else:
        print("Incorrect moveDownright")
        print(x)

def testmoveUpleft(piece, friendlyTeam, enemyTeam, expected):
    # This function will test the moveUpleft function in Pieces.
    # Parameters: Piece to move, List of Friendly Pieces, List of enemy Pieces, and expected return values.
    x = Pieces.Piece.moveUpleft(piece,friendlyTeam,enemyTeam)
    if x == expected:
        print("Correct")
    else:
        print("Incorrect moveUpleft")
        print(x)

def testmoveDownleft(piece, friendlyTeam, enemyTeam, expected):
    # This function will test the moveDownleft function in Pieces.
    # Parameters: Piece to move, List of Friendly Pieces, List of enemy Pieces, and expected return values.
    x = Pieces.Piece.moveDownleft(piece,friendlyTeam,enemyTeam)
    if x == expected:
        print("Correct")
    else:
        print("Incorrect moveDownleft")
        print(x)

def testkingMoves(self,team,enemyTeam,moves):
    # This function tests kingMoves.
    # Parameters are self, list of pieces team, list of pieces enemy team, and a list of coordinate lists.
    # Prints out correct or incorrect.
    x = Pieces.King.kingMoves(self,team,enemyTeam)
    if x == moves:
        print("Correct")
    else:
        print("incorrect kingMoves")
        print(x)

def testkingattackedSquares(self,moves,team,enemyTeam,expected):
    y = Pieces.King.kingattackedSquares(self, moves, team, enemyTeam)

    if y == expected:
        print("Correct")
    else:
        print("Incorrect")
        print(y)

def main():
    # this will create pieces and scenarios which then call the above test methods.
    z = chessPlayRNG.initializeBlackpieces()
    y = chessPlayRNG.initializeWhitepieces()

    piece = Pieces.King([10,10],"K","D")
    testpawnMoves(y[8],y,z,piece,[[2,0],[3,0]])
    # Testing moving a pawn
    testmovePiece(y[8],[3,0],[3,0])
    # Testing moveUp for friendly pieces moving out of the way.
    testmoveUp(y[0], y, z, [[1,0],[2,0]])
    testmovePiece(y[0],[2,0],[2,0])
    testmovePiece(y[0],[2,4],[2,4])
    # Testing moveUp for enemy piece threatening.
    testmoveUp(y[0], y, z, [[3, 4],[4, 4],[5, 4],[6, 4]])

    testpawnMoves(z[12],y,z,piece,[[5,4],[4,4]])
    testmovePiece(z[12],[4,4],[4,4])
    testmoveDownleft(z[3],y,z,[[6,4],[5,5],[4,6],[3,7]])
    testmovePiece(z[3],[5,5],[5,5])
    testmoveDownleft(z[3],y,z,[[4,6],[3,7]])
    testmoveRight(z[3],y,z,[[5,6],[5,7]])
    testmoveLeft(z[3],y,z,[[5, 4], [5, 3], [5, 2], [5, 1], [5, 0]])
    testmoveUp(z[3],y,z,[])
    testmoveDown(z[3],y,z,[[4, 5], [3, 5], [2, 5], [1, 5]])
    testmoveDownleft(z[3],y,z,[[4, 6], [3, 7]])
    testmoveUpleft(z[3],y,z,[[6, 4], [7, 3]])
    # Pawn is blocking queen moves Downright
    testmoveDownright(z[3],y,z,[])
    testmoveUpright(z[3],y,z,[])
    # Checking pawnmoves
    u = testpawnMoves(z[12],y,z,piece,[[3,4]])
    # Moving Pawn out of way of queen
    testmovePiece(z[12],[3,4],[3,4])
    # Queen moveDownright changed from nothing to below. Stops at enemy pawn on [1,1]
    testmoveDownright(z[3],y,z,[[4, 4], [3, 3], [2, 2], [1, 1]])
    # Testing black Bishop move downright.
    testmoveDownright(z[5],y,z,[[6, 4], [5, 3], [4, 2], [3, 1], [2, 0]])
    testmovePiece(z[5],[4,2],[4,2])
    # stops at the edge of the board [2,0]
    testmoveDownright(z[5],y,z,[[3, 1], [2, 0]])
    # This bishop is attacking the white rook on [2,4] moved back on line 125:
    testmoveDownleft(z[5],y,z,[[3, 3], [2, 4]])
    # The Bishops stops prior to pawns on own team:
    testmoveUpleft(z[5],y,z,[[5, 1]])
    # Can move back to original position:
    testmoveUpright(z[5],y,z,[[5, 3], [6, 4], [7, 5]])
    
    testpawnMoves(y[8],y,z,piece,[[4, 0]])# Previously pushed to [3,0]
    testpawnMoves(y[9],y,z,piece,[[2, 1], [3, 1]])#The rest are at starting position with no blocks.
    testpawnMoves(y[10],y,z,piece,[[2, 2], [3, 2]])
    testpawnMoves(y[11],y,z,piece,[[2, 3], [3, 3]])
    testmovePiece(y[11],[3, 3], [3, 3])
    piece = y[11]
    testpawnMoves(y[12],y,z,piece,[]) #There's a rook on [2,4]
    testpawnMoves(y[13],y,z,piece,[[2, 5], [3, 5]])
    testpawnMoves(y[14],y,z,piece,[[2, 6], [3, 6]])
    testpawnMoves(y[15],y,z,piece,[[2, 7], [3, 7]])

    # Testing King moves
    testkingMoves(y[3],y,z,[[1, 3]])
    #testmovePiece()
    # moving queen from [0,2] to [1,3]
    testmovePiece(y[2],[1, 3],[1, 3])


    wking = Pieces.King([0,3],"K","W") 
    
    squares = {"h8" :[7,0],"h7": [6,0],"h6": [5,0],"h5": [4,0],"h4": [3,0],"h3": [2,0],"h2": [1,0],"h1": [0,0],
                "g8": [7,1],"g7": [6,1],"g6": [5,1],"g5": [4,1],"g4": [3,1],"g3": [2,1],"g2": [1,1],"g1": [0,1],
                "f8": [7,2],"f7": [6,2],"f6": [5,2],"f5": [4,2],"f4": [3,2],"f3": [2,2],"f2": [1,2],"f1": [0,2],
                "e8": [7,3],"e7": [6,3],"e6": [5,3],"e5": [4,3],"e4": [3,3],"e3": [2,3],"e2": [1,3],"e1": [0,3],
                "d8": [7,4],"d7": [6,4],"d6": [5,4],"d5": [4,4],"d4": [3,4],"d3": [2,4],"d2": [1,4],"d1": [0,4],
                "c8": [7,5],"c7": [6,5],"c6": [5,5],"c5": [4,5],"c4": [3,5],"c3": [2,5],"c2": [1,5],"c1": [0,5],
                "b8": [7,6],"b7": [6,6],"b6": [5,6],"b5": [4,6],"b4": [3,6],"b3": [2,6],"b2": [1,6],"b1": [0,6],
                "a8": [7,7],"a7": [6,7],"a6": [5,7],"a5": [4,7],"a4": [3,7],"a3": [2,7],"a2": [1,7],"a1": [0,7]}

    square = 6
    coordinates = squares[square]



if __name__ == "__main__":
    main()
