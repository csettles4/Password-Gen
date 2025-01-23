# 11/21/2024 ---- Secure Password Generator ---- Chase Settles
#Uses Guidelines from CISA.gov for Secure Password creation. The function "generate" asks for the max length of the password you would like and then pulls from the array randomly to generate a password.

# Modules 
import random


# Variables

library = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","!","~","`","@","?","#","$","%","^","&","*","(",")","-","_","=","+",
           "[","]","{","}","|","\\",":",";","<",">",".","1","2","3","4","5","6","7","8","9","0"]


# Functions
def generate():
    # Local Variables
    max_L=int(input("What is the max amount of characters allowed in your password?"))
    num = 0
    output = ""
    character = ""

    while num != max_L:

        character = library[random.randint(0,63)]  #Chooses an item from the library list at random.

        if character.isalpha():            # Checks if the item chosen is a letter
            if random.randint(1,2) == 2:   # 50% chance to have a letter capitilized if it is a letter that is currently stored. Change these values in the if statement if you want to see more/less capital letters.
                character = character.upper()  # Capitilizes the letter

        output += character #Appends to final output string
        num += 1   #increases count 

    print(output)

generate()