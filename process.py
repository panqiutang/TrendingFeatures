# part of this code comes from a tutorial: https://www.analyticsvidhya.com/blog/2016/08/beginners-guide-to-topic-modeling-in-python/
# run LDA on parsed dataset to obtain topic distributions

import warnings
import gensim
from gensim import corpora
from nltk.corpus import stopwords 
from nltk.stem.wordnet import WordNetLemmatizer
import string
import glob
import json
import sys

warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')

def clean(doc):
    stop_free = " ".join([i for i in doc.lower().split() if i not in stop])
    punc_free = ''.join(ch for ch in stop_free if ch not in exclude)
    normalized = " ".join(lemma.lemmatize(word) for word in punc_free.split())
    return normalized

category = sys.argv[1]
outfile = open('data/result/' + category + '.txt', 'w+')

filenames = sorted(glob.glob('data/' + category + '/*.json'))
for file in filenames:
	with open(file, 'r', encoding='utf-8') as f:
		lines = f.readlines()
	doc_complete = [x.strip() for x in lines]

	stop = set(stopwords.words('english'))
	exclude = set(string.punctuation) 
	lemma = WordNetLemmatizer()

	doc_clean = [clean(doc).split() for doc in doc_complete]

	# Creating the term dictionary of our courpus, where every unique term is assigned an index. 
	dictionary = corpora.Dictionary(doc_clean)

	# Converting list of documents (corpus) into Document Term Matrix using dictionary prepared above.
	doc_term_matrix = [dictionary.doc2bow(doc) for doc in doc_clean]

	# Creating the object for LDA model using gensim library
	Lda = gensim.models.ldamodel.LdaModel

	# Running and Trainign LDA model on the document term matrix.
	ldamodel = Lda(doc_term_matrix, num_topics=5, id2word = dictionary, passes=50)

	out = ldamodel.print_topics(num_topics=5, num_words=7)
	print(out)
	outfile.write('%s\n' % file)
	json.dump(out, outfile)
	outfile.write('\n')

outfile.close()