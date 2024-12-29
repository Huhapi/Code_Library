// Daniel Hayes
// 11/17/24
// This file will create, store and create the outcome of the used items.
#ifndef USE_ITEM_H
#define USE_ITEM_H
#include "equipenum.h"
#include "player.h"
#include "monster.h"
#include "item.h"
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;
string weak_items[25] = {
    "Wooden Spoon Wand: Not much damage, but you can try poking!",          //  0   wand
    "A map: A crude piece of paper, with a mark on it - X marks the spot!", //  1   Wand
    "Fire Crackers: Just like magic missiles, shoot some zombies!!",        //  2   Wand
    "Feather Duster Wand: More for cleaning than killing, I wonder...",     //  3   wand
    "Toy Sword Wand: Fun for play, will it hurt zombies?",                  //  4   wand
    "Combat Knife: Quick and precise. Ideal for close encounters.",         //  5   W
    "Fire Axe: Sharp and sturdy. Perfect for chopping through zombies.",    //  6   W
    "Garden Shears: Sharp and strong. Great for decapitating zombies.",     //  7   W
    "Shovel: Versatile and heavy. Perfect for bashing and slicing.",        //  8   W
    "Pitchfork: Long and sharp. Ideal for impaling zombies.",               //  9   W
    "Cardboard Shield: Lightweight and flimsy, offers minimal protection.", //  10  S
    "Plastic Shield: Better than cardboard, but still easily broken.",      //  11  S
    "Wooden Shield: Basic protection, can block some attacks.",             //  12  S
    "Trash Can Lid: Improvised but sturdy, decent for blocking.",           //  13  S
    "Plywood Shield: Stronger than basic wood, offers moderate protection.",//  14  S
    "Paper Hat: Fun but flimsy, offers no real protection.",                //  15  H
    "Plastic Mask: Covers your face, will never decompose.",                //  16  H
    "Sunglasses: Stylish, but will it help?",                               //  17  H
    "Beanie: Keeps your noggin warm, but will it stop the undead?",         //  18  H
    "Baseball Hat: It won't stop much, but could help!",                    //  19  H
    "Plastic Poncho: Keeps you dry, but will it stop bites?",               //  20  A
    "Cardboard Armor: Lightweight but will it help?",                       //  21  A
    "Winter Coat: It's cold in here, this should help warm you up.",        //  22  A
    "Sweat Shirt: One of your average comfy sweatshirts, should help.",     //  23  A
    "Apron: Protects your clothes, but not your body."                      //  24  A
};

string strong_items[25] = {
    "Machete: Swift and sharp. Great for quick, clean kills.",                      //--------------25  W
    "Baseball Bat: Solid and reliable. Perfect for smashing skulls.",               //              26  W
    "Crowbar: Heavy and durable. Ideal for bashing zombie heads.",                  //              27  W    
    "Hatchet: Compact and lethal. Perfect for close combat.",                       //              28  W
    "Sledgehammer: Powerful and crushing. Great for heavy blows.",                  //              29  W
    "Paper Fan Wand: Delicate and easily torn, what does it do?",                   //              30  wand
    "Fly Swatter Wand: Good for bugs, not so much for zombies?",                    //              31  wand
    "Pool Noodle Wand: Soft and bendy, might not do much damage.",                  //              32  Wand
    "Stuffed Animal Tibbers: Cute, and potentially deadly.",                        //              33  Wand
    "Plastic Spatula Wand: Handy in the kitchen, maybe in a zombie fight?",         //              34  Wand
    "Kevlar Vest: Offers torso protection against bites and scratches.",            //              35  A
    "Leather Jacket: Tough and durable, helps prevent bites and scratches.",        //              36  A
    "Plate Carrier Armor: Plate mail, strongest armor you're going to find!",       //              37  A
    "Spiked Vest: A vest covered in spikes which damage zombies that hit you!",     //              38  A        
    "Purple Surcoat: A mysterious purple cloak which appears to be a basic cloak.", //              39  A
    "Purple Hood: A mysterious purple hood that appears to be clothe.",             //              40  H
    "Baseball Helmet: Kind of ratty, smells, but if it can stop a baseball...",     //              41  H
    "Iron Helmet: Protects your head from zombie bites and impacts.",               //              42  H
    "Welder Goggles: Shields your eyes from blood splatter and debris.",            //              43  H
    "Face Mask: Shields your face from blood splatter and airborne pathogens.",     //              44  H
    "Fiberglass Shield: Lightweight and durable, good for defense.",                //              45  S
    "Aluminum Shield: Lightweight and strong, effective against impacts.",          //              46  S
    "Steel Shield: Heavy but very durable, excellent protection.",                  //              47  S
    "Kevlar Shield: Lightweight and bullet-resistant, great for defense.",          //              48  S
    "Titanium Shield: Extremely strong and lightweight, top-tier protection."       //--------------49  S
};

class use_item {
    private:
    list<item> late_items;
    list<item> early_items;
    vector<int> idcontained;

    public:
    use_item(){}
    // Length of the distance to winning room determines number of items!
    use_item(int length){ // Initialize useitem - which will randomly select strong and weak items for this map.
        for(int makeitems=0;makeitems<length*2;makeitems++){
            if(makeitems < length){
                int id = rand()%25;
                item new_item;
                if(find(idcontained.begin(), idcontained.end(), id) == idcontained.end()){
                    if(id < 5){
                        new_item = item(id,weak_items[id],equipenum::none);
                        early_items.push_front(new_item);
                    }else if (id < 10){
                        new_item = item(id,weak_items[id],equipenum::weapon);
                        early_items.push_front(new_item);
                    }else if (id < 15){
                        new_item = item(id,weak_items[id],equipenum::shield);
                        early_items.push_front(new_item);
                    }else if (id < 20){
                        new_item = item(id,weak_items[id],equipenum::helmet);
                        early_items.push_front(new_item);
                    }else{
                        new_item = item(id,weak_items[id],equipenum::armor);
                        early_items.push_front(new_item);
                    }
                    //new_item.printString();
                }else{
                    makeitems--;
                }
            }else{
                int id = (rand()%25)+25;
                if(find(idcontained.begin(), idcontained.end(), id) == idcontained.end()){
                    item new_item;
                    if(id < 30){
                        new_item = item(id,strong_items[id-25],equipenum::weapon);
                        late_items.push_front(new_item);
                    }else if (id < 35){
                        new_item = item(id,strong_items[id-25],equipenum::none);
                        late_items.push_front(new_item);
                    }else if (id < 40){
                        new_item = item(id,strong_items[id-25],equipenum::armor);
                        late_items.push_front(new_item);
                    }else if (id < 45){
                        new_item = item(id,strong_items[id-25],equipenum::helmet);
                        late_items.push_front(new_item);
                    }else{
                        new_item = item(id,strong_items[id-25],equipenum::shield);
                        late_items.push_front(new_item);
                    }
                    //new_item.printString();
                }else{
                    makeitems--;
                }
            }
        }
    }
    // Get the size of the strong items
    int get_strong_size(){
        return late_items.size();
    }
    // get the size of the weak items.
    int get_weak_size(){
        return early_items.size();
    }
    int use_wand(int id, player* p, monster* m){
        // id 0,1,2,3,4 30,31,32,33,34
        switch(id){
            case 0: // "Wooden Spoon Wand: Not much damage, but you can try poking!"
            // Let's deal like 25 damage(depending on monster hp) to the first zombie in the list - or let them select one?
                m->hit(rand()%10+21);
                cout << "The wooden spoon grows to an unusually large size and smacks the zombie." << endl;
                if(m->gethealth() <= 0){
                    cout << "You have destroyed the undead creature!" << endl;
                    return 1;
                }
                return 0;
                break;
            case 1: // "Plastic Fork Wand: Flimsy and ineffective, but better than nothing?",
            // Extends fork across room injuring a zombie for 30 dmg(depending on max monster hp)
                m->hit(rand()%10+26);
                cout << "The forks extend across the room impaling the zombie." << endl;
                if(m->gethealth() <= 0){
                    cout << "You have destroyed the undead creature!" << endl;
                    return 1;
                }
                return 0;
                break;
            break;
            case 2: // "Fire Crackers: Just like magic missiles, shoot some zombies!!",
            // Shoots off multiple fire crackers! doing 15 damage 3 times randomly
                m->hit(rand()%5+13);
                m->hit(rand()%5+13);
                m->hit(rand()%5+13);
                cout << "Three fire crackers burst out of the wand at the zombie!" << endl;
                if(m->gethealth() <= 0){
                    cout << "You have destroyed the undead creature!" << endl;
                    return 1;
                }
                return 0;
                break;
            break;
            case 3: //  "Feather Duster Wand: More for cleaning than killing, I wonder...", ----------- Healing
            // Cleans wounds healing player for 40 damage? can be used once per room.(once used in a room cannot be used again?)
                
                cout << "Oddly warm healing water rushes out of the wand into you." << endl;
                p->heal(rand()%10+36);
                return 0;
            break;
            case 4: // "Toy Sword Wand: Fun for play, will it hurt zombies?",
            // Magically slashes a zombie for 45 damage! can be used once per room.
                cout << "The toy sword slashes the zombie!" << endl;
                if(!m->hit(rand()%10 + 41)){
                    cout << "You killed the zombie!"<< endl;
                    return 1;
                }
                return 0;
            break;
            case 30: // "Paper Fan Wand: Delicate and easily torn, what does it do?", ------------ Healing
            // Cleans wounds healing play for 80 damage? can be used once per room.(once used in a room cannot be used again?
                p->heal(rand()%10+75);
                cout << "The healing of a cool breeze on a hot day rushes into you." << endl;
                return 0;
            break;
            case 31: // "Fly Swatter Wand: Good for bugs, not so much for zombies?",
            // Extends fly swatter massively, smacking a zombie into a wall for 80 damage. can be used once per room.
                cout << "The fly swatter extends to large proportions and hits the undead!" << endl;
                if(!m->hit(rand()%10 + 41)){
                    cout << "The undead is flattened... Quite dead."<< endl;
                    return 1;
                }
                return 0;
            break;
            case 32: //  "Pool Noodle Wand: Soft and bendy, might not do much damage.",  
            // Wraps around a zombie constricting, breaking bones! for 75 damage. can be used once per room.
                cout << "Wraps around the undead constricting, breaking bones!" << endl;
                if(!m->hit(rand()%10 + 41)){
                    cout << "The undead crumples to the floor, quite dead."<< endl;
                    return 1;
                }
                return 0;
            break;
            case 33: // "Stuffed Animal Tibbers: Cute, and potentially deadly.",
            // Flame thrower tibbers burns a zombie for 100 damage. can be used once per room.
                cout << "Tibbers opens his mouth and spews fire at the undead!" << endl;
                if(!m->hit(rand()%10 + 41)){
                    cout << "The undead is replaced by a pile of ash."<< endl;
                    return 1;
                }
                return 0;
            break;
            case 34: // "Plastic Spatula Wand: Handy in the kitchen, maybe in a zombie fight?",
            // Swats a zombie over the head with magical force - 120 damage! can be used once per room.
                cout << "Swats the undead over the head with magical force!" << endl;
                if(!m->hit(rand()%10 + 41)){
                    cout << "The zombies head is flattened!"<< endl;
                    return 1;
                }
                return 0;
            break;
        }
        return 0;
    }

    // pops an item off the weak stack stored in this class, and returns it.
    item pop_weak(){
        item get_weak_item = early_items.front();
        early_items.pop_front();
        return get_weak_item;
    }
    // pops and item off the strong stack stored in this class and returns it.
    item pop_strong(){
        item get_strong_item = late_items.front();
        late_items.pop_front();
        return get_strong_item;
    }

    // Use item take in the item, room, player, and monsters
    // So that the wands can effect what is needed
    // Splits up the items by ID value
    // Calls the associated values for the types of items.
    int useitem(item* item,player* current_player, monster* monster, int n){
        int thisid = item->getId();
        if( item->getId()< 5){   // weak wands
            return use_wand(thisid,current_player, monster);
        }else if (item->getId() < 30){   // strong weapon
            current_player->equipItem(thisid, n);
            return 0;
        }else if(item->getId() < 35){    // strong wand
            return use_wand(thisid,current_player, monster);
        }else{  // equipable items
            current_player->equipItem(thisid, n);
            return 0;
        }
        return 0;
    }
};

#endif