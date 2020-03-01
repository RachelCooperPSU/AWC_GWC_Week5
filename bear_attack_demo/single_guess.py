#======================================================================
#iteration_intro.py
#This program gives a motivating example for using loops and functions
#======================================================================


#IMPORT DEPENDENCIES
#====================
#Import sys for ARGV functionality
import sys
from random import randint

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

import time


def main(args):

        # Step 1: Generate a random integer number from 1 to 5
        random_num = randint(1,5)

        # Step 2: Have the user guess the number 
        user_input = int(input("Guess my number: "))

        # Step 3: Check if the numbers match and give feedback
        print("The number was: " + str(random_num) + "\n")

        if(user_input == random_num): 
                print("You guessed correctly!")
                print("Congratulations! You get a bear meme! ")
                meme = str("bear_meme_" + str(random_num) + ".png") 

                time.sleep(1)
                output_image = mpimg.imread(meme)
                

        else:
                print("That was not correct!")
                print("Unfortunately I must send the bear-o-dactyl. ")
                
                time.sleep(1)
                output_image = mpimg.imread("bear_o_dactyl.png")

        imgplot = plt.imshow(output_image)
        plt.show()


 
#=======================================================================


#Execute main with the specified parameters
if __name__ == "__main__":
    main(sys.argv[1:])









