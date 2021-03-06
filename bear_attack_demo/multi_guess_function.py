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

def output_correct(correct_meme):
        print("You guessed correctly!")
        print("Congratulations! You get a bear meme! ")
        time.sleep(1)
        output_image = mpimg.imread(correct_meme)
        return output_image

def output_incorrect(incorrect_meme):
        print("That was not correct!")
        print("Unfortunately I must send the bear-o-dactyl. ")
        time.sleep(1)
        output_image = mpimg.imread(incorrect_meme)
        return output_image



def main(args):

        # Step 1: Generate a random integer number from 1 to 5
        random_num = randint(1,5)

        input_num_guesses = int(input("How many guesses would you like? "))


        correct_guess = False
        num_guess = 0

        while((not correct_guess) and (num_guess < input_num_guesses)):
                # Step 2: Have the user guess the number 
                user_guess = int(input("Guess my number: "))
                num_guess = num_guess + 1

                # Step 3: Check if the numbers match
                if(user_guess == random_num): 
                        correct_guess = True


        print("The number was: " + str(random_num) + "\n")


        # Step 3: Check if the user guessed correctly and give feedback
        if(correct_guess == True): 
                meme = "bear_meme_" + str(random_num) + ".png" 
                output_image = output_correct(meme)
                
        else: 
                meme = "bear_o_dactyl.png"
                output_image = output_incorrect(meme)

                
        imgplot = plt.imshow(output_image)
        plt.show()


 
#=======================================================================


#Execute main with the specified parameters
if __name__ == "__main__":
    main(sys.argv[1:])









