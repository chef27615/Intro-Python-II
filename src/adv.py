from room import Room
from player import Player
from item import Item
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

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

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
# 
# Make a new player object that is currently in the 'outside' room.

#room holding item
r = Item('A Rock')
room['outside'].items.append(r)
p = Player(room['outside'])
print(f'{p.cur_r}\n{p.cur_r.desc}\n{r.name}')
# Write a loop that:
#
while True:
    move = input('Your move:   ')
    if move == 'e':
        if p.cur_r.e_to is None:
            print('nope')
        else:
            p.cur_r = p.cur_r.e_to
            print(p.cur_r)
    elif move == 'w':
        if p.cur_r.w_to is None:
            print('nope')
        else:
            p.cur_r = p.cur_r.w_to
            print(p.cur_r)
    elif move == 's':
        if p.cur_r.s_to is None:
            print('nope')
        else:
            p.cur_r = p.cur_r.s_to
            print(p.cur_r)
    elif move == 'n':
        if p.cur_r.n_to is None:
            print('nope')
        else:
            p.cur_r = p.cur_r.n_to
            print(p.cur_r)
    elif move == 'q':
        break
    elif move == 'i':
        p.inv()
    elif move == 'l':
        p.look()
    else:
        print('enter your move in this format: e,w,n,s,q')

        

# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
