# this is a guess the number game.
import random
secNum = random.randint(1,20)
print ('I am thinking if a number between 1 and 20')

#Ask the player to guess 6 times
for gueTak in range(1,7):
    print ('Take  a Guess')
    guess= int(input())
    
    if guess < secNum:
        print ('Too low')
    elif guess > secNum:
        print('Too high')
    else:
        break #this condition is the correct guess!
if guess == secNum:
    print ('Good job! You guessed my number in '+str(gueTak) + ' guesses!')
else:
    print ('Nope. The number i was thinking was ' + str(secNum))
    

  

    

 
    
  


