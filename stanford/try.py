from nltk.tag import StanfordPOSTagger
from nltk import word_tokenize

# Add the jar and model via their path (instead of setting environment variables):
jar = '/home/anupam/taggers/StanfordPosTagger/stanford-postagger.jar'
model = '/home/anupam/taggers/StanfordPosTagger/stanfordTrainedModel.tagger'

pos_tagger = StanfordPOSTagger(model, jar, encoding='utf8')

text = pos_tagger.tag(word_tokenize("What's the airspeed of an unladen swallow ?"))
print(text)
