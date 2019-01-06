import random
import time
import threading
import sys

def init():
    global inventory
    inventory = []
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


def choosePath():
    answer = input("\nWill you accept this 'quest' from John?")
    if str(answer) == "yes":
        type("'Thanks for this, if you succeed you will be rewarded greatly', John exclaimed\n")
        startRoom()

    else:
        type("John turns around and walks away, you journey ends here.\n")
        time.sleep(1)
        type("GAME OVER")


def startRoom():
    global inventory
    inventory = []
    type("You are in the main lab, this is the place you do all your work, the exit is just south of you, in the centre\n is the protoype of the bomb, some pieces are missing however.\n")
    type("You can check your inventory by typing 'inventory', type 'look' in order to see what items you can interact with\n in the current room.\n")
    type("You can type 'take + the name of the item' to add the item to your inventory\n")
    type("By typing 'use + the name of the item' you can use the item\n")
    type("Lastly you can move by typing 'go + direction (eg. north, east, south and west)'\n")
    type("What will you do now?\n")

    action = input ("> ")
    acceptableActions = ['go', 'use', 'look', 'inventory', 'take', 'quit']
    while action not in acceptableActions:
        print("You can't do that")
        action = input("> ")
    if action == 'quit':
        sys.exit()

    if action == 'go':
        type("Where would you like to go?\n")
        direction = input("> ")
        acceptableDirections = ['south']
        while direction not in acceptableDirections:
            type("You cant go there.\n")
            direction = input("> ")
        if direction == 'south':
            secondRoom()

    elif action == 'look':
            type("You are in the main lab, this is the place you do all your work, the exit is just south of you, in the centre\n is the protoype of the bomb, some pieces are missing however. There is an Apple on your desk.\n")
            action = input("> ")

    elif action.lower() == 'inventory':
        inventory()

    if action.lower() == 'take':
        type("What Would you like to take?\n")
        item = input("> ")
        acceptableItems = ['apple']
        while item not in acceptableItems:
            type("You can't pick that up\n")
            item = input("> ")
        if item == 'apple':
            inventory.append("apple")
            type("You have taken the apple\n")
            action = input("> ")





def secondRoom():
    print("HI")

def quit():
    if input('quit'):
        sys.exit()

displayIntro()
choosePath()
