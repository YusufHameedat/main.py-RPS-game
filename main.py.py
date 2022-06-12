# program to create ROCK, PAPER & SCISSORS
# choose 'R' for "ROCK", 'P' for "PAPER", 'S' for "SCISSORS"

import random

while True:
    choices = ["R","P","S"]
    CPU = random.choice(choices)
    player = None

    while player not in choices:

     player = input("choose your choice: ")
     if player not in choices:
      print("invalid input, retry")
     else:
        print ("player: ",player)
        print ("CPU: ",CPU)

    if player == CPU:
        print ("Tie")
        continue
    elif player == "R":
        if CPU == "P":
            print ("CPU is the Winner")

    elif player == "R":
        if CPU == "S":
            print ("player is the Winsner")

    elif player == "P":
        if CPU == "R":
            print ("player is the Winner")

    elif player == "P":
        if CPU == "S":
            print ("CPU is the Winner")

    elif player == "S":
        if CPU == "R":
            print ("CPU is the Winner")

    elif player == "S":
        if CPU == "P":
            print ("player is the Winner")
    break
