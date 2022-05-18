#!/usr/bin/env python3
"""just learning some shutil stuff Justin"""
#import statements
import shutil
import os

def main():
    # move into the working directory
    os.chdir("/home/student/mycode/")
    #copy a file
    shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")
    #copy a folder/directory
    shutil.copytree("5g_research/", "5g_research_backup/")

if __name__ =="__main__":
    main()

