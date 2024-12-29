""" Daniel Hayes
4/29/23
Loading a PGN file into the game."""

def reader(file):
    # Takes in file name.
    # reads in move and returns a list of list of moves.

    f = open(file,"r")

    filestring = f.read()
    castle = False
    catch = False
    moveList = []

    for char in filestring:

        if catch == True:
            if char.isnumeric():
                moveList.append(char)
        catch = False
        if castle == True:
            moveList.append(char)
        castle = False  
        if char == "O":
            moveList.append(char)
            castle = True
        elif char == "=":
            moveList.append(char)
        elif char.isupper():
            moveList.append(char)
        elif char.islower():
            if char != "x":
                moveList.append(char)
                catch = True
            
        elif char == "#":

            return(moveList)

    return(moveList)

def file(letter):
    # Takes in the extra letter for file of piece, or number file
    # Returns the Y value, or coordinate[1] of piece position, or the letter associated with file number. 

    if letter == "a":
        return 7
    if letter == "b":
        return 6
    if letter == "c":
        return 5
    if letter == "d":
        return 4
    if letter == "e":
        return 3
    if letter == "f":
        return 2
    if letter == "g":
        return 1
    if letter == "h":
        return 0
    
    if letter == 7:
        return "a"
    if letter == 6:
        return "b"
    if letter == 5:
        return "c"
    if letter == 4:
        return "d"
    if letter == 3:
        return "e"
    if letter == 2:
        return "f"
    if letter == 1:
        return "g"
    if letter == 0:
        return "h"

#piece.position,piece.name,spots,"W",shared,pgnMoves
def pgnSaver(initCoordinates,name,toCoordinates,team,pgnString,shared,number=0):
    # This function takes in a piece's position, it's name, it's move 
    # and a boolean on whether or not that move is shared with another piece of the same name on it's team.
    
    if team == "W":
        pgnString += str(number)+". "

    if name == "P":
        if shared:
            pgnString += file(initCoordinates[1])+file(toCoordinates[1])+str(toCoordinates[0]+1)+" "
        else:
            pgnString += file(toCoordinates[1])+str(toCoordinates[0]+1)+" "
    elif name == "K":
        if initCoordinates[1]+2 == toCoordinates[1]:
            pgnString += "0-0-0 "
        elif initCoordinates[1]-2 == toCoordinates[1]:
            pgnString += "0-0 "
        else:
            pgnString += file(toCoordinates[1])+str(toCoordinates[0]+1)+" "
    else:
        pgnString += name
        if shared:
            pgnString += file(initCoordinates[1])+file(toCoordinates[1])+str(toCoordinates[0]+1)+" "
        else:
            pgnString += file(toCoordinates[1])+str(toCoordinates[0]+1)+" "

    return pgnString
    
def writePgn(value):
    # This position takes the summed up PGN string
    # prints it to a file.
    report = open("PGNreport.txt","w")
    report.write(value)



def converter(spot):
    # This function takes in a string, a square in chess notation, or a coordinate.
    # returns the coordinates for the move, or the chess notation for the coordinate.
    squares = { "h8": [7,0],"h7": [6,0],"h6": [5,0],"h5": [4,0],"h4": [3,0],"h3": [2,0],"h2": [1,0],"h1": [0,0],
                "g8": [7,1],"g7": [6,1],"g6": [5,1],"g5": [4,1],"g4": [3,1],"g3": [2,1],"g2": [1,1],"g1": [0,1],
                "f8": [7,2],"f7": [6,2],"f6": [5,2],"f5": [4,2],"f4": [3,2],"f3": [2,2],"f2": [1,2],"f1": [0,2],
                "e8": [7,3],"e7": [6,3],"e6": [5,3],"e5": [4,3],"e4": [3,3],"e3": [2,3],"e2": [1,3],"e1": [0,3],
                "d8": [7,4],"d7": [6,4],"d6": [5,4],"d5": [4,4],"d4": [3,4],"d3": [2,4],"d2": [1,4],"d1": [0,4],
                "c8": [7,5],"c7": [6,5],"c6": [5,5],"c5": [4,5],"c4": [3,5],"c3": [2,5],"c2": [1,5],"c1": [0,5],
                "b8": [7,6],"b7": [6,6],"b6": [5,6],"b5": [4,6],"b4": [3,6],"b3": [2,6],"b2": [1,6],"b1": [0,6],
                "a8": [7,7],"a7": [6,7],"a6": [5,7],"a5": [4,7],"a4": [3,7],"a3": [2,7],"a2": [1,7],"a1": [0,7]}

    return(squares[spot])


def getList(filename= "PGNCastle.txt"):
    # Retrieves PGN file
    # Gets list of pieces and moves
    # Returns list

    moves = reader(filename)
   
    x = 0
    castle = ""
    moveList = []
    while x < len(moves)-1:
        queening = False
        if moves[x].islower():
            if len(moves) > x+2:
                if moves[x+2] == "=":
                    moveList.append(moves[x]+moves[x+1]+moves[x+2]+moves[x+3])
                    x += 3
                    queening = True
            if queening == False:
                if moves[x+1].isnumeric():
                    moveList.append(moves[x]+moves[x+1])
                    x+=1
                else:
                    moveList.append(moves[x]+moves[x+1]+moves[x+2])
                    x+=2
        elif moves[x] == "O":
            while moves[x] != " ":
                castle += moves[x]
                x+=1
            moveList.append(castle)
            castle = ""
        elif moves[x].isupper():
            moveList.append(moves[x])
        x+=1

    return(moveList)   

def movelist():
    # This function gets the updated list, and makes it usable for the game loop.
    deltaList = getList()
    connected = False
    move = []
    moveList = []

    for positions in deltaList:

        if connected == True:
            if len(positions) == 2:
                move.append(converter(positions))
            elif len(positions) == 3:
                move.append(file(positions[0]))
                move.append(converter(positions[1]+positions[2]))
            connected = False
        elif len(positions) == 2:
            move.append("P")
            move.append(converter(positions))
        elif len(positions) == 1:
            if positions[0].isupper():
                move.append(positions)
                connected = True
        elif len(positions) == 3:
            if positions[0].islower():
                move.append("P")
                move.append(converter(positions[1]+positions[2]))
            elif positions[0] == "O":
                move.append("K")
                if len(moveList)%2 == 0:
                    move.append([0,1])
                else:
                    move.append([7,1])
        elif len(positions) == 4:
            move.append("P")
            move.append(converter(positions[0]+positions[1]))
        elif positions[0] == "O":
            move.append("K")
            if len(moveList)%2 == 0:
                move.append([0,5])
            else:
                move.append([7,5])
        if connected == False:
            moveList.append(move)
            move = []

    return moveList

def main():
    print(movelist())


if __name__ == "__main__":
    main()


