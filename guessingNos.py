import random

x=random.randint(1,9)
chances=0

print("Guess the number between 1-9!")

while chances<5:
          guess=int(input("enter your guess"))
          if guess==x:
                    print("Your guess is correct!!You won!!")
                    break
          if guess<x:
                    print("your no. is less try again")

          if guess>x:
                    print("you are thinking of too big no.")
          chances=chances+1          

                              