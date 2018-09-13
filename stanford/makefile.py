import nltk
from nltk.corpus import brown

brown_sents = brown.sents()
size = int(len(brown_sents) * 0.7)

test_sents = brown_sents[size:]

testing = open('textFile.txt','w') 
for sublist in test_sents:
	for item in sublist:
		testing.write(item + " ")		    
		if(item == "."):
			testing.write("\n")    

