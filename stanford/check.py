from nltk.tag import StanfordPOSTagger
from nltk.corpus import brown

brown_sents = brown.sents()
size = int(len(brown_sents) * 0.7)

# Add the jar and model via their path (instead of setting environment variables):
jar = '/home/anupam/taggers/StanfordPosTagger/stanford-postagger.jar'
model = '/home/anupam/taggers/StanfordPosTagger/stanfordTrainedModel.tagger'

pos_tagger = StanfordPOSTagger(model, jar, encoding='utf8')

test_sents = brown.sents()[size+18:]

sent = "Mostly the scene was crowded with mourners , such as the dramatic Dell'Arca Lamentation in Bologna , where the grief-stricken spectators had usurped Mary's last poignant moment ."

sents_words = sent.split(" ")

print (sents_words)

print (pos_tagger.tag(sents_words))

"""i = 0
f = open("output.txt", "w")
print("entering")
for each in test_sents:	
	del pos_tagger	
	pos_tagger = StanfordPOSTagger(model, jar, encoding='utf8')
	print("entering")
	i = i + 1
	for e in each:
		sents_words.append(e)
	text = pos_tagger.tag(sents_words)
	for x in text:
		f.write(x[1] + '\n')
	print(i)	
	sents_words.clear()"""
