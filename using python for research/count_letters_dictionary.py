# -*- coding: utf-8 -*-
"""
This code takes a sentence and makes a dictionary with
the letters of that occur in the sentences and
the number of times they occur.

"""

import string
alphabet = string.ascii_letters
count_letters = {}

sentence = 'Jim quickly realized that the beautiful gowns are expensive'

#%%
# initialize the character count dictionary
# 
# run through all ascii characters and set value to 0
# 

for char in alphabet:
    count_letters[char] = 0
#%%
#
# Now we run through our text and count the occurences
# of all the ascii letters (and ignoring non-letters)
# 

for char in sentence:
    if char in alphabet: # will ignore spaces, etc
        count_letters[char] += 1

print(count_letters)

#%%
# 
# Now the problem actually only asks for letters that
# occur in the sentence, so let's get rid of the 
# 0 count non-occurrences...
# 

for letter in alphabet:
    if count_letters[letter] == 0:
        del count_letters[letter]

print(count_letters)
