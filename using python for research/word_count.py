#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 19:50:22 2018

@author: robert
"""

inputfile = "gettysburg.txt"
with open(inputfile,"r") as f:
    text = f.read()     # text now contains the Gettysburg address

# Now get rid of the end of linefeed and carriage return
# characters

text = text.replace("\n","")
text = text.replace("\r","")


def count_words(text):
    """This makes a dictionary of the words with key values being 
    the count of the number of times that word appears. 
    """
    text = text.lower()
    skips = [",",".",";",":","!","?","'",'"']
    for ch in skips:
        text = text.replace(ch,"")
    word_counts = {}
    for word in text.split(" "):
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
        return word_counts 

# there is a faster way using a built in fuction...

from collections import Counter

def fast_count_words(text):
    """
    A word counter that uses the collections library function
    called Counter.
    """
    text = text.lower()
    skips = [",",".",";",":","!","?","'",'"']
    for ch in skips:
        text = text.replace(ch,"")
    word_counts = Counter(text.split(" "))
    return word_counts



    