import os
from collections import Counter
from collections import OrderedDict
import nltk
from nltk.tokenize import *
from nltk.probability import *

def my_func(x):
	return x[-1]

def main():
	path = 'class0/'
		
	freq_file = open(path+'word.db','r')
	freq_dic = Counter()
	lines = freq_file.readlines()
	freq_file.close();
	
	for line in lines:
		line = line.strip()
		words2 = line.split()
		freq_dic[words2[0]] =  int(words2[1])
		
	#print freq_dic

	files =  os.listdir(path)
	for f in files:
		if os.path.isdir(f) == False and f!="word.db" :
			fin = open(path+f,'r').read()
			tokenizer = RegexpTokenizer('[\S]+(@)[\S]+|[\S]*(http)[s]?[\S]+|\w+')
			words = tokenizer.tokenize(fin)
			
			#Getting word frequency
			fdist = FreqDist(words)
			
			for it in fdist.items():
				if(freq_dic[it[0]]):
					freq_dic[it[0]] = freq_dic[it[0]]+it[1]
				else:
					freq_dic[it[0]] = 1
			#fin.close()
			
	freq_dic = OrderedDict(sorted(freq_dic.items(), key=lambda x: x[1],reverse=True))
	
	fout = open(path+'word.db','w')
	
	for i in freq_dic.items():
		fout.write(i[0]+' '+repr(i[1])+'\n')
        
if __name__=='__main__':
	main()
