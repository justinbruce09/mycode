#!/usr/bin/env python3
"""Alta3 Research | Justin
   Conditionals - Monty Python Life of Brian guessing game using a while True loop."""

round = 0           # integer round set to 0
while True:        # sets up an infinite loop condition
    round = round + 1     # increases the round counter per guess
    print('Finish the movie title, "Monty Python\'s The Life of ______"')
    answer = input("Your guess--> ")    # string ans collected from user
    if answer == 'Brian': # checks for correct answer
        print('Correct!')
        break             # escapes the while loop
    elif round == 3:    # ensures round hasnt  reached 3
        print('Sorry, the answer was Brian.')
        break             #  escapes the while loop
    else:                 # if answer was wrong, and round is not yet equal to 3
        print('Sorry. Try again!') # default statement 

