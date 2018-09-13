import nltk
from nltk.corpus import brown
from sklearn.metrics import classification_report as crf

taggedByStanford = nltk.corpus.reader.TaggedCorpusReader("/home/anupam/taggers/StanfordPosTagger/",  "output.txt")

tagged_by_stanford = taggedByStanford.tagged_sents(tagset="universal")

y_pred = []
for each in tagged_by_stanford:
	for e in each:
		y_pred.append(e[1]);

size = int(len(brown_sents) * 0.7)

tagged_brown_sents = brown.tagged_sents(tagset="universal")[size:]

y_true = []

for each in tagged_brown_sents:
	for e in each:
		y_true.append(e[1]);

print(crf(y_true, y_pred))
