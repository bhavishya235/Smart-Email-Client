#Inverse document frequency example

import math
import nltk
from nltk.tokenize import *
from nltk.probability import *
from nltk.tokenize import RegexpTokenizer
 
def my_func(x):
	return x[-1]
	
	
def main():
	
	#Tokenization
	inp = open("body2.txt", "r").read()
	tokenizer = RegexpTokenizer('\w+')
	words = tokenizer.tokenize(inp)
	print words
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
		
			
	inp2 = open("body.txt", "r").read()
	sentence2 = sent_tokenize(inp2)
	
	words2 = []
	for it in sentence2:
		tmp = word_tokenize(it)
		#Bag of words filtering
		for item in tmp:
			if len(item)>1:
				words2.append(item)
	
	#Getting word frequency
	fdist2 = FreqDist(words2)
	
	idf = []
	for it in fdist.items():
		if it[0] in words2:
			n = 2
		else:
			n = 1
		tmp = (1+ math.log(it[1],10))*math.log(2/n, 10)
		idf.append((it[0], tmp))
	
#	print sorted(idf, key=my_func, reverse=True)
	
	
	
if __name__=='__main__':
	main()
