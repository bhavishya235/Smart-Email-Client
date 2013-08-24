import os
from collections import Counter
from collections import OrderedDict
import nltk
from nltk.tokenize import *
from nltk.probability import *

def my_func(x):
	return x[-1]

def main():
	
	freq_file = open('word.db','r')
	freq_dic = Counter()
	lines = freq_file.readlines()
	freq_file.close();
	
	for line in lines:
		line = line.strip()
		words2 = line.split()
		freq_dic[words2[0]] =  int(words2[1])
		
	#print freq_dic
	
	path1 = 'old/cat1'
	files =  os.listdir(path1)
	for f in files:
		if os.path.isdir(f) == False:
			fin = open(path1+'/'+f,'r').read()
			sentence = sent_tokenize(fin)
			words = []
			for it in sentence:
				tmp = word_tokenize(it)
				#Bag of words filtering
				for item in tmp:
					if len(item)>1:
						words.append(item)
			
			#Getting word frequency
			fdist = FreqDist(words)
			
			for it in fdist.items():
				if(freq_dic[it[0]]):
					freq_dic[it[0]] = freq_dic[it[0]]+it[1]
				else:
					freq_dic[it[0]] = 1
			#fin.close()
			
	freq_dic = OrderedDict(sorted(freq_dic.items(), key=lambda x: x[1],reverse=True))
	
	fout = open('word.db','w')
	
	for i in freq_dic.items():
		fout.write(i[0]+' '+repr(i[1])+'\n')
        
if __name__=='__main__':
	main()
