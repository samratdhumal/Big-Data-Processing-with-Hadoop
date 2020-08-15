#!/usr/bin/python3
"""reducer1.py"""
import sys
word_dict={}
for line in sys.stdin:
	i = line.split(" ") # removing white spaces
	if i[0] in word_dict:
		val = word_dict[i[0]]
		word_dict[i[0]]=val+1
	else:
		word_dict[i[0]]=1
for (key,val) in word_dict.items():
	print(key, val)
