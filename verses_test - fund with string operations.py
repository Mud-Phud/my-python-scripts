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

#print(contents)

# make an array with the index (position) of the strings "1", "2",...

# first initialize it to 0...

indices = [0 for i in range(30)]

# Now find the "verses" indices...

for i in range(100):
    current_index = contents.find(str(i+1))
    if current_index != -1 :
        indices[i] = current_index

print(indices)

# how many verses are there? We can make the verse index numbers = 1 and 
# then sum. How to do that? This works:

number_of_verses = sum([ i != 0 for i in indices]) + 1
print(number_of_verses)

# we can print out the verses:

for i in range(number_of_verses):
    print(contents[indices[i]:indices[i+1]])
# need to print the last verse:
print(contents[indices[number_of_verses-1]:])

front_matter = "<!DOCTYPE html>\n"\
"<html>\n"\
"<head>\n"\
"<style>\n"\
"table, th, td {\n"\
"  border: 1px solid black;\n"\
"  border-collapse: collapse;"\
"}\n"\
"</style>\n"\
"</head>\n" \
"<body>\n"\
"\n"\
"<h1>Table with Collapsed Borders</h1>\n"

# 
# A table in html:
#
# <table>
#   <tr>
#     <td>Month</td>
#     <td>Savings</td>
#   </tr>
#   <tr>
#     <td>January</td>
#     <td>$100</td>
#   </tr>
# </table>
#

table_code = "<table>\n"

for i in range(number_of_verses):
    table_code += "  <tr>\n    <td>"\
        + contents[indices[i]:indices[i+1]] \
        + "</td>\n"

table_code += "\table\n"

end_matter = "</body>\n </html>\n"

html_code = front_matter + table_code + end_matter

print(html_code)

# my_html = open("myfile.html", "x")
# my_html.write()

# myfile.close()