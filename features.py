#!/usr/bin/env python

import json
import csv
import sys

index = 0
result = []
each = []
category = sys.argv[1]
filter_words = ['good', 'great', 'use', 'well', 'ecxellent', 'one', 'two', 'three', 'four', 'five', 'love', 'really', 'very', 'get', 'also', 'too', 'ive', 'it', 'come', 'would', 'will', 'problem', 'product', 'like', '0', 'im']
if category == 'laptops':
	filter_words.extend(['laptop', 'computer', 'o', 'x'])
if category == 'tablets':
	filter_words.extend(['tablet'])
if category == 'mobilephone':
	filter_words.extend(['mobilephone'])
if category == 'video_surveillance':
	filter_words.extend(['video', 'surveillance'])
if category == 'TVs':
	filter_words.extend(['TV'])
if category == 'camera':
	filter_words.extend(['camera'])
with open('data/result/' + category + '.txt', 'r') as f:
	for line in f:
		if index % 2 == 0:
			each.append(line.split('/')[1].split('\\')[1].split('.')[0])
		else:
			#topics = []
			data = json.loads(line)
			for i in data:
				l = i[1].split('\"')
				j = 1
				while j <= 14:
					if l[j] not in each and l[j] not in filter_words:
						each.append(l[j])
						break
					j += 2
			#each.append(topics)
			result.append(each)
			each = []
		index += 1

with open('data/features/' + category + '.csv', 'w+', newline='') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerows(result)
