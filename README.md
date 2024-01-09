# Hangman
Table of Contents
- [What is the project?](##what-is-the-project?)
- [Steps Followed](##steps-followed)
- [Skills Demonstrated](##skills-demonstrated)

![ ](https://t4.ftcdn.net/jpg/02/48/96/11/360_F_248961156_XeSISXFo6bcFUw830wpE2zPLxWGCl1u9.jpg)

## What is the project?
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.
This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 
I have first gone through the steps of setting up separate blocks of code which are integral to the game through the milestone .py files; then the full culmination of the .py code can be found in milestone_5.py

## Steps followed
The steps follow through the hangman_Template.py file which can be found in the hangman folder. This details the structure of the code. 
1) milestone_2.py has two code blocks within it:
   - Code which inputs a list of words and outputs a random word from this list
   - Code which instructs user to input a single letter; if the letter is singular and if is a letter (not a number), then the output is "Good guess!" otherwise "Oops that is not a valid input".
2) milestone_3.py defines two functions:
   - check_guess() is a function which checks whether or not a letter inputted by the user is within a pre-defined word, outputting a message to let the user know this.
   - ask_for_input() is a function which asks the user to input a single letter, checking whether it is a character and whether it is singular.
3) milestone_4.py defines the Hangman() class:
   - This includes the init() function of establishing the word_list, randomisation of the chosen word, the number of letters in the chosen word and the number of lives. The number of letters in the chosen word are made into a list of '_' which will be filled in as correct guesses start coming in. 
   - The check_guess() function checks that the letter guess by the user is within the word. If it is not, then the number of lives is decreased by one. It also tracks the correct guesses within a set of spaces preset within the init() function.
   - The ask_for_input() function establishes a way in which the user can input a single letter as a guess. It also tracks the letters already inputted as guesses.
4) milestone_5.py showcases the Hangman() class as well as a function which incorporates the class as part of the game:
   - The same as milestone_4.py, with some additions to the Hangman() class such as counting how many letters are still left to guess, and printing user-friendly messages such as letting them know how many lives they have left or letting them know whether they have tried a letter already.
   - The play_game() function uses a word list as an input to choose a word from this list at random to start the game. It defines the winning and losing statements for the game, such that you win if there are no more '_' in the list length made based on the length of the word, and lose if there are no more lives left.

## Skills demonstrated 

- Core Python
- Variable changing
- Ability to create functions and classes within Python
- Ability to create user-friendly coding projects
- Python debugging 
