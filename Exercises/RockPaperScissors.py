'''
http://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html

Created on 9 Sep 2016

@author: Aamir.Jaffer
'''
import random

def main():
    possibilities = {"R": "Rock", "P": "Paper", "S":"Scissors"}
    
    print "Rock (R), Paper (P), Scissors (S)"
    
    while True:
        input = raw_input("Player: ")
        while input not in possibilities.keys():
            input = raw_input("Player: ")
        
        player = possibilities[input]
        cpu = random.choice(possibilities.values())
            
        print "Player: {}".format(player)
        print "CPU: {}".format(cpu)
        
        winner = get_winner(player, cpu)
        
        print "{} WINS! \n".format(winner)

def get_winner(player, computer):
    if player == computer:
        return "Nobody"
    elif player == "Rock":
        if computer == "Scissors":
            return "CPU"
        else:
            return "Player"
    elif player == "Paper":
        if computer =="Rock":
            return "Player"
        else:
            return "CPU"
    elif player == "Scissors":
        if computer == "Rock":
            return "CPU"
        else:
            return"Player"


if __name__=="__main__":
    main()