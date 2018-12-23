import random
import time

def displayIntro():
    print("The year is 1945, you are an American scientist working on the invetnion of the nuclear bomb.")
    time.sleep(2)
    print("You and your team are close to figuring it all out, however...")
    time.sleep(2)
    print("Your best friend John has just told you that some components required to complete the bomb are missing.")
    time.sleep(2)
    print("What were you expecting? Ofcourse he has asked YOU to go and find them!")
    time.sleep(2)
    print("Along your journey through the secret laboratory you will have to solve puzzles in order to complete your task")
    time.sleep(2)
    print("Since you aren't permitted to leave your workstation for long, you are limited by the time")
    time.sleep(2)
    print("If the time runs out you will be fired, thus ending your career")
    time.sleep(1)


displayIntro()
def choosePath():
    answer = input("Will you accept this 'quest' from John?")
    if str(answer) == "yes":
        print("'Thanks for this, if you succeed you will be rewarded greatly', John exclaimed")
    else:
        print("John turns around and walks away")
choosePath()
