#Michel Pierre-Louis
#intro message
intro = 'You’re a second-year student at the most prestigious mage’s college in the world.\n' \
        'The Queen’s college is known for its regal and opulent library.\n' \
        'As your first day of second year, you are to navigate through the library gather your materials and some items,\n' \
        'for the librarian who waits in the dungeon.\n' \
        '7 items in total\n' \
        'If you fail at your task and reach the dungeon before gathering you materials\n' \
        'your family will be gifted with an anatomically correct model and told a less concerning story of your passing.\n'



#The Map keys as directions and materials that serve as items that automaticly get picked up
rooms = {
    'Entrance': {'east': 'Library Office', 'west': 'Main Library', 'south': 'Backrooms Entrance', 'Material': False},
    'Library Office': {'west': 'Entrance', 'Material': 'Key to Backrooms'},
    'Main Library': {'east': 'Entrance', 'Material': 'Applied Fire Magic'},
    'Backrooms Entrance': {'north': 'Entrance', 'south': 'Throne', 'Material': 'Teleportation unit 1'},
    'Throne': {'north': 'Backrooms Entrance', 'west': 'Sparring Room', 'south': 'Bedroom', 'east': 'Dungeon', 'Material': 'Black Book'},
    'Sparring Room': {'west': 'Armory', 'south': 'Bedroom', 'east': 'Throne', 'Material': 'Perspectives in Summoning'},
    'Armory': {'east': 'Sparring Room', 'Material': 'Chalk'},
    'Bedroom': {'north': 'Sparring Room', 'east': 'Throne', 'Material': 'Secrets from Beyond the Veil'},
    'Dungeon': {'Material': False}
}

                 # 0: name, 1: current location, 2:health, 3:inventory[items]
p1 = [input("whats your name?"), 'Entrance', []]

def itemPickup(): #automaticly checks for items in room and add to player inventroy
    if rooms[p1[1]]['Material'] != False:
        p1[2].append(rooms[p1[1]]['Material'])
        print('You\'ve picked up:',rooms[p1[1]]['Material'])
        rooms[p1[1]]['Material']= False #changes value of item in loc to False
    else:
        return

def statusCheck():
    print(f"You are currently in the {p1[1]}")  # room check
    print(f'Inventory: {p1[2]}')  # inventory check

def p1move(move):#fuction that handles movement
    try:
        p1[1] == rooms[p1[1]][move]
    except Exception:
        return print("invalid move")
    else:
        p1[1] = rooms[p1[1]][move]#move is valid uses safeget command to update location and continue
        print()
        if p1[1] == 'Dungeon':
            if len(p1[2]) == 7:
                return print('Congratulations! You have collected all items and avoided the librarian\'s wrath!\n'
                             'Thanks for playing the game. Hope you enjoyed it. ')
            elif len(p1[2]) < 7:
                return print('The world fades to black as you see the librarians hand in your chest...GAME OVER!\n'
                             'Thanks for playing the game. Hope you enjoyed it.')

def dirFuc(loc):#returns directions
    if loc != 'Dungeon':
        materials_free_keys = [key for key in rooms[loc].keys() if key != 'Material']
        return materials_free_keys
    else:
        return

def main(): #Main function gameloop
    print(intro)
    gamewin = 0
    while gamewin != True:
        if p1[1] != 'Dungeon':#Loop ends when dungeon is reached
            statusCheck()
            move = input(f'Enter your move:{dirFuc(p1[1])}\n').lower()
            p1move(move)
            itemPickup()
        else:
            break

main()
