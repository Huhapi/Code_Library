Daniel Hayes
zMUD Final Project

Ideas of the program:
The ideas of this program are to explore recursive creation of a random map as well as
object oriented programming in C++ through making a zMUD game. 

Instructions to run the program:
Compile and run the driver.cpp C++ file:
g++ driver.cpp
./a.ext

Purpose of the program:
This program creates a random map of rooms, with items and monsters. You are the player
Which starts in a room and the goal of the game is for the player to fight past the monsters
and escape! - Which is via accessing a specific room in the map.

Details of environment for running the code:
This requires C++ to be installed so that it can compile and run the program.

Context:
I have little experience in working in C++. I wanted to explore some of the more
complicated ways of working with objects in a language I am unfamiliar with in 
order to gain competency and experience working in C++. I have worked in C, and
it is nice to have the std string library!

Reflection: - Mention random generation and potential for failure
Randomly generating a map on a two dimensional field is kind of complex - as it does 
not allow for rooms to have the same coordinates. As I was trying to make a straight run
of a certain distance from start to the winning room - if by chance the only exits to
consecutive rooms are something like North, North, East, East, South, South, West, North
the path has circled around on itself. 
|--
|@|
*|-
I am not sure I solved this specific example, but it is a rare occurrence - made even more rare 
by the way directions are selected for a room.

Sources Appendix:
I used AI for syntax. It was helpful in getting C++ to do what I wished, but otherwise I have
previous experience working with Object oriented programs, and it seems C++ works similarly.
I used AI to create the room descriptions and item descriptions. 
I used AI to get the syntax to set object comparisons.