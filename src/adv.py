from room import Room
from player import Player
import textwrap
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", ),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n = room['foyer']
room['foyer'].s = room['outside']
room['foyer'].n = room['overlook']
room['foyer'].e = room['narrow']
room['overlook'].s = room['foyer']
room['narrow'].w = room['foyer']
room['narrow'].n = room['treasure']
room['treasure'].s = room['narrow']

#
# Main
#
# Make a new player object that is currently in the 'outside' room.
p = Player('Ray', room['outside'])
# Write a loop that:
#

while True:
    direction = ['n', 's', 'e', 'w', 'q']
# * Prints the current room name
    print(p.room.room_name)
    print(p.room.room_desc)
    if p.room.room_name == 'Treasure Chamber':
        break
    move = input('where do you wanted to go:')
# * Prints the current description (the textwrap module might be useful here).
    
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
    
    if move == 'n':
        if p.room.n:
            p.room = p.room.n
        else:
            print('cannot move this direction')
    elif move == 's':
        if p.room.s:
            p.room = p.room.s
        else:
            print('cannot move this direction')
    elif move == 'e':
        if p.room.e:
            p.room = p.room.e
        else:
            print('cannot move this direction')
    elif move == 'w':
        if p.room.w:
            p.room = p.room.w
        else:
            print('cannot move this direction')
    elif move == 'q':
        print('goodbye')
        break

    else:
        print('you can move e, w, s, n, or enter q to quit')
    
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
