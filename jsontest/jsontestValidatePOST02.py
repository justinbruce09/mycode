#!/usr/bin/env
"""RESTful API stuff"""

import requests

TIMEURL ="http://date.jsontest.com"
IPURL = "http://ip.jsontest.com/"
VALIDURL = "http://validate.jsontest.com/"


def main():
    
    #PART A time request
    #accesses the webpage and delivers HTML resp
    resp = requests.get(TIMEURL)
    #converts json data to python data
    mytime = resp.json()
    mytime = mytime["time"].replace(" ", "").replace(":", "-")
    

    #PART B get my IP
    myip = requests.get(IPURL).json()
    ip = myip['ip']

    #PART C read in list of servers from a text file
    with open("/home/student/mycode/jsontest/myservers.txt") as myfile:
        mysvrs = myfile.readlines()
   
    #PART D test data to validate if it the formatting we created is json
    # via a POST request
    jsonToTest = {}
    jsonToTest["time"] = mytime
    jsonToTest["ip"] = myip
    jsonToTest["mysvrs"] = mysvrs

    mydata = {}
    mydata["json"] = str(jsonToTest)


    #PART E utilize requests to POST 
    resp = requests.post(VALIDURL, data=mydata)
    #convert response back to python data
    respjson = resp.json()
    #print python data
    print(respjson)

    # JUST display the value of "validate"
    print(f"Is your JSON valid? {respjson['validate']}")
   
if __name__ == "__main__":
    main()   





