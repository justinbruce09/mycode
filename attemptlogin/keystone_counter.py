#!/usr/bin/env python3

"""Justin parsing through some openstack keystone stuff"""
#create a counter for failed login attempts
loginfail = 0

#open the keystone file
keystone_file= open("/home/student/mycode/attemptlogin/keystone.common.wsgi", "r")

#make the file into a list of lines
keystone_file_lines=keystone_file.readlines()
#create a for loop for the text
for line in keystone_file_lines:
    #search for the login failure
    if "- - - - -] Authorization failed" in line:
       #increment when the above pattern is found
        loginfail+=1
        #print the results

print(f"The number of failed login attempts is {loginfail}")
# because the print is indented under the for loop,
# this will print EVERY time the for loop loops :)

#close the file
keystone_file.close()


