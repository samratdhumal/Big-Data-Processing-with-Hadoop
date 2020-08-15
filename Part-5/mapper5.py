#!/usr/bin/ python3
import sys
import string
import os
import hdfs
import numpy as np
import pandas as pd

test_df = pd.read_csv('/home/cse587/Downloads/Assignment/knn/Test.csv', header = None)
test_df.to_numpy()
for line in sys.stdin:
	line_p=np.array(line.strip().split(","),dtype = float)
	train=line_p[0:(len(line_p)-1)] 
	label = int((line_p[len(line_p)-1])) 
	test_dist = np.linalg.norm(np.subtract(test_df,train.transpose()),axis = 1) 
	for i in range(np.shape(test_dist)[0]):
		print('%s\t%s' % (str(i), ', '.join([str(label),str(test_dist[i])])))
