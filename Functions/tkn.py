#Inverse document frequency example

from nltk.tokenize import * 
	
def tkn():
	
	#Tokenization
	inp = open("newmail.txt", "r").read()
	
	tokenizer = RegexpTokenizer('[\S]+(@)[\S]+|[\S]*(http)[s]?[\S]+|\w+')
	return tokenizer.tokenize(inp)
