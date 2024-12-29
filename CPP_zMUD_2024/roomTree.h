//Daniel Hayes
//10/23/2024
// room tree class
// This class creates a tree of rooms.

#include "room.h"
#include "equipEnum.h"
#include "storedstrings.h"
#include "use_item.h"
//#include "storedstrings.h"
#include <cstdlib>
#include <set>
#include <vector>
#include <algorithm>
using namespace std;
int roomnumb=0;

class roomTree{
    private:
    int randomize_direction;
    int initx;
    int inity;
    int difficulty;
    int branching_factor;
    int winspot[2];
    room* headroom;
    room rooms[50][50];
    list<direction> map;
    use_item *itemstock;
    int** positions;
    int addpos;
    storedstrings roomnames;

    // This represents whether the map is working towards the winning room, or on side rooms.
    bool winroute;

    public:
    roomTree():initx(15),inity(15),difficulty(10),randomize_direction(0){}
    roomTree(int startx, int starty, int dif, use_item* items){
        initx = startx;
        inity = starty;
        winroute = true;
        itemstock = items;
        // start time seed, attempt
        srand(static_cast<unsigned>(time(0)));
        
        // Initialize stack of room names.
        roomnames = storedstrings();

        randomize_direction = (rand())%4;
        difficulty = dif;
        branching_factor = difficulty/5;

        // This tracks the positions of all of the rooms in an array.
        this->positions = new int*[50];
        addpos = 0;
        for(int i=0; i<50; i++){
            this->positions[i]= new int[2] {-1,-1};
        }
        printspots();

        headroom = mapWin(0,startx,starty,6, NULL);
        
    }

    // gets the starting room
    room* get_head_room(){
        
        room* hr = &rooms[initx][inity];
        
        return hr;
    }


    // Parameters - x and y coordinates of room map
    // returns a pointer to the room at those coordinates
    // Created to help reduce complexity of code in function pickdirections
    room* getRoom(int ex,int why){
        //cout <<ex << "y:" << why << endl;
        return &rooms[ex][why];
    }
    
    bool check_direction(int dir){
        if(winroute){
            int currentposition0 = positions[addpos-1][0];
            int currentposition1 = positions[addpos-1][1];
                        
            switch(dir){
                case 0: // North x+1
                    currentposition0=currentposition0+1;
                    break;
                case 1: // East y+1
                    currentposition1=currentposition1+1;
                    break;
                case 2: // South x-1
                    currentposition0=currentposition0-1;
                    break;
                case 3: // west y-1
                    currentposition1=currentposition1-1;
                    break;
            }
            //cout << "positions: "<<currentposition0<<", "<<currentposition1<<endl;
            //printspots();
            for(int a=0;a<30;a++){
                if(positions[a][0]== -1){
                    a = 30;
                }else{
                    // Another room is taking up this position
                    // Set room exit pointer to that room instead of creating a new room!
                    if(positions[a][0] == currentposition0 && positions[a][1]== currentposition1){
                        //cout << "False - position: "<< positions[a][0]<<", "<<positions[a][1] << " vs: "<<currentposition0<<", "<<currentposition1<<endl;
                        return false;
                    }
                }
            }
            return true;
        }
        return true;
    }
    // Takes in the number of exits for a room
    // returns a string array of exit names;
    // Made into a function for easy exit using return statement.
    vector<string> pickdirections(int nexits, int d){
        
        vector<string> names = {"north","east","south","west"};
        vector<string> exitstrings = {" "," "," "," "};

        //cout << "number of exits: "<< nexits << " Last direction: " << d << endl;

        if(d>1){
            d = d-2;
        }else{
            d = d+2;
        }

        if(nexits>=3){
            for(int n=0;n<4;n++){
                if(d!=n){
                    exitstrings[n] = names[n];
                }  
            }
            //cout << "exits: "<< exitstrings[0] << exitstrings[1] <<exitstrings[2]<< exitstrings[3]<<endl;
            return exitstrings;
        }else{
            vector<int> exits = {0,0,0,0};
            exits[d] = -1;
            int counter=0;
            while(counter<nexits){
                int rdirection = rand() % 4;
                //cout<<" direction: " << rdirection << endl;
                if(exits[rdirection]!=-1){
                    if(!check_direction(rdirection)){
                        if(nexits>1){
                            exits[rdirection] = -1;
                            nexits--;
                        }else{
                            //cout << "Map failure, reboot."<<endl;
                        }
                    }
                    else{
                        exitstrings[rdirection] = names[rdirection];
                        exits[rdirection] = -1;
                        counter++;
                    }
                }
            }
        }
        //cout << "exits: "<< exitstrings[0] << exitstrings[1] <<exitstrings[2]<< exitstrings[3]<<endl;
        return exitstrings;
    }

    // Function create exits
    // Recursively calls mapWin - decreases code length
    // Parameters:
    // dif - or difficulty of previous room to room created
    // dir = exit direction taken from previous room.
    // reroom - pointer to last room created.
    void create_exits(int dif,int dir,string exit,room* retroom){

        if(winroute){
            room* sroom = mapWin(dif+1,retroom->get_x(),retroom->get_y(),dir,retroom);

        }else{
            room* sroom = mapWin(dif+3,retroom->get_x(),retroom->get_y(),dir,retroom);
        }
    }
    // Using randomize_number to make it so that the win scenario is not always south.
    // Complications arrise when trying to do this with the "north" "east" "south" "west"
    // room creation - exit names will not line up with directions when trying to move through
    // rooms in the game loop.

    room* mapWin(int way, int x, int y, int dir, room* lastroom){
        //must make opposite of dir exit to last room.
        vector<direction> direct = {direction::north,direction::east,direction::south,direction::west};
        

        // Moving this to two functions - for x/y 
        // Adjust the coordinates based off from the direction taken to enter the new room.
        switch(dir){
            case 0: //North x+1
                x++;
                break;
            case 1: // East y+1
                y++;
                break;
            case 2: // South x-1;
                x--;
                break;
            case 3: // West y-1
                y--;
                break;
            case 6:
                break;
        }
        //
        //cout << "Way: " << way << " Difficulty: " << difficulty << "Direction: "<<dir<< endl;
        // Using the array of positions to check if there is a room at these coordinates.
        for(int a=0;a<50;a++){
            //cout << "spot check:" <<positions[a][0] << endl;
            if(positions[a][0] == -1){
                a = 50;
            }else{
                // Another room is taking up this position
                // Set room exit pointer to that room instead of creating a new room!
                if(positions[a][0]== x&& positions[a][1]==y){
                    //cout << "This is a return exit! x:"<< x << " y: "<< y <<endl;
                    // return the room at these coordinates instead!
                    return(&rooms[x][y]);
                    //depth++;     
                }
            }
        }
        
        int numbExits=0;
        // determining number of exits for this new room - based off from the "way" or difficulty value for the room.
        if(way==0){
            numbExits = 4;
        }else if(way<difficulty){
            if(way > difficulty/2){
                numbExits = numbExits-2;
                if(numbExits<=0 && winroute){
                    numbExits = 1;
                }
            }else{
                if(winroute){
                    numbExits = (rand()%3)+1;
                }else{
                    numbExits = rand()%4;
                }
            }    
        }
        

        //cout << "exits: " << numbExits <<endl;

        // Track the directions taken to get to the win room.
        if(winroute){
            if(way!=0){

                map.push_back(direct[dir]);
                //printmap();
            }
        }
        
        //cout << "exits: " << numbExits << " last direction: " << dir <<endl;

        
        //
        vector<string> exits = pickdirections(numbExits,dir);
        /*
        for(int co=0; co<4;co++){
            cout << " exit"<<co<<": "<< exits[co];
        }

        int s = (rand()+2) % 20;*/
        //cout << roomnames.top() << endl;

        
        positions[addpos][0] = x;
        positions[addpos][1] = y;
        //cout << "x: " << x << " y: " << y <<" Direction: "<< dir <<endl;
        addpos++;
        
        // Adding the return exit from sending room
        switch(dir){
            case 0:
                exits[2] = "south";
                break;
            case 1:
                exits[3] ="west";
                break;
            case 2:
                exits[0] = "north";
                break;
            case 3:
                exits[1] = "east";
                break;
            case 6:
                break;
        }

        room thisroom = room(way,difficulty,roomnames.pop(),x,y,exits,itemstock,winroute);
        this->rooms[x][y] = thisroom;

        // This determines winning room - as it will stay on path until way reaches difficulty.
        if (way>=difficulty){
            
            if(winroute){
                this->rooms[x][y].setwin();
                //cout << "Notify win condition - end game."<<endl;
                winroute = false;
            }
            numbExits = 0;
        }

        // Undo the exit on exits vector back to sending room prior to recursively calling mapWin.
        switch(dir){
            case 0:

                exits[2] = " ";
                break;
            case 1:

                exits[3] =" ";
                break;
            case 2:

                exits[0] = " ";
                break;
            case 3:

                exits[1] = " ";
                break;
            case 6:
                break;
        }
        
        //this->rooms[roomnumb] = thisroom;
        roomnumb++;
        room* retroom = &this->rooms[x][y];

        
        // Use exits vector to recursively call mapWin and create new rooms.
        // By swapping the order of these calls - it changes the direction of the win condition.
        // So by randomizing number going into the switch, it should be just as likely the win condition
        // will be northeast, northwest, southeast or southwest.
        
        switch(randomize_direction){
            case 0:
                if(exits[2]=="south"){
                    create_exits(way,2,"south",retroom);
                }
                if(exits[1]=="east"){
                    create_exits(way,1,"east",retroom);
                }
                if(exits[0]=="north"){
                    create_exits(way,0,"north",retroom);
                }
                if(exits[3]=="west"){
                    create_exits(way,3,"west",retroom);
                }   
                break;
            case 1:
                
                if(exits[1]=="east"){
                    create_exits(way,1,"east",retroom);
                }
                if(exits[0]=="north"){
                    create_exits(way,0,"north",retroom);
                }
                if(exits[3]=="west"){
                    create_exits(way,3,"west",retroom);
                }
                if(exits[2]=="south"){
                    create_exits(way,2,"south",retroom);
                }   
                break;

            case 2:

                if(exits[0]=="north"){
                    create_exits(way,0,"north",retroom);
                }
                if(exits[3]=="west"){
                    create_exits(way,3,"west",retroom);
                }
                if(exits[2]=="south"){
                    create_exits(way,2,"south",retroom);
                }   
                if(exits[1]=="east"){
                    create_exits(way,1,"east",retroom);
                }
                break;

            case 3:

                if(exits[3]=="west"){
                    create_exits(way,3,"west",retroom);
                }
                if(exits[2]=="south"){
                    create_exits(way,2,"south",retroom);
                }   
                if(exits[1]=="east"){
                    create_exits(way,1,"east",retroom); 
                }
                if(exits[0]=="north"){
                    create_exits(way,0,"north",retroom);
                }
                break;
            case 6:
                break;
        }
        return retroom;
    }


    void printrooms(){
        showString(*headroom);
    }
    string showString(room cycleroom){
        
        //cout << "There are " << roomnumb << " rooms." << endl;
        
        //cout << "Desc: " << cycleroom.getString() << endl;

        for(int z=0;z<roomnumb;z++){
            //cout << "room#: " << z << endl;
            //rooms[z].getString();
        }
        
        return "yes";
    }

    void printmap(){
        vector<string> arrows = {"^",">","V","<"};
        vector<direction> directions = {direction::north,direction::east,direction::south,direction::west};
        cout << "To victory! ";
        for(direction d:map){
            if(d==direction::north){
                cout << "^";
            }
            if(d==direction::east){
                cout << ">";
            }
            if(d==direction::south){
                cout << "V";
            }
            if(d==direction::west){
                cout << "<";
            }
        }
        cout << endl;
    }

    void displaymap(bool showwin,int size){

        for(int why = 25+size;why>25-size;why--){
            for(int ex = 25-size; ex < 25+size; ex++){
                cout << rooms[why][ex].getmap(showwin) << " ";
            }
            cout << endl;
        }
    }

    void printspots(){
        for(int x=0;x<50;x++){
            if(positions[x][0] ==-1){
                x = 50;
            }else{
                for(int y=0;y<2;y++){
                    cout << positions[x][y] << " ";
                }
                cout << endl;
            }
            
        }
        cout << endl;
    }

};