import pickle
import nltk.tag
from nltk.corpus import brown
from nltk.tag import CRFTagger
from nltk.tbl.template import Template
from nltk.tag.brill import Pos, Word
from nltk.tag import BrillTaggerTrainer

#preparing baseline CRFTagger and trainingData for brill tagger
brown_sents = brown.sents()
size = int(len(brown_sents) * 0.7)

training_data = brown.tagged_sents()[:size]

templates = [Template(Pos([-1])),
        Template(Pos([1])),
        Template(Pos([-2])),
        Template(Pos([2])),
        Template(Pos([-2, -1])),
        Template(Pos([1, 2])),
        Template(Pos([-3, -2, -1])),
        Template(Pos([1, 2, 3])),
        Template(Pos([-1]), Pos([1])),
        Template(Word([-1])),
        Template(Word([1])),
        Template(Word([-2])),
        Template(Word([2])),
        Template(Word([-2, -1])),
        Template(Word([1, 2])),
        Template(Word([-3, -2, -1])),
        Template(Word([1, 2, 3])),
        Template(Word([-1]), Word([1]))]

 
baseline = CRFTagger()

baseline.set_model_file("model.crf.tagger")
 
#training brill tagger 
tt = BrillTaggerTrainer(baseline, templates, trace=3)
taggerFinal = tt.train(training_data, max_rules=10)

pickle.dump(taggerFinal, open( "BrillFinal.p", "wb" ) )
