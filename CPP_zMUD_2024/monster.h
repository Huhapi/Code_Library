//Daniel Hayes
//10/23/2024
//monster class
// What does the monster class have?
// - health - attack damage - poisonous?
// What does the monster class do?
// - attack - die - Show String - compare(==) - ?
#ifndef MONSTER_H
#define MONSTER_H

#include <iostream>
using namespace std;
int identity = 0;

class monster{
    private:
    int id;
    int health;
    int damageMax;
    bool blocking_an_exit;
    string d; // Monsters will block an exit in a direction d;
    string descript;

    public:
    monster(): health(10),damageMax(2),d(" "),descript("Just your average ghoul."){}
    
    monster(int length,int difficulty,string dir,string description){

        health = difficulty*10;
        damageMax = difficulty*5;
        d = dir;
        descript = description;
        id = identity;
        identity++;
    }
    
    int gethealth(){
        return health;
    }
    void sethealth(int mh){
        health = mh;
    }

    int getdamage(){
        return damageMax;
    }

    int getid() const{
        return id;
    }

    string getdirection(){
        return d;
    }

    // Monster is hit by damage!
    bool hit(int dmg){
        this->health = health - dmg;
        if(health <=0){
            return false;
        }
        return true;
    }

    // Applying a == operator for monsters.
    bool operator==(const monster& other) const {
        // Compare relevant members for equality
        return this->id == other.getid(); // Example comparison
    }

    void printString(){
        cout << descript<<endl;
        cout << "health: " << health << " Damage: " << damageMax << endl; 
        cout << "It is blocking the "<<this->d<< " exit."<<endl;
    }
    
};


#endif