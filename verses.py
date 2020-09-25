#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
I want to scan a string and find "verse" numbers and divide it up into verses.


Created on Mon Sep 21 00:30:20 2020

@author: robert
"""

# input the file name and proceed: Will comment out for now.
# input the file name...

# print('Enter the file name:')
# file_name = input()

file_name = "atos-1.txt"

myfile = open(file_name, encoding='utf-8')

contents = myfile.read()
#print(contents)

print(contents.find("meu"))
print(contents[5:8])

# get rid of the end of lines in the text...

contents = contents.replace("\n", " ")
#print(contents)

index14 = contents.find("14")
index15 = contents.find("15")
print(contents[index14:index15])

# want to get rid of double spaces
# Remember:
# if contents.find(string) doesn't find any instances, it returns -1.

while(contents.find("  ") > 0):
    contents = contents.replace("  "," ")

print(contents)

myfile.close()