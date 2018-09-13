from nltk.tag import CRFTagger
from nltk.corpus import brown

ct = CRFTagger()

brown_tagged_sents = brown.tagged_sents(tagset='universal')
size = int(len(brown_tagged_sents) * 0.7)

train_sents = brown_tagged_sents[:size]
ct.train(train_sents, 'model.crf.tagger')

#brown_sents = brown.sents()
#test_sents = brown_sents[size:]

#print(ct.tag(test_sents))
