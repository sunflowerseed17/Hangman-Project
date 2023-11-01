import random

# Define what the word_list is

class Hangman():
    def __init__(self, word_list, num_lives = 5):
        self.num_lives = num_lives
        self.word = random.choice(word_list) # Randomly selects a word from the list of words defined
        self.num_letters = len(set(self.word)) # Number of letters in word
        self.word_guessed = len(self.word) * ['_'] # List of dahses based on the random word's length
        self.list_of_guesses = [] #Defining a list of guesses (Begins empty as there are no guesses yet)
    '''
Method for checking guess

This method checks for whether the inputted guess is in the word which has been randomly chosen for this instance.
It replaces the dash for the index of that letter with the letter, and also decreases the number of letters left to guess by one. 
If the guess is wrong, a statement letting you know this is returned. 
    '''
    
    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:  
            print(f"Good guess! {guess} is in the word.")
            for i in range(len(self.word)):
                if self.word[i] == guess:
                    self.word_guessed[i] = guess
                    self.num_letters = self.num_letters - 1
        else:
            self.num_lives -= 1
            print(f"Sorry. {guess} is not in the word. Try again")
            print(f"You have {self.num_lives} left.")
    '''
    Method for getting an input from player

    The player inputs a letter. This method makes sure that the method is a letter and that it is singular, otherwise returning an invalid input message.
    The method then passes through the check_letter() method previously defined, and adds your guess to a list of previous guesses. 

    '''
    
    def ask_for_input(self):
        while True:
            print(self.word_guessed)
            print("These are your guesses so far: ", self.list_of_guesses)
            guess = input("Provide a single letter input ")
            if len(guess) != 1 or guess.isalpha() != True:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break

'''
Running the game

This method plays the entire game based on the Hangman class and its methods. 
it defines the numbers of lives and uses the list of words as an input
'''

def play_game(word_list):
    num_lives=5
    game = Hangman(word_list, num_lives)

    while True:
        game.ask_for_input()

        if '_' not in game.word_guessed:
            print("Congratulations. You won the game!")

        elif game.num_lives == 0:
            print("You lost!")
    
        print(f"The word was: {game.word}")

if __name__ == '__main__':
    word_list = ["strawberries", "mangoes", "blueberries", "grapefruit", "oranges"]
    play_game(word_list)




