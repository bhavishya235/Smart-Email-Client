#Inverse document frequency

import math
import os

def main():
	THRESHOLD = 0.5
	ran = range(3)
	
	for i in ran:
		path = 'class'+str(i)+'/'
		
		freq_file = open(path+'word.db').readlines()
		freq = []
		key = []

		for line in freq_file:
			tmp = line.strip()
			tmp = tmp.split()
			key.append(tmp[0])
			freq.append(int(tmp[1]))

		occ = []				#Occurence of key
		for it in key:
			occ.append(1)

		j = i+1
		while j<i+len(ran):
			f = open("./class"+str(j%len(ran))+"/word.db").readlines()
			
			for line in f:
				tmp = line.strip()
				tmp = tmp.split()
				if tmp[0] in key:
					occ[key.index(tmp[0])] += 1
			j = j+1
		
		f_out = open(path+'idf.db', 'w')
		f_out2 = open(path+'rel_word.db', 'w')
		
		j=0
		for it in key:
			tmp = (1+ math.log(freq[j],10))*math.log(len(ran)/occ[j], 10)
			f_out.write(it+" "+str(tmp)+'\n')
			if tmp>THRESHOLD:
				f_out2.write(it+" "+str(freq[j])+'\n')
			j=j+1
		

		
			
if __name__=='__main__':
	main()
