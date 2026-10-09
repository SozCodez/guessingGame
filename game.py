import random
start = True
#the random module is used to generate a random number
#here we are importing it for later use

#extra cred: limited tries
numTries = 5

randomNum1 = random.randrange(1, 11)
"""
this will set our first random number to anything
between 1 and 10. we set it to 11 because with
this function it goes up to, but does not include 11
"""
#another way to do this is:
#random.randint(1, 10)
#which does include the final parameter

prevGuesses = []
#program intro and list creation
print("---Welcome to:---")
print("--GUESSING GAME--")
print("-RULES: You get 5 tries to guess the number. Good luck!-")
print()
print("Please enter a number between 1 and 10:")
guess1 = int(input(""))


#loop keeps it open as program runs, basically
#as long as there are more lines it can run, it will
while start:
     #if numTries > 0:
     #    tryAvailable = True
     #else:
     #    tryAvailable = False

     #while not tryAvailable:
     #    print()
     #    print("Out of tries :(")
     #    start = False #to be able to exit main game loop
     #   break
     #if not start:
     #   break 
    """ 
    when no more tries are avalable, we set start to false, but this doesnt
    exit the main game loop meaning it will continue to run guess queries
    to fix this we add a check early in the game loop that stops 
    before any more queries are made
    """
    
    if guess1 != "":
        if 10 >= guess1 >= 1:
            if guess1 in prevGuesses:
                print()
                print("You already tried", guess1)
                print("Try a different number")
                print()
                print("Previous Guesses:", prevGuesses)
                guess1 = int(input(":"))
            else: #this is our code block for a valid input
                numTries += -1
                
                if guess1 > randomNum1 and guess1 != randomNum1 and numTries != 0:
                    prevGuesses.append(guess1) 
                    print()
                    print("You have", numTries, "tries left, Lower")
                    print()
                    print("Previous Guesses:", prevGuesses)
                    guess1 = int(input(":"))
                elif guess1 < randomNum1 and guess1 != randomNum1 and numTries != 0:
                    prevGuesses.append(guess1) 
                    print()
                    print("You have", numTries, "tries left, Higher")
                    print()
                    print("Previous Guesses:", prevGuesses)
                    guess1 = int(input(":"))
                elif guess1 != randomNum1 and numTries == 0:
                    print()
                    print("Out of tries :(")
                    print("The number was", randomNum1)
                    break
                else:
                    prevGuesses.append(guess1) 
                    print()
                    print("You guessed it!")
                    break      
        else:
            print()
            print("Invalid input")
            print("Please enter a number between 1 and 10:")
            guess1 = int(input(""))

    #else:
    #    print()
    #    print("Cannot leave blank")
    #    print("Please enter a number between 1 and 10:")
    #    guess1 = int(input(""))      
    #just dont leave it blank..

