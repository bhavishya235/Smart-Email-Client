#Inverse document frequency example

import math
import nltk
from nltk.tokenize import *
from nltk.probability import *

	
def main():
	
	#Tokenization
	inp = open("newmail.txt", "r").read()
	sentence = sent_tokenize(inp)
	
	words = []
	for it in sentence:
		tmp = word_tokenize(it)
		#Bag of words filtering
		for item in tmp:
			if len(item)>1:
				words.append(item)
	
	#Getting word frequency
	fdist = FreqDist(words)
	
	doc = open("doc1.txt", "r").readlines()
	count = 0
	key = []
	freq = []
	uniq_words = len(fdist.keys())
	prob = 1.0
	
	for it in doc:
		tmp = it.strip()
		tmp = tmp.split()
		key.append(tmp[0])
		freq.append(int(tmp[1]))
		count += int(tmp[1])
	
	for it in fdist.keys():
		n = 0
		if it in key:
			n = freq[key.index(it)]
		prob = prob+math.log((float(1+n)/float(count+uniq_words)),10)
		
	print prob
	
if __name__=='__main__':
	main()
