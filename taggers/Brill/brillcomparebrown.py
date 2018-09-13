import pickle
import nltk.tag
from nltk.corpus import brown
from nltk.tag import CRFTagger
from nltk.tbl.template import Template
from nltk.tag.brill import Pos, Word
from nltk.tag import BrillTaggerTrainer

#testing brill tagger

brown_sents = brown.sents()
size = int(len(brown_sents) * 0.7)

taggerFinal = pickle.load( open( "BrillFinal.p", "rb" ) )

test_sents = brown_sents[size:]
li = []
for each in test_sents:
	for e in each:
		li.append(e)
tagged_final = taggerFinal.tag(li)

#preparing predicted tags list
y_pred = []

for each in tagged_final:
	y_pred.append(each[1])


#preparing true tags list
tagged_sents = brown.tagged_sents(tagset="universal")[size:]

y_true = []
for each in tagged_sents:
	for e in each:
		y_true.append(e[1]);
	

print(crf(y_true, y_pred))

