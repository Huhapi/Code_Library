//Daniel Hayes
//10/23/2024
//Item class holds the building block for items in the game.
//May be virtual and used by other item object classes. 
#ifndef ITEM_H
#define ITEM_H
#include "equipenum.h"
#include <iostream>
using namespace std;

class item{
    private:
        int id;
        string description;
        equipenum equip; 

    public:
    item(): description("NULL"),id(0),equip(equipenum::none){}
    item(int idnumb,string desc,equipenum eqtype){
        description = desc;
        id = idnumb;
        equip = eqtype;

    }

    bool operator==(const item& other) const {
        // Compare relevant members for equality
        return this->id == other.getId(); // Example comparison
    }

    int getEnum(){
        return equip;
    }

    int getId() const {
        return id;
    }

    void printString(){
        cout << description << endl;
        if(equip != equipenum::none){
            switch (equip){
                case (equipenum::armor):
                    cout << "Using this will equip it to chest." << endl;
                    break;
                case (equipenum::helmet):
                    cout << "Using this will equip it as a helmet." << endl;
                    break;
                case (equipenum::weapon):
                    cout << "Using this will equip it as a weapon." << endl;
                    break;
                case (equipenum::shield):
                    cout << "Using this will equip it as a shield." << endl;
                    break;
            }
        }
    }
};

#endif