#!/usr/bin/python3
"""mapper1.py"""
import sys
import nltk
from nltk.corpus import stopwords
nltk.download("punkt") # to remove puntuations
nltk.download("stopwords") # to remove stop words
from nltk.tokenize import word_tokenize

for line in sys.stdin:

    line = line.strip() # removing white spaces
    line = line.lower() # converting string to lowercase
    text_tokens=word_tokenize(line) #creating list og words
    for word in text_tokens: # iterating over list
    	if not word in stopwords.words(): #removing stop words
    		if word.isalnum(): #removing puntuations
    			print(word, 1)
