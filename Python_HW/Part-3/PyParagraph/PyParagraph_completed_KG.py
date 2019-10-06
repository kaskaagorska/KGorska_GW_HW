# -*- coding: UTF-8 -*-
"""PyParagraph Homework Solution."""

# Incorporate regular expressions (helpful for splitting by punctuation)
import re
import os

# Files to load and output (Remember to change these)
file_to_load = os.path.join('..', 'PyParagraph', 'paragraph_2.txt')
file_to_output = os.path.join('..', 'PyParagraph', 'paragraph_analysis.txt')

numlines = 0
numwords = 0
numchars = 0
avg_numwords = []
numletters_list = []
lineslist =[]

filepath = os.path.join('..', 'PyParagraph', 'paragraph_2.txt')
with open(file_to_load, 'r') as text_file:
    
    
     #Count of sentences
    lineslist = re.split("[?<=.!?] +", str(text_file))
    numlines = len(lineslist)
    
    for line in text_file:
        
        #Count of words
        wordslist = line.split()
        numwords += len(wordslist)
        

        #Count of letters per word
        for words in wordslist:
            numletters = len(words)
            numletters_list.append(numletters)
        avg_numwords = sum(numletters_list)/(numwords)
        

        #Average Sentence length        
        avg_line_len = (numwords)/(numlines)
        
        

#Printing all the values
print("Paragraph Analysis")
print("-----------------")
print("Approximate Word Count: " + str(numwords))
print("Approximate Sentence Count:" + str(numlines))
print("Average Letter Count:" + str(avg_numwords))
print("Average Sentence Length:" + str(avg_line_len))