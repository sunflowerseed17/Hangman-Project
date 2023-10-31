import random


word_list = "strawberries", "mangoes", "blueberries", "grapefruit", "oranges"

class Hangman():
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = [len(self.word) * '_']
        self.num_letters = len(self.word)
        self.list_of_guesses = []

    
    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:  
            print(f"Good guess! {guess} is in the word.")
            for letter in self.word:
                if letter == guess:
                    self.word_guessed.replace([self.word.index(letter)], guess)
            self.num_letters = self.num_letters - 1
        else:
            self.num_lives = self.num_lives - 1
            print(f"Sorry. {guess} is not in the word. Try again")
            print(f"You have {self.num_lives} left.")
    
    def ask_for_input(self):
        while True:
            guess = input("Provide a single letter input ")
            if len(guess) != 1 or guess.isalpha() != True:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)


Hangman(word_list)


