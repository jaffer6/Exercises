'''
http://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html

Created on 13 Sep 2016

@author: Aamir.Jaffer
'''
import random

def main():    
    print "Guessing Game - Guess the number between 1 and 100"
    target =random.randint(1, 100)    
    #print target
    guesses = []
    while True:
        try:                
            input = int(raw_input("> "))
            guesses.append(input)
            if input == target:
                print "Correct!"
                break
            if input > target:
                print "Lower"
            else:
                print "Higher"                            
        except ValueError:
            print "That's not a number"
        
        
        
    print "That took you {} guesses".format( len(guesses) )


if __name__ =="__main__":
    main()