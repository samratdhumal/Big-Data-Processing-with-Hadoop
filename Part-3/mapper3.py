#!/usr/bin/env python

import sys
import re
import os

for line in sys.stdin:
	document_id = os.environ["map_input_file"]
	part_split = document_id.split('/');
	length_p = len(part_split)
	document_id = part_split[length_p-1]
	words = re.findall(r'\w+', line.strip())
	for word in words:
		print("%s\t%s:1" % (word.lower(), document_id))
