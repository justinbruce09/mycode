#!/usr/bin/env python3

"""Justin Bruce aka j-speed (ask someone why in class) if else/while loop project, How Basic are You"""

def main():
    #Plan:first create a loop that gets person into quiz
    #create questions ref. https://www.buzzfeed.com/chelseamarshall/how-basic-are-you,
    # count yes responses
    # generate 'basic' output level

    # create an initial count to tally from
    response =0

    #write out the directions for how to take the survey
    print("answer 'y' or 'n' to the following questions to find out how basic you are")

    # create a list of questions
    questions= [
            "Do you think you are basic?",
            "Do you love Northface?",
            "Has a yoga instructor 'changed your life'?",
            "Do you love scented candles?",
            "Do you Pinterest?",
            "Do you follow astrology?",
            "Do you have an astrological tattoo?",
            "Do you LOVE brunch?",
            "Do you take pictures of your food and post them on Instagram?",
            "Do you use the newest valley vernacular?",
            "Do you abbreviate a lot of words?",
            "Do you say 'I can't even' when maybe you can?",
            "Do you use 'literally' very liberally?",
            "Have you ever gotten into a heated argument about something you have no idea about drunk OR sober?",
            "Do you love Diet Coke?",
            "Do you LOVE Taylor Swift?",
            "Do you feel as though you identify with the song '22'?",
            "Have you ever gone to Coachella",
            "Do you LOVE 'The Notebook'?",
            "Do you LOVE pumpkin spice?",
            "Do you love Starbucks?",
            "Do you watch 'Keeping Up with the Kardashians'?",
            "Do you follow the latest celebrity gossip?",
            "Do you call gossip, 'goss' OR 'Tea'?",
            "Do you have a(n) accent nail?"
            ]
    # Iterate through these questions
    for question in questions: # missing :
            
           #show user the question
            print(question)
            #set user input = variable for counting
           
            answer= input(">") # chad added this line
           
           #count the yes (y) responses and ensure we account for different user I/Ps
            if "y" in answer.lower(): # chad tweaked this line
                response+=1
            else:
                response=+0
       

    # take the number of yes responses and categorize based on 'yes' response
    if response in list(range(0,6)): # the tweak I made on this line is this:
                                     # list() converts range() into a list of numbers
                                     # so the "in" can check if one of those numbers matches
                                     # if you do that to the other ranges below, you'll be good:)

        print("you aren't that basic, you just like a few basic things, unless you don't like them because everyone likes them, because thats pretty basic")
    elif response in list(range(6, 11)):
        print("yeah, face it, you like some really basic stuff, but there's a reason why basic stuff is so popular")
    elif response  in list(range (11, 16)):
        print("You are basically basic. Not overwhelmingly, but you most definitely have some basic inside that grows every time you say 'literally' when it may not have been necessary")
    elif response in list(range (16, 21)):
        print("You are one of the most basic people I have ever met, being basic is your lifestyle, but that's ok, and while you may never be the most complex person, you like what you like and there is nothing wrong with that, so just own it")
    else: 
        #response in list(range(21, 25)):
        print("you are NEXT LEVEL BASIC, but that's ok because everyone is at least a little basic there is nothing wrong with it, but for real like pH of 14 BASIC")

# allows use of block if imported
if __name__ == "__main__":

    main()
