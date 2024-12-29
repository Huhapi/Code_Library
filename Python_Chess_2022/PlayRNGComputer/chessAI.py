""" Daniel Hayes
4/23/23
This algorithm plays moves for black."""
import random
import PlayRNGComputer.Pieces as Pieces

def pickApiece(blackTeam,whiteTeam,lastMove):
    # This function takes in both teams list of pieces, and the last move.
    # It returns a piece with a legal move available.
    move = False
    count = 0
    while move == False:
        piecenumb = random.randint(0,len(blackTeam)-1)
        item = blackTeam[piecenumb]

        if item.name == "R":
            moves = Pieces.Rook.rookMoves(item,blackTeam,whiteTeam)

        elif item.name == "P":
            moves = Pieces.Pawn.pawnMoves(item, blackTeam, whiteTeam, lastMove)

        elif item.name == "B":
            moves = Pieces.Bishop.bishopMoves(item, blackTeam, whiteTeam)

        elif item.name == "Q":
            moves = Pieces.Queen.queenMoves(item, blackTeam, whiteTeam)

        elif item.name == "N":
            moves = Pieces.Knight.knightMoves(item, blackTeam, whiteTeam)

        elif item.name == "K":
            moves = Pieces.King.kingMoves(item, blackTeam, whiteTeam)

        count += 1
        if count > 150:
            return(False)
        if len(moves) > 0:
            return item

def pickAmove(item, blackTeam, whiteTeam, lastMove):
    # This function takes in a piece, and randomly selects a move for that piece.
    # Parameters are the piece object, the list of pieces blackTeam, list of pieces whiteTeam, and the last move.
    
    if item.name == "R":
        moves = Pieces.Rook.rookMoves(item,blackTeam,whiteTeam)

    elif item.name == "P":
        moves = Pieces.Pawn.pawnMoves(item, blackTeam, whiteTeam, lastMove)

    elif item.name == "B":
        moves = Pieces.Bishop.bishopMoves(item, blackTeam, whiteTeam)

    elif item.name == "Q":
        moves = Pieces.Queen.queenMoves(item, blackTeam, whiteTeam)

    elif item.name == "N":
        moves = Pieces.Knight.knightMoves(item, blackTeam, whiteTeam)

    elif item.name == "K":
        moves = Pieces.King.kingMoves(item, blackTeam, whiteTeam)

    if len(moves)> 1:
        spot = random.randint(0,len(moves)-1)
        return(moves[spot])
    else:
        return(moves[0])

def main():
    pass


if __name__ == "__main__":
    main()
