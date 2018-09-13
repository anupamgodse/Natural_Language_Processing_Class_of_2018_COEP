import os
from nltk.parse import stanford
from nltk.parse import DependencyGraph, DependencyEvaluator

os.environ['STANFORD_PARSER'] = '/home/anupam/parsers/stanford-parser-full-2018-02-27/stanford-parser.jar'
os.environ['STANFORD_MODELS'] = '/home/anupam/parsers/stanford-parser-full-2018-02-27/stanford-parser-3.9.1-models.jar'

parser = stanford.StanfordParser()
sentences = parser.raw_parse_sents(("Hello, My name is Melroy.", "What is your name?"))
print(sentences)

# GUI
for line in sentences:
    for sentence in line:
        #sentence.draw()
        print(sentence)
