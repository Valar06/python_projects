import art
import random
a=0
def difficulty_level(l):
    global a
    if l=="easy":
        a=10
    else:
        a=5
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
level=str(input("Choose a difficulty. Type 'easy' or 'hard': ")).lower()
n=random.randint(1,100)
difficulty_level(level)
b=0
while a>0:
    print(f"You have {a} attempts remaining to guess the number ")
    input_number = int(input("Make a guess: "))
    if input_number==n:
        print(f"Congratulations You found the mystery number in {b} steps")
        break
    elif input_number>n:
        print("Too high")
    else:
        print("Too low")
    a -= 1
    b+=1