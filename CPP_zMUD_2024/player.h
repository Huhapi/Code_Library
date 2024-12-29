//Daniel Hayes
// 10/23/2024
// player class holds the player information and functions.
// What does a player have?
// - Health - Inventory - Equipment - Weapon    - Shield
// - Mana?
// What does a player do?
// - attack - Cast  - fire bow  - pick up items - drop items - examine inventory/equipment - equip - de-equip
// 
#ifndef PLAYER_H
#define PLAYER_H

#include "item.h"
#include "equipenum.h"
#include <iostream>
#include <list>
#include <vector>

using namespace std;

class player{
    private:
        int max_health;
        int health;
        int mana;
        item holder;
        vector<item> inventory;
        item weapon;
        item shield;
        item armor;
        item helmet;
        int defense;
        int attackDamage;
    public:
    player():health(100),mana(10){
        item a = item();
        max_health = health;
        holder = a;
        weapon = a;
        shield = a;
        armor = a;
        helmet = a;
        attackDamage = 10;
        defense = 10;
    }
    // Get and set methods!
    int getHealth(){
        return health;
    }
    void setHealth(int hp){
        health = hp;
    }
    int getMana(){
        return mana;
    }

    int getDamage(){
        return(attackDamage);
    }

    // Removes an item at position parameter n-1.
    void removeItem(int n){
        //cout << "Is this failing? " << n << endl;
        this->inventory.erase(inventory.begin()+n);
    }

    item* getitem(int position){
        if(inventory.size() > 0 && position < inventory.size()){
            return &inventory.at(position);   
        }
        return new item();    
    }

    void setMana(int m){
        mana = m;
    }

    // Player is hit by damage!
    bool hit(int dmg){
        dmg = dmg - defense;
        if(dmg > 0){
            cout << "You take: " << dmg << " damage."<< endl;
            this->health = health - dmg;
        }
        if(this->health <=0){
            return false;
        }
        return true;
    }
    // Add item to inventory!
    // takes in item, adds it to inventory.
    void addItem(item itm){
        inventory.push_back(itm);
    }

    // prints out the inventory using the item's printString method.
    void display_inventory(){
        if(inventory.size()==0){
            cout << "Your inventory is empty." << endl;
        }else{
            int counter = 0;
            for(item it: inventory){
                cout << counter << ": ";
                it.printString();
                counter++;
            }
        }
    }
    void heal(int hps){
        this->health += hps;
        if(this->health > this->max_health){
            health = max_health;
            cout << "You are fully healed." << endl;
        }
    }

    // Returns inventory size, can be used to check if inventory is empty.
    int inventory_size(){
        return inventory.size();
    }

    // Display equipment
    void display_equipment(){
        int total = 0;
        if(helmet.getId()!=0){
            total += helmet.getId();
            helmet.printString();
        }
        if(armor.getId()!=0){
            total += armor.getId();
            armor.printString();
        }
        if(weapon.getId()!=0){
            total += weapon.getId();
            weapon.printString();
        }
        if(shield.getId()!=0){
            total += shield.getId();
            shield.printString();
        }
        if(total == 0){
            cout << "You have no equipment on." << endl;
        }
    }

    // Sets the equip slot for the item!
    void equipItem(int itemid, int n){
        // Retrieve the item from inventory using the itemid
        item itm;
        for(item it: inventory){
            if(itemid == it.getId()){
                itm = it;
            }
        }
        // Use the enum to determine which equipment slot the equipment goes.
        switch(itm.getEnum()){
            case equipenum::weapon:
                if(weapon.getId()==0){
                    this->weapon = itm;
                    attackDamage += itm.getId();
                    removeItem(n);
                }else{
                    addItem(weapon);    // Add current weapon to inventory.
                    this->weapon = itm;       // Setting weapon as new weapon.
                    attackDamage -= this->weapon.getId();
                    attackDamage += itm.getId();
                    removeItem(n);    // Remove new weapon from inventory.
                }
                break;
            case equipenum::shield:
                if(shield.getId()==0){
                    this->shield = itm;
                    defense += itm.getId();
                    removeItem(n);
                }else{
                    addItem(shield);
                    defense -= shield.getId();
                    defense += itm.getId();
                    this->shield = itm;
                    removeItem(n);
                }
                break;
            case equipenum::armor:
                if(this->armor.getId()==0){
                    this->armor = itm;
                    defense += itm.getId();
                    removeItem(n);
                }else{
                    addItem(this->armor);
                    defense -= armor.getId();
                    defense += itm.getId();
                    this->armor = itm;
                    removeItem(n);
                }
                break;
            case equipenum::helmet:
                if(this->helmet.getId()==0){
                    this->helmet = itm;
                    defense += itm.getId();
                    removeItem(n);
                }else{
                    addItem(this->helmet); // Add the current armor to inventory
                    this->helmet = itm;    // Replace current armor with new armor
                    defense -= helmet.getId();
                    defense += itm.getId();
                    removeItem(n); // removes the item from inventory
                }
                break;
        }
    }
    // Remove item from equipment - back into inventory.
    void unequipItem(item itm){
        switch(itm.getEnum()){
            case equipenum::weapon:
                addItem(this->weapon);
                attackDamage -= weapon.getId();
                this->weapon = item();
                
            case equipenum::shield:
                addItem(this->shield);
                defense -= shield.getId();
                this->shield = item();

            case equipenum::armor:
                addItem(this->armor);
                defense -= armor.getId();
                this->armor = item();
                
            case equipenum::helmet:
                addItem(this->helmet);
                defense -= helmet.getId();
                this->helmet = item();
        }
    }

};

#endif