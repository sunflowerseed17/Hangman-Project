import random

#This is the first task

word_list = "strawberries", "mangoes", "blueberries", "grapefruit", "oranges"
print(word_list)

word = random.choice(word_list)

print(word)

#This is the second task

guess = input("Please enter a single letter ")



if len(guess) == 1 and type(guess) == str:
    print("Goess guess! ")
else:
    print("Oops that is not a valid input")