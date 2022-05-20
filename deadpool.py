#!/usr/bin/env python3

 """deadpool dictionary Justin """

def main():
    deadpool{ "Real Name" : "Wade Winston Wilson",
            "Creators":[ "Fabian Nicieza", "Rob Liefeld"],
            "Aliases":["Merc with a Mouth", "Jack", "Wade", "Hulkpool"],
            "Powers":["Accelerated Healing Factor"," Extended longevity"," Immunity to telepathy"],
            "Universe":"Marvel"}
        

    print(f"Deadpool, aka {deadpool['Real Name]'}, written by {deadpool['Creators'[0]]}, his most commonly known alias is {deadpool['Aliases'[0]]}, with his most notable power being {deadpool['Powers'[0]]} ")

    print("Deadpool - food add")
    deadpool["fav_food"] = "chimichangas"
    print(deadpool.keys() )
    print(deadpool.values() )

   user_search= input("choose a key:"'/n')

   print(f"Deadpools {user_search} is/are deadpool.get(user_search)" )

   

    
    

    
