from nltk.tokenize import *
from nltk.tokenize import RegexpTokenizer

def token(x):
	tokenizer = RegexpTokenizer('\w+|\b[\w\d_-\.]@.*\b|\bhttp.*\b')
	tokenizer.tokenize(s)
	
	print s
	
if __name__=="__main__":
	token(open("newmail.txt", "r").read())
