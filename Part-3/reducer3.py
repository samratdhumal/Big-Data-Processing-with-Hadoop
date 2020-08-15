#! /usr/bin/python

from sys import stdin
import re

index = {}

for line in stdin:
	word, filename = line.split('\t')
	index.setdefault(word, {})
	for posting in filename.split(','):
		document_id, count = posting.split(':')
		index[word].setdefault(document_id, 0)

for word in index:
	filename_list = ["%s" % (document_id)for document_id in index[word]]

	filename = ','.join(filename_list)
	print('%s\t%s' % (word, filename))
