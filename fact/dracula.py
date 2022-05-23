#!/usr/bin/env python3
"""Dracula book file import Justin"""
count=0
with open("dracula.txt", "r") as book:
    for line in book:
        if "vampire" in line.lower():
            print(line)
            count+=1
            with open("vampytimes.txt", "a") as vampi:
                vampi.write(line + "\n")
print(count)
