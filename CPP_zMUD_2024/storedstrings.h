// Daniel Hayes
// 10/24/2024
// Strings for C++ zMUD game.

#include <iostream>
#include <vector>
#include <random>
#include <algorithm>
#include <stack>
using namespace std;

string mansionrooms[20] ={
    "Grand Foyer: A spacious entryway with intricate woodwork, and a large chandelier, setting a grand tone for the mansion.",
    "Drawing Room: A formal space once used for entertaining guests, featuring shredded plush seating, ornate wallpaper, and a destroyed grand piano.",
    "Library: Shelves lined with tattered books, a broken in half ladder, and once cozy armchairs by a cold fireplace.",
    "Dining Room: A long mahogany table, crystal chandelier, and walls adorned with rich tapestries, seemingly untoched, once for hosting lavish dinners.",
    "Ballroom: A vast room with a wooden floor, high ceilings, which once held grand dances and events.",
    "Conservatory: A glass-walled room filled with long dead exotic plants, pieces of furniture, and a broken fountain, a ghost of a nice room.",
    "Study: A quiet room with a dilapidated desk, broken leather chair, and walls covered in dark wood paneling, once a peaceful place.",
    "Parlor: A cozy room with remenants of chairs, a fireplace, and a piano, once used for informal gatherings and music.",
    "Kitchen: A dirty space with a large stove, wooden cabinets, and a central island, where meals were once prepared.",
    "Butlers Pantry: A small room adjacent to the kitchen, filled with shelves for china, silverware, and linens.",
    "Master Bedroom: A luxurious room with a four-poster bed, velvet drapes, and an en-suite bathroom.",
    "Guest Bedroom: A welcoming room with a comfortable bed, antique furniture, and a view of the gardens.",
    "Nursery: A cheerful room with pastel walls, a crib, and toys, designed for the youngest members of the family.",
    "Music Room: A space dedicated to musical pursuits, with pieces of various instruments, sheet music strewn about, and remenants of a grand piano.",
    "Billiard Room: A recreational room with a busted billiard table, bar, and burned leather chairs, once used for leisure and games.",
    "Servants Quarters: Simple, functional rooms located in a separate wing, which once provided living space for the household staff.",
    "Attic: A large, dusty space filled with old trunks, forgotten treasures, and family heirlooms.",
    "Wine Cellar: A cool, dark room in the basement, lined with racks of fine wines and spirits.",
    "Garden Room: A bright, airy space, filled with remenants of comfortable seating and dead plants.",
    "Bathroom: A luxurious space with a clawfoot tub, marble sink, and ornate fixtures, offering a relaxing retreat."
    };
string bombshelterrooms[20] = {
    "Entrance Hall: A narrow, dimly lit corridor with peeling paint and rusted metal doors, leading into the shelter.",
    "Control Room: Filled with outdated equipment, broken monitors, and dusty control panels, once used to manage the shelters systems.",
    "Living Quarters: Small, cramped rooms with bunk beds, worn mattresses, and minimal furnishings, showing signs of long-term neglect.",
    "Kitchen: A basic area with old, rusted appliances, empty shelves, and a few scattered utensils, hinting at past use.",
    "Dining Area: A communal space with a long, battered table and mismatched chairs, surrounded by faded walls.",
    "Storage Room: Shelves lined with expired canned goods, dusty boxes, and forgotten supplies, covered in cobwebs.",
    "Medical Bay: A small room with outdated medical equipment, empty cabinets, and a single, rusted bed.",
    "Water Treatment Room: Filled with corroded pipes, broken filters, and stagnant water puddles, indicating a once-functional system.",
    "Generator Room: Housing an old, non-functional generator, surrounded by oil stains and discarded tools.",
    "Air Filtration Room: Containing rusted air filters, broken fans, and a thick layer of dust, showing signs of disrepair.",
    "Communications Room: Equipped with obsolete radios, tangled wires, and silent speakers, hinting at past attempts at contact."
    "Workshop: A cluttered space with broken tools, scattered parts, and unfinished projects, left in disarray.",
    "Laundry Room: Featuring rusted washing machines, empty detergent bottles, and piles of dirty, abandoned clothes.",
    "Recreation Room: A neglected area with a broken pool table, torn sofas, and faded posters on the walls.",
    "Library: Shelves filled with old, dusty books, many of which are falling apart, and a few scattered chairs.",
    "Bathroom: A grimy space with cracked tiles, rusted fixtures, and a lingering smell of mildew.",
    "Showers: A row of rusted showerheads, broken tiles, and moldy curtains, indicating long-term disuse.",
    "Armory: Empty weapon racks, scattered ammunition boxes, and a few rusted, unusable weapons.",
    "Command Center: A central room with a large, broken table, outdated maps, and non-functional communication devices.",
    "Escape Tunnel: A narrow, dark passageway with crumbling walls and debris, leading to an uncertain exit."
};
string schoolrooms[20] = {
    "Classroom: Desks with chipped paint, broken chairs, and faded posters on the walls, with a dusty chalkboard at the front.",
    "Library: Shelves filled with torn, outdated books, broken chairs, and a musty smell lingering in the air.",
    "Gymnasium: A large space with cracked floors, deflated basketballs, and broken bleachers, echoing with silence.",
    "Cafeteria: Long tables with peeling surfaces, mismatched chairs, and a kitchen area with rusted appliances.",
    "Science Lab: Broken beakers, dusty counters, and non-functional equipment, with faded safety posters on the walls.",
    "Principals Office: A cluttered desk, old filing cabinets, and a worn-out chair, with peeling paint on the walls.",
    "Music Room: Broken instruments, torn sheet music, and a piano with missing keys, surrounded by faded music posters.",
    "Art Room: Paint-splattered tables, dried-up paint tubes, and broken easels, with faded student artwork on the walls.",
    "Computer Lab: Outdated computers, broken keyboards, and tangled wires, with dusty monitors.",
    "Locker Room: Rusted lockers, broken benches, and a lingering smell of mildew, with graffiti on the walls.",
    "Auditorium: Torn seats, a dusty stage, and broken lighting fixtures, with faded curtains.",
    "Nurses Office: An old examination table, empty medicine cabinets, and a broken scale, with peeling wallpaper.",
    "Teachers Lounge: Worn-out sofas, a broken coffee machine, and cluttered tables, with faded motivational posters.",
    "Restroom: Cracked tiles, broken sinks, and graffiti-covered stalls, with a persistent smell of dampness.",
    "Hallway: Faded lockers, cracked floors, and flickering lights, with peeling paint on the walls.",
    "Storage Room: Cluttered shelves, broken furniture, and dusty boxes, with cobwebs in the corners.",
    "Playground: Completely fenced in area with rusted swings, broken slides, and overgrown grass, with faded hopscotch lines.",
    "Counselors Office: A small room with a worn-out chair, cluttered desk, and faded posters, with peeling paint.",
    "Art Gallery: Broken frames, faded student artwork, and dusty display cases, with cracked walls.",
    "Janitors Closet: Old cleaning supplies, broken mops, and a cluttered space, with a lingering smell of chemicals."
};
class storedstrings{
    private:
        stack<string> roomstrings;
    public:
        storedstrings(){
            addShelter();
            addschool();
            addMansion();
        }

        void addMansion(){
            random_device rd;
            mt19937 gen(rd());
            vector<int> numbers;
            for(int rnumbs=0;rnumbs<20;rnumbs++){
                numbers.push_back(rnumbs);
            }
            shuffle(numbers.begin(),numbers.end(),gen);

            for(int mans=0;mans<20;mans++){
                roomstrings.push(mansionrooms[numbers[mans]]);
            }
        }

        void addShelter(){
            for(int shelter=0;shelter<20;shelter++){
                roomstrings.push(bombshelterrooms[shelter]);
            }
        }

        void addschool(){
            for(int school=0;school<20;school++){
                roomstrings.push(schoolrooms[school]);
            }
        }

        string pop(){
            string retstring = roomstrings.top();
            roomstrings.pop();
            return retstring;
        }
        string top(){
            return roomstrings.top();
        }
};























