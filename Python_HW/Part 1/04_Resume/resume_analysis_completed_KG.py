# -*- coding: UTF-8 -*-
"""Resume Analysis Module."""

import os
import string

# Counter is used later in the program
from collections import Counter

# Paths
resume_path = os.path.join("..", "04_Resume", "resume.txt")

# Skills to match
REQUIRED_SKILLS = {"excel", "python", "mysql", "statistics"}
DESIRED_SKILLS = {"r", "git", "html", "css", "leaflet"}

# function to load a file
def load_file(filepath):
    """Helper function to read a file and return the data."""
    with open(filepath, "r") as resume_file_handler:
        return resume_file_handler.read().lower().split()


# Grab the text for a Resume
word_list = load_file(resume_path)
print(word_list)
# Create a set of unique words from the resume
resume = set()

# Remove trailing punctuation from words
for token in word_list:
    # print(token)
    resume.add(token.split(',')[0].split('.')[0])

# # Remove Punctuation that were read as whole words
punctuation = set(string.punctuation)
resume = resume - punctuation
# print(resume)
#
# Calculate the Required Skills Match using Set Intersection
print("REQUIRED SKILLS")
match_required = resume.intersection(REQUIRED_SKILLS)
# print(match_required)
print("=============")
print(resume & REQUIRED_SKILLS)


# # Calculate the Desired Skills Match using Set Intersection
print("DESIRED SKILLS")
print("=============")
print(resume & DESIRED_SKILLS)

# # Resume Word Count
# # ==========================
# # Initialize a dictionary with default values equal to zero

word_count = {}.fromkeys(word_list, 0)
# print(word_count)

# # Loop through the word list and count each word.
for word in word_list:
    word_count[word] += 1
print(word_count)

# # Using collections.Counter
word_counter = Counter(word_list)
print(word_counter)

# # Comparing both word count solutions
print(word_count == word_counter)

# # Top 10 Words
print("Top 10 Words")
print("=============")
top_10 = word_counter.most_common()[:10]
top_10_dict = dict(top_10)
# print(len(word_counter.most_common()[:10]))

# Don't worry about the underscore in front of _word_count
# It is just convention for internal use only
# More info here: https://dbader.org/blog/meaning-of-underscores-in-python

# Clean Punctuation
clean_dict = {}
for w in word_counter.keys():
    if w not in punctuation:
        clean_dict[w] = word_counter[w]

print(clean_dict)
# print(resume)


# _word_count = #YOUR CODE HERE hint:
# Hint: return only words that are not in string.punctuaton
# Hint: consider using a list comprehension

# Clean Stop Words
stop_words = ["and", "with", "using", "##", "working", "in", "to"]

_word_count = {}
for i in clean_dict.keys():
    if i in stop_words:
        pass
    else:
        _word_count[i] = clean_dict[i]

print(_word_count)
# # Sort words by count and print the top 10
# sorted_words = []
final_top_10 = Counter(_word_count).most_common()[:10]
print(final_top_10)