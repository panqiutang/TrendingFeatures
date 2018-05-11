# parse the original dataset into JSON format.
# output: a directory of files, each represents one year of reviews, each line in every file represent one review

import json
from pprint import pprint
import glob
import sys

reviews = {}
category = sys.argv[1]
path = 'AmazonReviews'
if len(sys.argv) > 2:
	path = sys.argv[2]
file_names = glob.glob(path + '/' + category + '/*.json')
for f in file_names:
	data = json.load(open(f))
	for r in data['Reviews']:
		year = r['Date']
		if year is None:
			continue
		year = year.split(', ')[1]
		if year in reviews:
			content = reviews[year]
		else:
			content = []
		content.append(r['Content'])
		reviews[year] = content

os.makedirs('data/' + category)
for key, value in reviews.items():
	s = 'data/' + category + '/' + key + '.json'
	with open(s, 'w', encoding='utf-8') as f:
		for each in value:
			f.write("%s\n" %each)