from nltk.tag import CRFTagger
from nltk.corpus import brown
from sklearn.metrics import classification_report as crf

ct = CRFTagger()

ct.set_model_file("model.crf.tagger")

brown_sents = brown.sents()
size = int(len(brown_sents) * 0.7)

test_sents = brown_sents[size:]

flat_list = []
for sublist in test_sents:
    for item in sublist:
        flat_list.append(item)

l = ct.tag(flat_list)
y_pred = []

for each in l:
	y_pred.append(each[1])
	
#print(y_pred[:10])

tagged_sents = brown.tagged_sents(tagset="universal")[size:]

y_true = []
for each in tagged_sents:
	for e in each:
		y_true.append(e[1]);
	
#print(y_true[0:10])

print(crf(y_true, y_pred))

