#!/usr/bin/env python

import random

def main():
    nama = input("Masukkan nama kamu: ")
    print ("Hai",(nama))
    """Start a music guessing game."""
    print("Guess the music: pop,balada,jazz,hiphop,rock,tradisional!")

    music = [
        "pop",
        "balada",
        "jazz",
        "hiphop",
        "rock",
        "tradisional",
        ]

    x = random.choice(music)
    
    guess = None

    while x != guess:

        guess = str(input("What music am I thinking of? "))
        
        if x == guess:
            print("You guessed {}. Congratulations you got it right!".format(guess))
            break
        else:
            print("You guessed {}. Unfortunately you got the wrong answer. Please try again!".format(guess))

main()