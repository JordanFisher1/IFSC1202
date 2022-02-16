from random import randint
x = randint(1,20)
a = input("Hello! What is your name? ")
print("Well,",a,"I am thinking of a number between 1 and 20")
print("You have 5 guesses.")
for i in range(1,6):
    b = int(input("Take a guess: "))
    if (b < x) and (b != x):
        print("Your guess is too low")
    if (b == x):
        print("Good job",a,"!","You guessed my number in",i,"guesses")
        break
    if (b > x) and (b != x):
        print("Your guess is too high")
if (b != x):
    print("Nope. The number I was thinking of was",x)
   



