from random import random
import math

# galgje
class Galgje:
    def __init__(self):
        self.L = [
            "test",
            "password"
        ]
        self.playing = True
        self.guessed_letters = []
        self.word = self.L[math.floor(random()*len(self.L))]
        self.play()


    def play(self):
        print("Guess the word!\n")
        while self.playing:
            self.display()
            if self.playing:
                self.ask_question()


    def display(self):
        all_words = True
        for char in self.word:
            if char in self.guessed_letters:
                print(char, end="")
            else:
                all_words = False
                print("_", end="")
        print()

        if all_words:
            self.playing = False
            print("You win!")

    def ask_question(self):
        response: str = input("Enter a letter: ")
        if response.isalpha():
            self.guessed_letters.append(response)


Galgje()