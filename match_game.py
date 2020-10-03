#   __  __       _       _        ____                      
#  |  \/  | __ _| |_ ___| |__    / ___| __ _ _ __ ___   ___ 
#  | |\/| |/ _` | __/ __| '_ \  | |  _ / _` | '_ ` _ \ / _ \
#  | |  | | (_| | || (__| | | | | |_| | (_| | | | | | |  __/
#  |_|  |_|\__,_|\__\___|_| |_|  \____|\__,_|_| |_| |_|\___|
#
botName='josecruz_s-defbot'
from random import sample
move_number = 0

# =============================================================================
# The calculate_move() function is where you write your code. It plays
# a complete game for you. You can click the Run button to play now.
#
# 1. It will be called every time you need to make a move
# 2. This is where you control your bot and implement your strategy
# 3. You can call other functions from it
#
# Receives a parameter containing all of the information about the game
# Returns the move we want to make in the game
#
def calculate_move(gamestate):
    global move_number
    move_number += 1
    print("{}. {}".format(move_number, gamestate))
    
    # Record the number of tiles in the game
    # so we know how many tiles we need to create in the list
    num_tiles = len(gamestate["Board"])
    
    # Create a list of tile numbers
    list_of_tile_numbers = range(num_tiles)
    
    # Randomly pick 2 tile numbers from the list to upturn. (e.g. [3,5])
    move = sample(list_of_tile_numbers, 2)
    # Return the move we wish to make
    print(move)
    return {"Tiles": move}
