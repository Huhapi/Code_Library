//Daniel Hayes
//10/23/2024
// room class 
// What does the room class have?
// - items - chest? - monsters - player - list of exits
// What does a room class do?
// - remove item - open chest? - remove monsters
// - block exits - unblock exits
#ifndef ROOM_H
#define ROOM_H

#include "item.h"
#include "use_item.h"
#include "equipenum.h"
#include "monster.h"
#include <cstdlib>
#include <iostream>
#include <string>
#include <list>
#include <set>
#include <vector>
using namespace std;
// Difficulty determines the number of monsters and their strength.
// As well as the potential items in the room.

class room{
    private:
    // position on room graph
        int x;
        int y;
        bool win;
        bool visited;
        bool current_room;
        int diff;
        vector<item> items;
        use_item* ui;
        vector<monster> monsters;
        string roomstring;
        vector<string> unblocked_exits;
        vector<string> exits;
    public:
    room():x(0),y(0),roomstring("NULL"),win(false){}
    // Remove a and b from iniator - this information is stored in roomTree.
    room(int room_difficulty,int game_length,string rmstring,int a,int b, vector<string> sentexits,use_item* getitem,int rnumb){
        this->roomstring = rmstring;
        this->win = false;
        this->visited = false;
        this->current_room = false;
        this->ui = getitem;
        this->diff = room_difficulty;
        for(string exstring:sentexits){
            if(exstring != " "){
                exits.push_back(exstring);
                unblocked_exits.push_back(exstring);
            }
        }
        
        // Initialize the Monsters and Items for each room:
        if(room_difficulty > 0){
            initialize_Monsters(room_difficulty,game_length,rnumb);
        }
        initialize_Items(game_length,room_difficulty,false);
        this->x = a;
        this->y = b;
        //this->depth = c;
        //cout << "we initialize x,y,depth: "<< this->x<<", "<<this->y<<", "<<this->depth<< endl;

    }   

    // Set room as winning room.
    void setwin(){
        this->win = true;
    }
    // General room description getter.
    string getdescription(){
        return this->roomstring;
    }

    // get x  value
    int get_x(){
        return this->x;
    }
    // get y value
    int get_y(){
        return this->y;
    }


    monster* get_monster(int n){
        if(monsters.size() > 0 && n < monsters.size()){
            return &monsters.at(n); 
        }
        return new monster();
    }

    // return if win or not.
    bool getwin(){
        return this->win;
    }

    void unblock_exit(string dir){
        unblocked_exits.push_back(dir);
    }
    void visit(){
        this->visited = true;
        this->current_room = true;
    }

    // Switching current_room for mapping purposes.
    void leave(){
        current_room = false;
    }

    int hitplayer(player* p, int hit){
        int dmg = 0;
        for(monster m:monsters){
            dmg += m.getdamage();
        }
        if(hit == 1){
            dmg = dmg/2;
        }
        if(dmg>0){
            if(p->hit(dmg)){
                
                return 1;
            }
        }else{
            return 1;
        }
        return 0;
    }

    char getmap(bool seewin){
        if(win && seewin){
            return 'W';
        }else if(visited){
            if(current_room){
                return '@';
            }else if(monsters.size()==0){
                if(items.size()==0){
                    return '0';
                }else{
                    return 'I';
                }
            }else{
                return '0'+monsters.size();                
            }
        }else {
            return '0'+monsters.size();

        }
        return '*';
    }

    void add_zombie_to_room(int l, int d){
        // Create a new monster based on the length of the game and room difficulty
        monster m = monster(l,d/2," ","Monstrosity: This looks like several ghouls patchworked together into something bigger.");
        // Add monster to list of monsters in room.
        monsters.push_back(m);
    }
    void zombie_placer(int l,int d, string dir){
        // Create a new monster based on the length of the game and room difficulty
        monster m;
        if(d < l/2){
            m = monster(l,d,dir,"Ghoul: Nasty bugger, quite undead, and not getting out of the way.");
        }else{
            m = monster(l,d,dir,"Hardened Skeleton: bit tougher than a ghoul, sinewy appendages.");
        }
        
        // Add monster to lost of monsters in room.
        monsters.push_back(m);
        // Remove this exit from unblocked exits - as it is now blocked by a monster.
        int c = 0;
        for(string it: unblocked_exits){
            if(it == dir){
                unblocked_exits.erase(unblocked_exits.begin()+c);
            }
            c++;
        }
    }
    // place zombie in room function
    // This function follows the placement of rooms for the win condition.
    // Meaning it is purposely set up to have the first monsters block the route most likely going towards win.
    // Param l - length of game
    // param d = difficulty of current room
    // param rnumb - random number determining room selection.
    int place_zombie_in_room(int l, int d,int rnumb){
        monster m;
        switch (rnumb){
                // These orders will make it so that the spawned ghouls are always in the way of progressings towards victory
                case 0:
                    if(find(unblocked_exits.begin(),unblocked_exits.end(),"south")!= unblocked_exits.end()){
                        zombie_placer(l,d,"south");
                        break;
                    }else if(find(unblocked_exits.begin(),unblocked_exits.end(),"east")!= unblocked_exits.end()){
                        zombie_placer(l,d,"east");
                        break;
                    }else if(find(unblocked_exits.begin(),unblocked_exits.end(),"north")!= unblocked_exits.end()){
                        zombie_placer(l,d,"north");
                        break;
                    }else if(find(unblocked_exits.begin(),unblocked_exits.end(),"west")!= unblocked_exits.end()){
                        zombie_placer(l,d,"west");
                        break;
                    }
                    return 1;
                    break;
                case 1:
                    if(find(unblocked_exits.begin(),unblocked_exits.end(),"east")!= unblocked_exits.end()){
                        zombie_placer(l,d,"east");
                        break;
                    }else if(find(unblocked_exits.begin(),unblocked_exits.end(),"north")!= unblocked_exits.end()){
                        zombie_placer(l,d,"north");
                        break;
                    }else if(find(unblocked_exits.begin(),unblocked_exits.end(),"west")!= unblocked_exits.end()){
                        zombie_placer(l,d,"west");
                        break;
                    }else if(find(unblocked_exits.begin(),unblocked_exits.end(),"south")!= unblocked_exits.end()){
                        zombie_placer(l,d,"south");
                        break;
                    }
                    return 1;
                    break;
                case 2:
                    if(find(unblocked_exits.begin(),unblocked_exits.end(),"north")!= unblocked_exits.end()){
                        zombie_placer(l,d,"north");
                        break;
                    }else if(find(unblocked_exits.begin(),unblocked_exits.end(),"west")!= unblocked_exits.end()){
                        zombie_placer(l,d,"west");
                        break;
                    }else if(find(unblocked_exits.begin(),unblocked_exits.end(),"south")!= unblocked_exits.end()){
                        zombie_placer(l,d,"south");
                        break;
                    }else if(find(unblocked_exits.begin(),unblocked_exits.end(),"east")!= unblocked_exits.end()){
                        zombie_placer(l,d,"east");
                        break;
                    }
                    return 1;
                    break;
                case 3:
                    if(find(unblocked_exits.begin(),unblocked_exits.end(),"west")!= unblocked_exits.end()){
                        zombie_placer(l,d,"west");
                        break;
                    }else if(find(unblocked_exits.begin(),unblocked_exits.end(),"south")!= unblocked_exits.end()){
                        zombie_placer(l,d,"south");
                        break;
                    }else if(find(unblocked_exits.begin(),unblocked_exits.end(),"east")!= unblocked_exits.end()){
                        zombie_placer(l,d,"east");
                        break;
                    }else if(find(unblocked_exits.begin(),unblocked_exits.end(),"north")!= unblocked_exits.end()){
                        zombie_placer(l,d,"north");
                        break;
                    }
                    return 1;
                    break;
                }
                return 0;
    }
    // Uses the difficulty to create Monster objects
    // Use the difficulty of the room compared to the difficulty of the game
    // param d - int room difficulty
    // param l - int game length
    // param rnumb - int random number used in room generation.
    // This random number can be used to summon zombies in such a way that they tend to block the way forward.
    void initialize_Monsters(int d,int l,int rnumb){
        int random = rand()%100;
        monster m;
        if(d < l/2){
            if(random > 50){
                place_zombie_in_room(l,d,rnumb);
            }
        }else if (d < 3*l/4){
            int r = rand()%4;
            for(int count=0;count < r;count++){
                place_zombie_in_room(l,d,rnumb);
            }
        }else{
            int r = rand()%5;
            int missed = 0;
            for(int count=0;count < r;count++){
                missed += place_zombie_in_room(l,d,rnumb);
            }
            for(int counter=0;counter < missed;counter++){
                add_zombie_to_room(l,d);
            }
        }
    }

    // Uses the difficulty to create items
    void initialize_Items(int d,int rd, bool thepath){

        if(rd < d/2){
            if(ui->get_weak_size() > 0){
                // Get a number to use for percent chance 
                int random = rand()%100;
                if(thepath){
                    if(random > 30){
                        items.push_back(ui->pop_weak());
                    }
                }else{
                    if(random > 25){
                        items.push_back(ui->pop_weak());
                    }
                }
            }
            

        }else if (rd<d){
            if(ui->get_strong_size() > 0){
                int random = rand()%100;
                if(thepath){
                    if(random > 25){
                        items.push_back(ui->pop_strong());
                    }
                }else{
                    if(random > 40){
                        items.push_back(ui->pop_strong());
                    }
                }
            }
        }else{
            if(ui->get_strong_size() > 0){
                items.push_back(ui->pop_strong());
            }
        }
    }

    // Adds an item object to the vector.
    void addItem(item itm){
        this->items.push_back(itm);
    }

    // Adds a monster object to the vector.
    void addMonster(monster m){
        this->monsters.push_back(m);
    }

    // Removes a monster from the vector at position parameter n.
    void removeMonster(int m){
        unblocked_exits.push_back(monsters[m].getdirection());
        this->monsters.erase(monsters.begin()+m);
    }
    // Removes an item at position parameter n.
    void removeItem(int n){
        this->items.erase(items.begin()+n);
    }

    // gets and returns the item from the int position sent into the parameters.
    item getitem(int position){
        if(items.size() > 0 && position < items.size()){
            item hold = items.at(position);
            removeItem(position);
            return hold;   
        }
        return item();    
    }

    // Current the current available exits from the room:
    void display_exits(){
        cout << "Current exits: ";
        for(string exit:unblocked_exits){
            cout << exit << ", ";
        } 
        cout << endl;
    }
    // prints out the items in the room using the item's printString method.
    void display_inventory(){
        if(items.size()==0){
            cout << "There are no items in this room." << endl;
        }else{
            int counter = 0;
            for(item it: items){
                cout << counter << ": ";
                it.printString();
                counter++;
            }
        }
    }

    // Returns the number of moonsters in the room.
    int numb_monsters(){
        return monsters.size();
    }

    // prints out the monsters in the room using the item's printString method.
    void display_monsters(){
        if(monsters.size()==0){
            cout << "There are no monsters in this room." << endl;
        }else{
            int counter = 0;
            for(monster it: monsters){
                cout << counter << ": ";
                it.printString();
                counter++;
            }
        }
    }
    // Check if the room has an unblocked exit in input direction.
    // returns bool true if it does, false if not
    // takes in the string exit direction.
    bool hasExit(string e){
        for(string exit:unblocked_exits){
            if(e==exit){
                return true;
            }
        }
        return false;
    }
    // Checks if there are any items in the list.
    // If there are return true, else false.
    bool hasItems(){
        if(items.size()>0){
            return true;
        }
        return false;
    }

    // Checks if there are monsters in the room.
    // Returns true if there are, otherwise false.
    bool hasMonsters(){
        if(monsters.size()>0){
            return true;
        }
        return false;
    }

    // returns the number of items in the room.
    int item_list_size(){
        return items.size();
    }
    // Prints the list of items in the room.
    // With the number(+1) corresponding to it on the vector.
    void printItems(){
        if(items.size()>0){
            int counter=1;
            for(item i: items){
                cout << counter<<". ";
                i.printString();
            }
        } 
    }

    // When entering a room this will print the description,
    // Any monsters or items in the room as well.
    void printString(){
        
        cout << "You are in the " << roomstring << endl;
        
        if(monsters.size()>0){
            cout <<"There's "<<monsters.size()<<" undead in this room!"<< endl;
            for(monster m: monsters){
                m.printString();
            }
        }
        if(items.size()>0){
            cout << "Lying on the ground you see: "<<endl;
            for(item i: items){
                i.printString();
            }
        } 
        
        if(exits.size()>0){
            cout << "There are exits in the following directions: ";
            for(int exitspot=0;exitspot<exits.size();exitspot++){
                cout << exits[exitspot] << ", ";
            }
            cout << endl;
        // << ", " << exits[1] << ", " << exits[2] << ", "<< exits[3]<<endl;
        }else{
            cout << "There are no exits.... You may want to quit out."<<endl;
        }
        //return "yes\n";
    }
};

#endif