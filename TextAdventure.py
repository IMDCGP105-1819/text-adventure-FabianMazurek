import random
import time
import threading

class player:
    def __init__(self):
        self.location = 'start'
myPlayer = player()
#### MAP SETUP ####

zonename = ''
description = 'desc'
up = 'up', 'north'
down = 'down', 'south'
left = 'left', 'west'
right = 'right', 'east'

zonemap = {
    '1': {
        zonename: 'Main Laboratory',
        description = ''
        down = '2'
        left = ''
        right = ''
    },
    '2': {
        zonename == 'Hallway'
        description == 'A long and narrow corridor with two rooms on either ends.'
        up == '1'
        down ==
        left == '3'
        right = ='4'
    },
    '3': {
        zonename == 'Main Laboratory'
        description == 'You are in the main lab, this is the place you do all your work, the exit is just south of you, in the centre is the protoype of the bomb, some pieces are missing however.'
        up == '5'
        down == '6'
        left ==
        right == '2'
    },
    '4': {
        zonename == 'Main Laboratory'
        description == 'You are in the main lab, this is the place you do all your work, the exit is just south of you, in the centre is the protoype of the bomb, some pieces are missing however.'
        up == '7'
        down == '8'
        left == '2'
        right ==
    },
    '5': {
        zonename == 'Main Laboratory'
        description == 'You are in the main lab, this is the place you do all your work, the exit is just south of you, in the centre is the protoype of the bomb, some pieces are missing however.'
        up ==
        down == '3'
        left ==
        right ==
    },
    '6': {
        zonename == 'Main Laboratory'
        description == 'You are in the main lab, this is the place you do all your work, the exit is just south of you, in the centre is the protoype of the bomb, some pieces are missing however.'
        up == '3'
        down ==
        left ==
        right ==
    },
    '7': {
        zonename == 'Main Laboratory'
        description == 'You are in the main lab, this is the place you do all your work, the exit is just south of you, in the centre is the protoype of the bomb, some pieces are missing however.'
        up ==
        down == '4'
        left ==
        right ==
    },
    '8': {
        zonename == 'Main Laboratory'
        description == 'You are in the main lab, this is the place you do all your work, the exit is just south of you, in the centre is the protoype of the bomb, some pieces are missing however.'
        up == '4'
        down ==
        left ==
        right ==
    },
}

def displayIntro():
    print("The year is 1945, you are an American scientist working on the invetnion of the nuclear bomb.")
    time.sleep(1)
    print("You and your team are close to figuring it all out, however...")
    time.sleep(1)
    print("Your best friend John has just told you that some components required to complete the bomb are missing.")
    time.sleep(1)
    print("What were you expecting? Ofcourse he has asked YOU to go and find them!")
    time.sleep(1)
    print("Along your journey through the secret laboratory you will have to solve puzzles in order to complete your task")
    time.sleep(1)

def choosePath():
    answer = input("Will you accept this 'quest' from John?")
    if str(answer) == "yes":
        print("'Thanks for this, if you succeed you will be rewarded greatly', John exclaimed")
        time.sleep(1)
        startRoom()

    else:
        print("John turns around and walks away, you journey ends here.")
        time.sleep(1)
        print("GAME OVER")

inventory = []

def addToInventory(item):
    inventory.append(item)
def playerMove(myAction):
    ask = "Where would you like to move to?"
    dest input(ask)
    if dest in ['up', 'north']
        print("You can't go there.")
        dest input(ask)
    elif dest in ['down', 'south']
        destination = zonemap[myPlayer.location][down]
        movementHandler()


def startRoom():
    global inventory
    print("You are in the main lab, this is the place you do all your work, the exit is just south of you, in the centre is the protoype of the bomb, some pieces are missing however.")
    time.sleep(1)
    print("You can check your inventory by typing 'inventory', type 'look' in order to see what items you can interact with in the current room.")
    time.sleep(1)
    print("You can type 'pickup + the name of the item' to add the item to your inventory")
    time.sleep(1)
    print("By typing 'use + the name of the item' you can use the item")
    time.sleep(1)
    print("Lastly you can move by typing 'go + direction (eg. north, east, south and west)'")
    print("What will you do now?")
    action = input ("> ")
    acceptableActions = ['go', 'use', 'look', 'inventory', 'pickup', 'quit']
    while action.lower() not in acceptableActions:
        print("You can't do that")
        action = input("> ")
    if action.lower() == 'quit':
        sys.exit()
    elif action.lower() == 'go':
        playerMove(action.lower())
    elif action.lower() == 'look':
        playerLook(action.lower())
    elif action.lower() == 'inventory':
        playerInventory(action.lower())
    elif action.lower() == 'pickup':
        playerPickup(action.lower())




def secondRoom():
    print("HI")

displayIntro()
choosePath()
