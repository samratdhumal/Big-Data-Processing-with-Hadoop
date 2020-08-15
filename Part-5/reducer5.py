#!/user/bin/python3
from operator import itemgetter
import sys
import numpy as np
import pandas as pd
from scipy import stats
current_ind = ''
current_label_list = []
current_dist_list = []
k = 3
for line in sys.stdin:
	line = line.strip()
	test_ind,dist_label = line.split('\t', 1)
	label,dist = dist_label.split(', ')
	if test_ind == current_ind:
		current_label_list.append(int(label))
		current_dist_list.append(float(dist))
	else:
		sorted_ind = np.argsort(current_dist_list)[0:k-1]
		sorted_labels = []
		for i in sorted_ind[0:(k-1)]:
			sorted_labels.append(current_label_list[i])
		final_label = stats.mode(sorted_labels)[0]
		print('%s\t%s' % (str(current_ind), str(final_label)))
		current_ind = test_ind
		current_label_list = []
		current_label_list.append(label)
		current_dist_list = []
		current_dist_list.append(float(dist))

print('%s\t%s' % (str(test_ind), str(final_label)))
