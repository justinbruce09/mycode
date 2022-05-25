#!/usr/bin/env python3
"""trivia API for practice"""

import os
import requests
import json

URL ='https://opentdb.com/api.php?amount=1&type=multiple'

def main():
    trivia = requests.get(URL).json()
    question = trivia["results"][0]["question"]

    print(question)
   
    # this looks perfect! just gotta unindent main()
main()
