// Daniel Hayes
// 10/23/2024
// Initialize and start game!
#include "game.h"
#include "room.h"
#include "player.h"

int main(){
    game agame = game(15);
    agame.initializemap();
    agame.gameLoop();
}