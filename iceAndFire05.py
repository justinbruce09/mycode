#!/usr/bin/env python3

import requests
import pprint

AOIF_House = "https://www.anapioficeandfire.com/api/houses"

def name_finder(got_list):
    names=[] #list returns back characters house
    for x in got_list:
        #send a GET to one of the entries from list
        r= requests.get(x)
        decodedjson = r.json() # convert to JSON
        names.append(decodedjson.get("name"))
    return names
def main():
    ## Ask user for input
        got_charToLookup = input("Pick a number between 1 and 1000 to return info on a GoT character! " )

        ## Send HTTPS GET to the API of ICE and Fire character resource
        gotresp = requests.get(AOIF_CHAR + got_charToLookup)

         ## Decode the response
        got_dj = gotresp.json()
        pprint.pprint(got_dj)

        # call our function
        print("This character belongs to the following houses:")
        for x in name_finder(got_dj.get("allegiances")):
            print(x)

        print("This character appears in the following books:")
        for x in name_finder(got_dj.get("books")):
            print(x)

if __name__ == "__main__":
    main()
