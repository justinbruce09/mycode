#!/usr/bin/python3

# Replace RPG starter project with this code when new instructions are live

def showInstructions():
  #print a main menu and the commands
  print('''
RPG Game
========
Commands:
  go [direction]
  get [item]
''')

def showStatus():
  #print the player's current status
  print('---------------------------')
  print('You are in the ' + currentRoom)
  #prints a verbal description of what you see based on location
  print(rooms[currentRoom]['description'])
  #print the current inventory
  print('Inventory : ' + str(inventory))
  #print an item if there is one
  if "item" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item'])
  print("---------------------------")
# asks a riddle and places user in a loop until the answer correctly
def riddleFunction(riddleItem):
  print('---------------------------')
  print('if you want the item you must first answer the riddle.')
  print(riddleDictionary[riddleItem][0])
  answer=input(">")
  if answer.lower().strip() == riddleDictionary[riddleItem][1]:
      print("Correct!")
  else:
    riddleFunction(riddleItem)
        
#an inventory, which is initially empty
inventory = []

#a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms
rooms = {

            'Hall' : {
                  'south' : 'Kitchen',
                  'east'  : 'Dining Room',
                  'item'  : 'key',
                  'description': 'a long dimly lit hallway with doors that lead [up] the Attic, [south] to the Kitchen, [east] to the Dining Room'
                },

            'Kitchen' : {
                  'north' : 'Hall',
                  'item'  : 'monster',
                  'description': 'a large open room full of dilapidated cabinets, and a strong, stench resembling that of a rotten milk. From Kitchen you can go [down] to get to the Basement or [north] to return to the Hall',
                },
            'Dining Room' : {
                  'west' : 'Hall',
                  'south': 'Garden',
                  'item' : 'potion',
                  'north' : 'Pantry',
                  'description': 'A once beautiful room with a grand table and ornate woodwork, covered in fine silver, now covered in cobwebs. You may go [west] to the Hall, [south] to the Garden, and [north] to the Pantry'
               },
            'Garden' : {
                  'north' : 'Dining Room',
                  'description': 'An overgrown garden with an odd glow coming from somewhere just out of sight. Head [north] to go to the Dining Room.'

               },
            'Pantry' : {
                  'south' : 'Dining Room',
                  'item' : 'cookie',
                  'description':"A large butler's pantry that appears to be untouched still having some food inside. From the Pantry you can head [south] to the Dining Room."
			         },
            'Attic' : {
                  'description': 'a hot dark space only pieces of it can be seen by sunlight peeking through holes from the attic turbines. Who knows what could exist up here.'
			         },
            'Basement' : {
                  'description': 'a large open space that was used as a livingroom. Go [up] to return to the kitchen.'     
               }
         }
# creates a bank of riddles to be asked based on item in room
riddleDictionary = {

    'key' : ['You can hear me, but can not see me, and I will not answer unless spoken to. What am I?', 'echo'],

    'cookie' : ['What belongs to you but is used more by others?', 'name'],

    'potion' : ['What goes up but never comes down?' , 'age']}

#start the player in the Hall
currentRoom = 'Hall'


showInstructions()

#loop forever
while True:

  showStatus()

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':
    move = input('>')

  # split allows an items to have a space on them
  # get golden key is returned ["get", "golden key"]          
  move = move.lower().split(" ", 1)

  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
      #set the current room to the new room
      currentRoom = rooms[currentRoom][move[1]]
    #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')

  #if they type 'get' first
  if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
        # enters user into riddle when they attempt to get item, requires a correct answer to receive item
      riddleFunction(move[1])
      #add the item to their inventory
      inventory += [move[1]]
      #display a helpful message
      print(move[1] + ' got!')
      #delete the item from the room
      del rooms[currentRoom]['item']
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!')
      
  ## Define how a player can win
  if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
    print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
    break
  
  elif 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
     #alternate ending, if you have a cookie and are in the kitchen with monster you win
      if 'cookie' in inventory and 'monster' in  rooms['Kitchen']['item']:
      print('You gave the Monster your cookie, YOU WIN!')
      break
     else:
      print('A monster has got you... GAME OVER!')
      break
