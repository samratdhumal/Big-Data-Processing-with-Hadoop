#!/usr/bin/python3
"""reducer2.py"""
import sys
import operator
word_dict={}
for line in sys.stdin:
	line = line.split(" ") # removing white spaces
	if line[0] in word_dict:
		val = word_dict[line[0]]
		word_dict[line[0]]=val+1
	else:
		word_dict[line[0]]=1
sorted_dict=dict(sorted(word_dict.items(),key=operator.itemgetter(1),reverse=True))
final_dict=dict(list(sorted_dict.items())[0:10])
for (key,val) in final_dict.items():
	print(key, val)
