import random

#This is the first task

word_list = "strawberries", "mangoes", "blueberries", "grapefruit", "oranges"
print(word_list)

word = random.choice(word_list)

print(word)

#This is the second task

guess = input("Please enter a single letter ")

print(type(guess))

if len(guess) == 1:
    print("Goess guess! ")