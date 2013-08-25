#Inverse document frequency

import math
import os
import nltk
from nltk.tokenize import *
from nltk.probability import *

train_vector = []
test_vector = []
THRESHOLD = -400
K = 1000


def myfunc(x):
	return x[-1]


def main():
	global train_vector
	ran = range(3)
	
	docs = len(ran)

	temp_li = []
	d_file = open('dictionary').readlines()
	dict_key = []
	dict_occ = []
	dict_indx = []
	
	train_file = open('training', 'w')
	
	i = 0
	for line in d_file:
		tmp = line.strip()
		tmp = tmp.split()
		dict_indx.append(i)
		dict_key.append(tmp[0])
		dict_occ.append(int(tmp[1]))
		i=i+1
		
		
	for i in ran:
		train_file.write(str(i+1))
		
		path = 'class'+str(i)+'/'
		
		freq_file = open(path+'word.db').readlines()
		freq = []
		key = []

		maximum = 0
		for line in freq_file:
			tmp = line.strip()
			tmp = tmp.split()
			key.append(tmp[0])
			freq.append(int(tmp[1]))
			if maximum<int(tmp[1]):
				maximum = int(tmp[1])
		
		f_out = open(path+'idf.db', 'w')
		f_out2 = open(path+'rel_word.db', 'w')
		
		j=0
		k=0
		for it in dict_key:
			if it in key:
				indx = key.index(it)
				tmp = (1+math.log(float(freq[indx]),10))*math.log(float(docs)/float(dict_occ[j]), 10)
				f_out.write(it+" "+str(tmp)+'\n')
				if tmp>THRESHOLD:
					train_file.write(" "+str(dict_indx[j])+":"+str(tmp))
					temp_li.append([dict_indx[j], freq[indx]])
					#train_vector.append(({dict_indx[j]: freq[indx]},i+1))
					f_out2.write(it+" "+str(freq[indx])+'\n')

			j = j+1		

		temp_li = sorted(temp_li, key=myfunc, reverse=True)

		k = 0
		temp_maarli = []
		for li in temp_li:
			if k>=K:
				break
			temp_maarli.append([li[0], li[1]])
			k=k+1
			
		temp_maarli = sorted(temp_maarli)
		for it in temp_maarli:
			train_vector.append(({it[0]: it[1]},i+1))

		f_out.close()
		f_out2.close()

		train_file.write('\n')

	train_file.close()
	
	detect()
	

def detect():
	global train_vector
	test_vector = []
	classifier = nltk.NaiveBayesClassifier.train(train_vector)
	
	docs = 4
	
	d_file = open('dictionary').readlines()
	dict_key = []
	dict_occ = []
	dict_indx = []
	
	test_file = open('test', 'w')
	test_file.write('0 ')				#Writing label 0
	
	i = 0
	for line in d_file:
		tmp = line.strip()
		tmp = tmp.split()
		dict_indx.append(i)
		dict_key.append(tmp[0])
		dict_occ.append(int(tmp[1]))
		i=i+1
		
	fin = open('newmail','r').read().lower()
	tokenizer = RegexpTokenizer('[\w\.]+(@)[\w\.]+|[\w]*(http)[s]?[^"<>\s]+|\w+')
	words2 = tokenizer.tokenize(fin)
	words = []
	
	for it in words2:
		if len(it)>2:
			words.append(it)
	
	fdist = FreqDist(words)
	
	f_out = open('test_idf.db', 'w')

	j=0
	temp_li = []
	for it in dict_key:
		if it in fdist.keys():
			tmp = (1+ math.log(float(fdist[it]),10))*math.log(float(docs)/float((dict_occ[j]+1)), 10)
			f_out.write(it+" "+str(tmp)+'\n')
			if tmp>THRESHOLD:
				test_file.write(str(dict_indx[j])+":"+str(tmp)+" ")
				temp_li.append([dict_indx[j], fdist[it]])
				
		j = j+1		
	#temp_li = sorted(temp_li, key=myfunc, reverse=True)
	for it in temp_li:
		test_vector.append({it[0]: it[1]})
	
	print test_vector
		
	f_out.close()
		
	test_file.close()

	count1 = float(0)
	count2 = float(0)
	count3 = float(0)
	for it in test_vector:
		if classifier.classify(it)==3:
			count3 += 1
		if classifier.classify(it)==2:
			count2 += 1
		if classifier.classify(it)==1:
			count1 += 1

	summ = float(count1+count2+count3)
	print count1/summ*100
	print count2/summ*100
	print count3/summ*100
			
			
if __name__=='__main__':
	main()
