#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: robert

We look at 'necklaces' which are sets where cycling through doesn't matter

E.g., AAB = ABA = BAA


"""

# Here is a function that takes list of strings and another list of strings
# and makes a list of combination of the concatenations

def list_cat_list(L1,L2):
    L3 = []
    for a in L1:
        for b in L2:
            L3.append(a + b)
    return L3



# Now we want to define a function that takes a word and generates
# the "necklace". E.g, 'ABB' => ['ABB', 'BAB', 'BBA'].
# Sometimes this will generate redundancies, for example
# 'ABAB' => ['ABAB', 'BABA', 'ABAB','BABA']. So let's first 
# write a routine that eliminates redundancies...

def remove_redundant(L):
    assert(type(L) == list)
    new_L = []
    for i in L:
        if ( i not in new_L): new_L.append(i)
    return new_L

# now the necklace generation...


def necklace(a):
    assert(type(a) == str)
    result = []
    for i in range(len(a)):
        result.append(a)
        a = a[len(a)-1]+a[0:len(a)-1]


# Now given n = number of characters, we want to generate all
# words and then group them in necklaces = equivalent classes.
    
char_list = ['A','B','C','D','E']

n_chars = 2

L0 = char_list[0:n_chars]

############################################

n = 15 # = the length of words

L = L0

for i in range(n-1):
    L = list_cat_list(L, L0)

# now we go through the words in L and add the necklace of the word to
# our list of necklaces if the word isn't already in the list of 
# necklaces already.

necklaces = []

for a in L:
    already_in = False
    for N in necklaces:
        if a in N:
            already_in = True
            break
    if not already_in:
        necklaces.append(necklace(a))


necklaces_summary = []
for N in necklaces:
    necklaces_summary.append([N[0], len(N)])
print(necklaces_summary)

for i in necklaces_summary:
    if i[1] != n: print(i)


