# -*- coding: utf-8 -*-
"""
This code takes a input_string and returns a dictionary with
the letters of that occur in the sentences and
the number of times they occur.

Exercise 1c in the Python for research

"""
most_frequent_letter= ""
frequency = 0 

for letter in address_counter:
    print(most_frequent_letter, frequency,letter,letter_freq)
    if address_counter[letter] > frequency:
        most_freqent_letter = letter
        frequency = letter_freq

print(most_frequent_letter, frequency)
    