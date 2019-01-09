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
        type("'Thanks for this, we are missing three things, the Plutonium core, the fuse and lastly the blueprints for the bomb,\n we lost these things somehow... if you succeed you will be rewarded greatly', John exclaimed\n")
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
    if action == 'look':
        if "apple" in inventory:
            type("There is nothing to pick up\n")
            actionsMainLab()
        else:
            type("There is an apple on your desk.\n")
            type("\nWhat will you do now?\n")
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
        if item == 'apple':
            if "apple" in inventory:
                type("You already picked up the apple!\n")
                type("\nWhat will you do now\n")
                actionsMainLab()
            else:
                inventory.append("apple")
                type("You have taken the apple\n")
                type("\nWhat will you do now?\n")
                actionsMainLab()

    if action == 'use':
        type("Which item would you like to use?\n")
        use = input("> ")
        acceptableUses = ['apple', 'energy drink']
        while use not in acceptableUses:
            type("You can't use this item\n")
            actionsMainLab()

        if use == 'apple':
            if "apple" in inventory:
                inventory.remove("apple")
                type("You have eaten the apple, you feel stronger!\n")
                actionsMainLab()
            else:
                type("You dont have an apple!\n")
                type("\nWhat will you do now\n")
                actionsMainLab()

            if use == 'energy drink':
                if "energy drink" in inventory:
                    inventory.remove("energy drink")
                    type("You drank the entirety of the bottle, you feel funny.\n")
                    actionsMainLab()
                else:
                    type("You don't have an energy drink!\n")
                    type("\nWhat will you do now\n")
                    actionsMainLab()
##############################
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
            if "key" not in inventory:
                type("The door is locked, there must be a key somewhere...\n")
                type("\nWhat will you do now?\n")
                actionsMainCorridor()
            else:
                room4()
    if action == 'help':
        help()
        actionsMainCorridor()
###
    if action == 'look':
        if "key" in inventory:
            type("There is nothing else to pick up!\n")
            type("\nWhat will you do now?\n")
            actionsMainCorridor()
        else:
            type("There is a key on the floor.\n")
            type("\nWhat will you do now?\n")
            actionsMainCorridor()

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
            actionsMainCorridor()
        if item == 'key':
            inventory.append("key")
            type("You have taken the key\n")
            type("\nWhat will you do now?\n")
            actionsMainCorridor()
        elif item:
            type("You already picked up the key!\n")
            type("\nWhat will you do now\n")
            actionsMainCorridor()

    if action == 'use':
        type("Which item would you like to use?\n")
        use = input("> ")
        acceptableUses = ['apple', 'energy drink', 'key']
        while use not in acceptableUses:
            type("You can't use this item\n")
            actionsMainCorridor()
        if use == 'key':
            if "key" in inventory:
                type("You have openned the door to 'room4'!\n")
                actionsMainCorridor()
            else:
                type("You don't have the key!\n")
                type("\nWhat will you do now\n")
                actionsMainCorridor()
        elif use:
            type("You don't have that item! \n")
            type("\nWhat will you do now\n")
            actionsMainCorridor()

#######################
def actionsDiningRoom():

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
        acceptableDirections = ['north', 'east', 'south']
        while direction not in acceptableDirections:
            type("You cant go there.\n")
            direction = input("> ")
        if direction == 'north':
            kitchen()
        elif direction == 'east':
            secondRoom()
        elif direction == 'south':
            cleanersCloset()
    if action == 'help':
        help()
        actionsDiningRoom()
###
    if action == 'look':

        if "fuse" in inventory:
                type("There is an energy drink on the table.\n")
                type("\nWhat will you do now?\n")
                actionsDiningRoom()

        if "energy drink" in inventory:
            type("There is a fuse underneath the table.\n")
            type("\nWhat will you do now?\n")
            actionsDiningRoom()

        if "energy drink" and "fuse" in inventory:
            type("There is nothing else to pick up!\n")
            type("\nWhat will you do now?\n")
            actionsDiningRoom()
        else:
            type("There is an energy drink on the table, there is a fuse underneath the table.\n")
            type("\nWhat will you do now?\n")
            actionsDiningRoom()

###
    if action == 'inventory':
        print(inventory)
        type("\nWhat will you do now?\n")
        actionsDiningRoom()
###
    if action == 'take':
        type("What would you like to take?\n")
        item = input("> ")
        acceptableItems = ['energy drink', 'fuse']
        while item not in acceptableItems:
            type("You can't pick that up\n")
            actionsDiningRoom()
        if item == 'energy drink':
            if "energy drink" in inventory:
                type("You already picked up the energy drink!\n")
                type("\nWhat will you do now\n")
                actionsDiningRoom()
            else:
                inventory.append("energy drink")
                type("You have taken the energy drink\n")
                type("\nWhat will you do now?\n")
                actionsDiningRoom()
        if item == 'fuse':
            if "fuse" in inventory:
                type("You already picked up the fuse!\n")
                type("\nWhat will you do now?\n")
                actionsDiningRoom()
            else:
                inventory.append("fuse")
                type("You have taken the fuse\n")
                type("\nWhat will you do now?\n")
                actionsDiningRoom()

    if action == 'use':
        type("Which item would you like to use?\n")
        use = input("> ")
        acceptableUses = ['apple', 'energy drink']
        while use not in acceptableUses:
            type("You can't use this item\n")
            actionsDiningRoom()

        if use == 'energy drink':
            if "energy drink" in inventory:
                inventory.remove("energy drink")
                type("You drank the entirety of the bottle, you feel funny.\n")
                actionsDiningRoom()
            else:
                type("You don't have an energy drink!\n")
                type("\nWhat will you do now\n")
                actionsDiningRoom()

            if use == 'apple':
                if "apple" in inventory:
                    inventory.remove("apple")
                    type("You have eaten the apple, you feel stronger!\n")
                    actionsDiningRoom()
                else:
                    type("You dont have an apple!\n")
                    type("\nWhat will you do now\n")
                    actionsDiningRoom()

def actionsKitchen():
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
        acceptableDirections = ['south']
        while direction not in acceptableDirections:
            type("You cant go there.\n")
            direction = input("> ")

        if direction == 'south':
            diningRoom()

    if action == 'help':
        help()
        actionsKitchen()
###
    if action == 'look':

        if "lockpick" in inventory:
                type("There is a knife you can take.\n")
                type("\nWhat will you do now?\n")
                actionsKitchen()

        if "knife" in inventory:
            type("There is a lockpick you can take.\n")
            type("\nWhat will you do now?\n")
            actionsKitchen()

        if "lockpick" and "knife" in inventory:
            type("There is nothing else to pick up!\n")
            type("\nWhat will you do now?\n")
            actionsKitchen()
        else:
            type("There is a lockpick and a knife that you can pick up.\n")
            type("\nWhat will you do now?\n")
            actionsKitchen()

###
    if action == 'inventory':
        print(inventory)
        type("\nWhat will you do now?\n")
        actionsKitchen()
###
    if action == 'take':
        type("What would you like to take?\n")
        item = input("> ")
        acceptableItems = ['knife', 'lockpick']
        while item not in acceptableItems:
            type("You can't pick that up\n")
            actionsKitchen()
        if item == 'lockpick':
            if "lockpick" in inventory:
                type("You already picked up the lockpick!\n")
                type("\nWhat will you do now\n")
                actionsKitchen()
            else:
                inventory.append("lockpick")
                type("You have taken the lockpick.\n")
                type("\nWhat will you do now?\n")
                actionsKitchen()
        if item == 'knife':
            if "knife" in inventory:
                type("You already picked up the knife!\n")
                type("\nWhat will you do now?\n")
                actionsKitchen()
            else:
                inventory.append("knife")
                type("You have taken the knife, the head chef walks in to the kitchen, he sees you and asks,\n 'What are you doing with that knife?', how will you respond?\n")
                type("You can...\n")
                type("\n(s)tab him\n")
                type("\nmake up an (e)xcuse\n")
                type("\n(r)un away\n")
                type("\n... by entering the letter in the brackets.\n")

                RESPONSE = input("\n>")

                if RESPONSE == 's':
                    type("You stab the man in the stomach, he makes a loud and generic death sound, a person who was\n in the dining room saw what happened and has called the police, you get arrested\n your boss has fired you.\n")
                    time.sleep(2)
                    type("\nGAME OVER\n")
                    sys.exit()
                if RESPONSE == 'e':
                    type("You say, 'John has asked me to bring him this knife because he needs to cut his loaf of bread.',\n the chef looks at you suspiciously and responds with, 'Thats fine, just remember to bring it back later.',\n the chef walks off.\n")
                    type("\nWhat will you do now?\n")
                    actionsKitchen()
                if RESPONSE == 'r':
                    type("You attempt to run away, the chef stabs you in the stomach, you make a loud and generic death sound and die.\n")
                    time.sleep(2)
                    type("\nGAME OVER\n")
                    sys.exit()


    if action == 'use':
        type("Which item would you like to use?\n")
        use = input("> ")
        acceptableUses = ['apple', 'energy drink']
        while use not in acceptableUses:
            type("You can't use this item\n")
            actionsKitchen()

        if use == 'energy drink':
            if "energy drink" in inventory:
                inventory.remove("energy drink")
                type("You drank the entirety of the bottle, you feel funny.\n")
                actionsKitchen()
            else:
                type("You don't have an energy drink!\n")
                type("\nWhat will you do now\n")
                actionsKitchen()

            if use == 'apple':
                if "apple" in inventory:
                    inventory.remove("apple")
                    type("You have eaten the apple, you feel stronger!\n")
                    actionsKitchen()
                else:
                    type("You dont have an apple!\n")
                    type("\nWhat will you do now\n")
                    actionsKitchen()

def actionsCleanersCloset():
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
        acceptableDirections = ['north']
        while direction not in acceptableDirections:
            type("You cant go there.\n")
            direction = input("> ")
        if direction == 'north':
            diningRoom()

    if action == 'help':
        help()
        actionsCleanersCloset()
###
    if action == 'look':
        if 'plutonium' in inventory:
            type("The chest from which you took the plutonium is still open and empty.\n")
        else:
            type("There is a locked chest on the shelf, amongst all the cleaning products.\n")
            type("\nWhat will you do now?\n")
            actionsCleanersCloset()

###
    if action == 'inventory':
        print(inventory)
        type("\nWhat will you do now?\n")
        actionsCleanersCloset()
###
    if action == 'take':
        type("There is nothing in here that would be of any use.\n")
        type("\nWhat will you do now?\n")
        actionsCleanersCloset()

    if action == 'use':
        type("Which item would you like to use?\n")
        use = input("> ")
        acceptableUses = ['chest', 'lockpick']
        while use not in acceptableUses:
            type("You can't use this item\n")
            actionsCleanersCloset()

        if use == 'chest' or 'lockpick':
            if "lockpick" not in inventory:
                type("You can't open the chest, it's locked, maybe there is a way you can open it...\n")
                type("\nWhat will you do now?\n")
                actionsCleanersCloset()
            elif "hazmat suit" not in inventory:
                type("You open the chest using the lockpick, the inside of the chest seems to have a thick layer of lead,\n inside there is a large, solid chunk of Plutonium.\n")
                type("\nDo you want to pick it up?\n")

                answer = input("\n> ")

                if answer == 'yes':
                    type("You pick up the Plutonium with your bare hands, you die real quick.\n")
                    time.sleep(2)
                    type("\nGAME OVER\n")
                    sys.exit()
                else:
                    type("You decide to close the chest in fear of the radiation, you realise it may be too late for you however.\n you die a couple of days later in hospital.\n")
                    time.sleep(2)
                    type("\nGAME OVER\n")
                    sys.exit()
                    actionsCleanersCloset()

            elif "hazmant suit" in inventory:
                    type("You open the chest using the lockpick, the inside of the chest seems to have a thick layer of lead,\n inside there is a large, solid chunk of Plutonium.\n")
                    type("\nDo you want to pick it up?\n")

                    answer = input("\n> ")

            if "plutonium" in inventory:
                type("You have already taken the plutonium!\n")
                type("\nWhat will you do now?\n")
                actionsCleanersCloset()

            if answer == 'yes':
                inventory.append("plutonium")
                type("You pick up the Plutonium\n")
                type("\nWhat will you do now?\n")
                actionsCleanersCloset()
            else:
                type("You close the chest\n")
                type("\nWhat will you do now?\n")
                actionsCleanersCloset()

def actionsRoom4():
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
        acceptableDirections = ['north', 'east', 'south']
        while direction not in acceptableDirections:
            type("You cant go there.\n")
            direction = input("> ")
        if direction == 'north':
            kitchen()
        elif direction == 'east':
            secondRoom()
        elif direction == 'south':
            actionsRoom4()
    if action == 'help':
        help()
        actionsRoom4()
###
    if action == 'look':

        if "fuse" in inventory:
                type("There is an energy drink on the table.\n")
                type("\nWhat will you do now?\n")
                actionsRoom4()

        if "energy drink" in inventory:
            type("There is a fuse underneath the table.\n")
            type("\nWhat will you do now?\n")
            actionsRoom4()

        if "energy drink" and "fuse" in inventory:
            type("There is nothing else to pick up!\n")
            type("\nWhat will you do now?\n")
            actionsRoom4()
        else:
            type("There is an energy drink on the table, there is a fuse underneath the table.\n")
            type("\nWhat will you do now?\n")
            actionsRoom4()

###
    if action == 'inventory':
        print(inventory)
        type("\nWhat will you do now?\n")
        actionsRoom4()
###
    if action == 'take':
        type("What would you like to take?\n")
        item = input("> ")
        acceptableItems = ['energy drink', 'fuse']
        while item not in acceptableItems:
            type("You can't pick that up\n")
            actionsRoom4()
        if item == 'energy drink':
            if "energy drink" in inventory:
                type("You already picked up the energy drink!\n")
                type("\nWhat will you do now\n")
                actionsRoom4()
            else:
                inventory.append("energy drink")
                type("You have taken the energy drink\n")
                type("\nWhat will you do now?\n")
                actionsRoom4()
        if item == 'fuse':
            if "fuse" in inventory:
                type("You already picked up the fuse!\n")
                type("\nWhat will you do now?\n")
                actionsRoom4()
            else:
                inventory.append("fuse")
                type("You have taken the fuse\n")
                type("\nWhat will you do now?\n")
                actionsRoom4()

    if action == 'use':
        type("Which item would you like to use?\n")
        use = input("> ")
        acceptableUses = ['apple', 'energy drink']
        while use not in acceptableUses:
            type("You can't use this item\n")
            actionsRoom4()

        if use == 'energy drink':
            if "energy drink" in inventory:
                inventory.remove("energy drink")
                type("You drank the entirety of the bottle, you feel funny.\n")
                actionsRoom4()
            else:
                type("You don't have an energy drink!\n")
                type("\nWhat will you do now\n")
                actionsRoom4()

            if use == 'apple':
                if "apple" in inventory:
                    inventory.remove("apple")
                    type("You have eaten the apple, you feel stronger!\n")
                    actionsRoom4()
                else:
                    type("You dont have an apple!\n")
                    type("\nWhat will you do now\n")
                    actionsRoom4()

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
    print("You enter 'room 4', you have no idea what is in this room, that means you probably shouldn't know.\n")
    actionsRoom4()
def kitchen():
    type("You enter the kitchen, no one else is here, the only way to exit is the way you came in.\n")
    actionsKitchen()

def cleanersCloset():
    type("You enter a small room that belongs to the cleaner, there are hoovers and lots of cleaning products inside.\n")
    actionsCleanersCloset()

def quit():
    if input('quit'):
        sys.exit()

displayIntro()
choosePath()
