// Daniel Hayes
// 11/2/24
// Equip class implements item

#ifndef ITEM_H
#define ITEM_H
#include "item.h"
#include "equipenum.h"
#include <iostream>
using namespace std;

class equip : private item {
    private:
    equipenum equipment;
    int damage;
    int defense;

    public:
    equip(equipenum eq, int dam,int def){
        equipment = eq;
        damage = dam;
        defense = def;
    }



}





#endif