#!/usr/bin/env python3
"""Returning the location of the ISS in latitude/longitude"""
import requests
    # json data format 
    #"timestamp": 1653405504,
    #"iss_position": {
    #"latitude": "-41.8890",
    #"longitude": "-63.8429"
    #},
    #"message": "success"
URL= "http://api.open-notify.org/iss-now.json"
def main():
    # request library is running a get from the website, should receive an HTTP response
    #.json() conversts to a json dict
    resp= requests.get(URL).json()
    print(f"""
CURRENT LOCATION OF THE ISS:
Lon: {resp["iss_position"]["longitude"]}
Lat: {resp["iss_position"]["latitude"]}""" )



if __name__ == "__main__":
    main()
