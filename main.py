import random


print("🎯 Welcome to the Number Guessing Game!")
n=random.randint(50,100)  
a =-1                               #It helps us start the game and go inside the loop (while a != n:).
Guesses = 1

while(a != n):
    a=int(input("Guess The  Number: "))
    if(a>n):
        print("Too high! Try a smaller number.\n")
        Guesses +=1
    elif(a<n):
        print("Too low! Try a Higer number.\n")
        Guesses +=1


print(f"Congratulation! You Choose The Correct Number {n},In {Guesses} attempt!")