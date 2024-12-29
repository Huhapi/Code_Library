//Daniel Hayes
//10/23/2024
//Holds the consol data for the game- player and room objects
// What does the game object have?
// - Player - Room
// what does the game object do?
// - Moves player - initialize game objects
// - run game loop - open chest? 
// - Possible actions in a room - attack - exit - open chest? - pick up item - examine inventory - use item - equip item
// - examine equipment
#include "room.h"
#include "player.h"
#include "roomTree.h"
#include "use_item.h"
#include <iostream>
#include <list>
#include <string>
#include <algorithm>
#include <cctype>
using namespace std;

class game{
    private:
    roomTree map;
    room *currentRoom;
    player playerOne;
    use_item item_stock;
    int difficulty;
    //int *map;
    int xcoord;
    int ycoord;
    bool show_win;

    public:
    game(int length):currentRoom(new room()),playerOne(player()),difficulty(length){}
    int initializemap(){
        //cout << "started rt."<<endl;
        // Create map of room!
        // All of these 15s should be a variable!
        this->show_win = false;
        xcoord = 25;
        ycoord = 25;

        item_stock = use_item(difficulty);

        map = roomTree(xcoord,ycoord,difficulty,&item_stock);
        // Set current room as the root of the tree!
        currentRoom = map.get_head_room();
        cout << "room tree initialization success!!" << endl;
        //rt.printrooms();
        //rt.printspots();

        return 0;
    }
    
    // Takes a string and returns true if it is numeric or false if not.
    bool isNumeric(const string& str) {
        return !str.empty() && all_of(str.begin(), str.end(), ::isdigit);
    }

    int attackMonster(monster* m, int n){

        if(!m->hit(playerOne.getDamage())){
            currentRoom->removeMonster(n);
            cout << "You killed that monster!" << endl;
        }else{
            cout << "You managed to damage it." << endl;
        }

        return 0;
    }
    int attackPlayer(int hit){
        
        if(currentRoom->hitplayer(&playerOne, hit) ==1){
            return 1;
        }   
        return 0;
    }   

    room* move(string d){
        if(d=="east"){
            ycoord++;
            return map.getRoom(xcoord,ycoord);
        } else if(d=="north"){
            xcoord++;
            return map.getRoom(xcoord,ycoord);
        } else if(d == "south"){
            xcoord--;
            return map.getRoom(xcoord,ycoord);
        }else if(d == "west"){
            ycoord--;
            return map.getRoom(xcoord,ycoord);
        }
        cout << "we aren't going anywhere! Haha"<<endl;
        return currentRoom;
    }

    void gameLoop(){
        string input;
        bool run;
        cout << "Welcome player, would you like to try your hand at the zombie maze?(yes or no)"<<endl;
        cin >> input;
        if(input == "yes"){
            run = true;
            cout << "You awake in a foreign place. If at any point you would like to quit respond to the prompt with 'q'." <<endl;
        }else{
            run = false;
        }
        
        // Initializing loop variables.
        //bool hasitems=false;
        //bool hasmonsters = false;
        bool movedRooms = true;
        while(run){
            if(movedRooms){
                if(currentRoom->getwin()){
                    cout << "Congratulations! You have made it through the maze!" << endl;
                    break;
                }else{
                    currentRoom->printString();
                    currentRoom->visit();
                    movedRooms = false;
                }
                
            }
            bool cresponse = false;
            string response;
            
            while(!cresponse){
                // Four different requests representing four different possibilities in a room. 
                // Both items and monsters, just monsters, just items, or an empty room with just exits.
                if(currentRoom->hasItems()&&currentRoom->hasMonsters()){
                    cout << "Are you going to try and loot the 'item', 'fight', take an available 'exit' look at the 'map' or view your 'inventory'/'equipment'?" << endl; 
                // Only Monsters
                }else if(currentRoom->hasMonsters()){
                    cout << "Are you going to 'fight', take an 'exit',or view your 'inventory'/'equipment'?" << endl;
                // Only Items
                }else if(currentRoom->hasItems()){
                    cout << "Loot the 'item', look at the 'map', take an 'exit', or view your 'inventory'/'equipment'?" << endl;
                }else{
                    cout << "Would you like to look at the 'map', take an 'exit', or view your 'inventory'/'equipment'?" << endl;
                }
                cout << "Health: "<< playerOne.getHealth() << endl;

                // Takes in their response.
                cin >> response;
                // Reactions dealing with each possible response
                // If the response is not on the list of responses, the while loop makes the request again above.
                if(response=="exit"){

                    cout << "Which direction would you like to go? " << endl;
                    currentRoom->display_exits();
                    cin >> response;
                    if(response == "q"){
                        cresponse = true;
                        run = false;
                    } else if(currentRoom->hasExit(response)){
                        // Need to account for monster blocked exits here
                        currentRoom->leave();
                        currentRoom = move(response);
                        cout << "You travel " << response << "!"<<endl;
                        movedRooms = true;
                        cresponse = true;
                    }else{
                        currentRoom->printString();
                    }
                }else if(response == "equipment"){
                    playerOne.display_equipment();
                
                }else if(response == "map"){

                    map.displaymap(show_win, difficulty);
                        
                }else if(response == "inventory"){

                    playerOne.display_inventory();
                    if(playerOne.inventory_size() > 0){
                        cout << "If you would like to use one of your items, select it's number(for example 0,1,2 or 3): " << endl;
                        cin >> response;
                        if(isNumeric(response)){
                            if(-1 < stoi(response) && stoi(response) < playerOne.inventory_size()){
                                item* useit = playerOne.getitem(stoi(response));
                                //cout << "item# in game loop: " << useit->getId() << endl;
                                // if it is a wand, and doesn't have id #
                                if(useit->getEnum()== equipenum::none){
                                    // Could potentially add more items to this list later.
                                    if(useit->getId() != 3 && useit->getId() != 30 && useit->getId() != 1){
                                        if(currentRoom->hasMonsters()){
                                            if(currentRoom->numb_monsters() == 1){
                                                if(item_stock.useitem(useit,&playerOne,currentRoom->get_monster(0),stoi(response))==1){
                                                    currentRoom->removeMonster(0);
                                                    cout << "You have slain the monster!" << endl;
                                                }else{
                                                    if(attackPlayer(1) == 0){
                                                        cout << "You have died. Good luck next time adventurer!" << endl;
                                                        run = false;
                                                        cresponse = true;
                                                    }
                                                }
                                            }else{
                                                cout << "input the monster's number(for example 0,1,2 or 3): " << endl;
                                                currentRoom->display_monsters();
                                                cin >> response;
                                                if(isNumeric(response)){
                                                    if(-1 < stoi(response) && stoi(response) < currentRoom->numb_monsters()){
                                                        if(item_stock.useitem(useit,&playerOne,currentRoom->get_monster(stoi(response)),stoi(response))==1){
                                                            currentRoom->removeMonster(stoi(response));
                                                            cout << "The monster targetted falls over dead." << endl;
                                                            if(attackPlayer(1) == 0){
                                                                cout << "You have died. Good luck next time adventurer!" << endl;
                                                                run = false;
                                                                cresponse = true;
                                                            }
                                                        }else{
                                                            if(attackPlayer(1) == 0){
                                                                cout << "You have died. Good luck next time adventurer!" << endl;
                                                                run = false;
                                                                cresponse = true;
                                                            }
                                                        }
                                                    }else{
                                                        cout << "That selection was outside of the options." << endl;
                                                    }
                                                }else{
                                                    cout << "That selection was outside of the options." << endl;
                                                }
                                                
                                            }

                                        }
                                    }else{
                                        if(useit->getId() == 1){
                                            show_win = true;
                                            cout << "Your map has been updated." << endl;
                                            playerOne.removeItem(stoi(response));
                                        }
                                        item_stock.useitem(useit,&playerOne,NULL,stoi(response));
                                    }
                                    // If it is not a wand, the just use it - as monster type does not matter.
                                    // Would need to implement usable equipment here as well! - by checking item id.
                                }else{
                                    item_stock.useitem(useit,&playerOne, NULL,stoi(response));
                                }
                            }else{
                                cout << "That number is outside the list." << endl;
                            }
                        }
                        
                    }

                }else if(response == "q"){

                    cresponse = true;
                    run = false;

                }else if(response == "item"){

                    if(currentRoom->hasItems()){
                        if(currentRoom->hasMonsters()){
                            cout << "Are you sure you would like to try to grab the item?('yes' if yes, anything else if no.)" << endl;
                            cin >> response;
                            if(response == "yes"){
                                // Selected to pick up item with monsters in room.
                                // Take damage from monsters.
                                if(attackPlayer(1) == 0){
                                    cout << "You have died. Good luck next time adventurer!" << endl;
                                    run = false;
                                    cresponse = true;
                                }
                                // Pick up first item you reach.
                                item useit = currentRoom->getitem(0);
                                playerOne.addItem(useit);

                            }
                        }else{
                            // Two different things here, either there's 1 item and you just grab it or there's more and you select a number.
                            if(currentRoom->item_list_size() > 1){
                                currentRoom->display_inventory();
                                cout << "If you would like to pick up one of these items, select it's number(for example 0,1,2 or 3): " << endl;
                                cin >> response;
                                cout << "Response: " << stoi(response) << endl;
                                if(-1 < stoi(response) && stoi(response) < playerOne.inventory_size()){
                                    item useit = currentRoom->getitem(stoi(response));
                                    playerOne.addItem(useit);
                                }else{
                                    cout << "That number is outside the list." << endl;
                                }
                            }else{
                                    item useit = currentRoom->getitem(0);
                                    playerOne.addItem(useit);
                            }
                        }
                    }else{
                        cout << "There are no items in the room." << endl;
                    }
                    
                }else if(response == "fight"){
                    cout << "Select a monster to strike!(for example 0,1,2 or 3):" << endl;
                    currentRoom->display_monsters();
                    cin >> response;
                    if(isNumeric(response)){
                        if(-1 < stoi(response) && stoi(response) < currentRoom->numb_monsters()){
                            attackMonster(currentRoom->get_monster(stoi(response)),stoi(response));
                            if(attackPlayer(0) == 0){
                                cout << "You have died. Good luck next time adventurer!" << endl;
                                run = false;
                                cresponse = true;
                            }
                        }   
                    }
                    
                }
                    
            }
        
            
        }

        cout << "Safe travels adventurer!"<<endl;
    }
};
