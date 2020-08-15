#!/usr/bin/python3
"""mapper1.py"""
import sys
import nltk
from nltk.corpus import stopwords
nltk.download("punkt") # to remove puntuations
from nltk.tokenize import word_tokenize
temp_tokens=[]
keywords=['science','sea','fire']
for line in sys.stdin:

    line = line.strip() # removing white spaces
    line = line.lower() # converting string to lowercase
    text_tokens=word_tokenize(line) #creating list og words
    trigram_tokens=temp_tokens #adding last 2 words of previous line
    for word in text_tokens: # iterating over list
        if word.isalnum(): #removing puntuations
            trigram_tokens.append(word)
    for i in range(0,len(trigram_tokens)-1):
        if (i< len(trigram_tokens)-2):
            if trigram_tokens[i] in keywords or trigram_tokens[i+1] in keywords or trigram_tokens[i+2] in keywords:
                out=trigram_tokens[i]+"_"+trigram_tokens[i+1]+"_"+trigram_tokens[i+2]
                out=out.replace('science','$').replace('sea','$').replace('fire','$')
                print(out,1)
        
    temp_tokens=trigram_tokens[-3:-1]
