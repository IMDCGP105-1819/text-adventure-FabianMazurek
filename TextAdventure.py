import random
import time
import threading
import sys


class player:
    def __init__(self):
        self.location = 'start'
myPlayer = player()

###MAP###
def type(word):
    for letter in word:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.01)


def displayIntro():
    type("The year is 1945, you are an American scientist working on the invetnion of the nuclear bomb.\n")

    type("You and your team are close to figuring it all out, however...\n")

    type("Your best friend John has just told you that some components required to complete the bomb are missing.\n")

    type("What were you expecting? Ofcourse he has asked YOU to go and find them!\n")

    type("Along your journey through the secret laboratory you will have to solve puzzles in order to complete your task.\n")

global inventory
inventory = []

def choosePath():
    answer = input("\nWill you accept this 'quest' from John?\n")
    if str(answer) == "yes":
        type("'Thanks for this, if you succeed you will be rewarded greatly', John exclaimed\n")
        startRoom()

    else:
        type("John turns around and walks away, you journey ends here.\n")
        time.sleep(1)
        type("GAME OVER")

def help():
    type("You can check your inventory by typing 'inventory', type 'look' in order to see what items you can interact with\n in the current room.\n")
    type("\nYou can type 'take' to access the take item function\n")
    type("\nBy typing 'use' you can use the item\n")
    type("\nLastly you can move by typing 'go' followed by north, east, south and west\n")
    type("\nWhat will you do now?\n")
#######################################################################################################################
def actionsMainLab():
    global inventory
    action = input ("> ")
    acceptableActions = ['go', 'use', 'look', 'inventory', 'take', 'quit', 'help']
    while action not in acceptableActions:
        print("You can't do that")
        type("\nWhat will you do now?\n")
        action = input("> ")
    if action == 'quit':
        sys.exit()
###
    if action == 'go':
        type("Where would you like to go?\n")
        direction = input("> ")
        acceptableDirections = ['south']
        while direction not in acceptableDirections:
            type("You cant go there.\n")
            direction = input("> ")
        if direction == 'south':
            secondRoom()

    if action == 'help':
        help()
        actionsMainLab()
###
    if action == 'look' and not inventory[0]:
            type("There is an apple on your desk.\n")
            type("\nWhat will you do now?\n")
            actionsMainLab()
    if action == 'look':
            type("There is nothing to pick up\n")
            actionsMainLab()

###
    if action == 'inventory':
        print(inventory)
        type("\nWhat will you do now?\n")
        actionsMainLab()
###
    if action == 'take':
        type("What would you like to take?\n")
        item = input("> ")
        acceptableItems = ['apple']
        while item not in acceptableItems:
            type("You can't pick that up\n")
            actionsMainLab()
        if item == 'apple' and not inventory:
            inventory.append("apple")
            type("You have taken the apple\n")
            type("\nWhat will you do now?\n")
            actionsMainLab()
        elif item:
            type("You already picked up the apple!\n")
            type("\nWhat will you do now\n")
            actionsMainLab()

    if action == 'use':
        type("Which item would you like to use?\n")
        use = input("> ")
        acceptableUses = ['apple', 'energy drink']
        while use not in acceptableUses:
            type("You can't use this item\n")
            actionsMainLab()

        if use == 'apple' and inventory:
            inventory.remove("apple")
            type("You have eaten the apple, you feel stronger!\n")
            actionsMainLab()
        elif use:
            type("You don't have an apple! \n")
            type("\nWhat would you like to do?\n")
            actionsMainLab()

#####
def actionsMainCorridor():

    action = input ("> ")
    acceptableActions = ['go', 'use', 'look', 'inventory', 'take', 'quit', 'help']
    while action not in acceptableActions:
        print("You can't do that")
        type("\nWhat will you do now?\n")
        action = input("> ")
###
    if action == 'quit':
        sys.exit()
###
    if action == 'go':
        type("Where would you like to go?\n")
        direction = input("> ")
        acceptableDirections = ['north', 'east', 'west']
        while direction not in acceptableDirections:
            type("You cant go there.\n")
            direction = input("> ")
        if direction == 'north':
            startRoom()
        elif direction == 'west':
            diningRoom()
        elif direction == 'east':
            room4()
    if action == 'help':
        help()
        actionsMainCorridor()
###
    if action == 'look' and not inventory['key']:
            type("There is a key on the floor.\n")
            type("\nWhat will you do now?\n")
            actionsMainCorridor()
    if action == 'look':
            type("There is nothing to pick up\n")
            actionsMainLab()
###
    if action == 'inventory':
        print(inventory)
        type("\nWhat will you do now?\n")
        actionsMainCorridor()
###
    if action == 'take':
        type("What would you like to take?\n")
        item = input("> ")
        acceptableItems = ['key']
        while item not in acceptableItems:
            type("You can't pick that up\n")
            actionsMainLab()
        if item == 'key' and not inventory:
            inventory.append("key")
            type("You have taken the key\n")
            type("\nWhat will you do now?\n")
            actionsMainLab()
        elif item:
            type("You already picked up the key!\n")
            type("\nWhat will you do now\n")
            actionsMainCorridor()
    if use == 'key' and inventory:
        type("You have opened the door to 'room 4'\n")
        actionsMainLab()
    elif use:
        type("You don't have a key! \n")
        type("\nWhat would you like to do?\n")
        actionsMainLab()


def actionsDiningRoom():
    action = input ("> ")
    acceptableActions = ['go', 'use', 'look', 'inventory', 'take', 'quit', 'help']
    while action not in acceptableActions:
        print("You can't do that")
        action = input("> ")
###
    if action == 'quit':
        sys.exit()
###
    if action == 'go':
        type("Where would you like to go?\n")
        direction = input("> ")
        acceptableDirections = ['north', 'east', 'south']
        while direction not in acceptableDirections:
            type("You cant go there.\n")
            direction = input("> ")
        if direction == 'north':
            startRoom()
        elif direction == 'east':
            secondRoom()
        elif direction == 'south':
            room4()
    if action == 'help':
        help()
        actionsDiningRoom()
###
    if action == 'look':
            type("There is a fork on the table, there is also an energy drink.\n")
            actionsDiningRoom()
###
    if action == 'inventory':
        print(inventory)
        actionsDiningRoom()
###
    if action.lower() == 'take':
        type("What Would you like to take?\n")
        item = input("> ")
        acceptableItems = ['fork', 'energy drink']
        while item not in acceptableItems:
            type("You can't pick that up\n")
            actionsDiningRoom()
        if item == 'fork':
            inventory.append("fork")
            type("You have taken the fork\n")
            actionsDiningRoom()
        if item == 'energy drink':
            inventory.append("energy drink")
            type("You have taken the energy drink\n")
            actionsDiningRoom()


def startRoom():

    type("You are in the main lab, this is the place you do all your work, the exit is just south of you, in the centre\n is the protoype of the bomb, some pieces are missing however. Type help to display controls.\n")
    actionsMainLab()



def secondRoom():

    type("You enter a long and narrow hallway with two doors on either ends, which way will you go?\n")
    actionsMainCorridor()

def diningRoom():
    type("You entered a large dining room with lots of long tables next to one another, there is a door to the north that leads\n to the kitchen, and a door to the south that is the cleaners' closet\n")
    actionsDiningRoom()

def room4():
    print("BYE")
def quit():
    if input('quit'):
        sys.exit()

displayIntro()
choosePath()
