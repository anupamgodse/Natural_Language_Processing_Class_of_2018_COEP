import xml.etree.ElementTree as ET
import nltk
from nltk.corpus import wordnet, semcor
import os, string


functionwords = ['about', 'across', 'against', 'along', 'around', 'at',
                 'behind', 'beside', 'besides', 'by', 'despite', 'down',
                 'during', 'for', 'from', 'in', 'inside', 'into', 'near', 'of',
                 'off', 'on', 'onto', 'over', 'through', 'to', 'toward',
                 'with', 'within', 'without', 'anything', 'everything',
                 'anyone', 'everyone', 'ones', 'such', 'it', 'itself',
                 'something', 'nothing', 'someone', 'the', 'some', 'this',
                 'that', 'every', 'all', 'both', 'one', 'first', 'other',
                 'next', 'many', 'much', 'more', 'most', 'several', 'no', 'a',
                 'an', 'any', 'each', 'no', 'half', 'twice', 'two', 'second',
                 'another', 'last', 'few', 'little', 'less', 'least', 'own',
                 'and', 'but', 'after', 'when', 'as', 'because', 'if', 'what',
                 'where', 'which', 'how', 'than', 'or', 'so', 'before', 'since',
                 'while', 'although', 'though', 'who', 'whose', 'can', 'may',
                 'will', 'shall', 'could', 'be', 'do', 'have', 'might', 'would',
                 'should', 'must', 'here', 'there', 'now', 'then', 'always',
                 'never', 'sometimes', 'usually', 'often', 'therefore',
                 'however', 'besides', 'moreover', 'though', 'otherwise',
                 'else', 'instead', 'anyway', 'incidentally', 'meanwhile']

for p in string.punctuation:
	functionwords.append(p)

sentence = input("Enter Sentence:\t")
target = input("Enter target word:\t")

tags = nltk.pos_tag(nltk.word_tokenize(sentence))

#print(tags)

"""
if wordnet.morphy(target) is not None:
	target = wordnet.morphy(target)
"""

#print(target)

nb_senses = len(wordnet.synsets(target))

sense_count = [0 for i in range(nb_senses)]
target_count = 0

#print(nb_senses)

directory = "xml/"

lexical_senses = []
lexical_senses_lemma = []

for filename in os.listdir(directory):
	tree = ET.parse(directory+filename)
	root = tree.getroot()
	sents = root.findall('context/p/s')
	for sent in sents:
		for wordform in sent.getchildren():
			if wordform.text == target:
				target_count += 1
				lexical_sense = wordform.get('lexsn')
				if lexical_sense is not None:
					if lexical_sense not in lexical_senses:
						lexical_senses.append(lexical_sense)
						lexical_senses_lemma.append(wordform.get('lemma'))
					
count_lexical_senses = [0 for i in range(len(lexical_senses))]
count_lexical_senses_feature = [0 for i in range(len(lexical_senses))]


for filename in os.listdir(directory):
	tree = ET.parse(directory+filename)
	root = tree.getroot()
	sents = root.findall('context/p/s')
	for sent in sents:
		for wordform in sent.getchildren():
			lexical_sense = wordform.get('lexsn')
			for j in range(len(lexical_senses)):
				if lexical_sense == lexical_senses[j]:
					count_lexical_senses[j] += 1
					if wordform.text == target:
						count_lexical_senses_feature[j] += 1

#print(lexical_senses, count_lexical_senses, count_lexical_senses_feature)


probability_sense = []

for sense in count_lexical_senses_feature:
	probability_sense.append(sense/target_count)


fw = set(nltk.word_tokenize(sentence)) - set(functionwords)

feature_words = []
for i in fw:
	feature_words.append(i)

feature_words.remove(target)
#print(feature_words)
#print(probability_sense)


max_prob = 0
max_prob_index = 0
	
for i in range(len(probability_sense)):
	if probability_sense[i] > max_prob:
		max_prob = probability_sense[i]
		max_prob_index = i

#print(wordnet.synsets(target)[max_prob_index].definition())

feature_words_sense_count = [[0 for j in range(len(lexical_senses))]for i in range(len(feature_words))]

for filename in os.listdir(directory):
	tree = ET.parse(directory+filename)
	root = tree.getroot()
	sents = root.findall('context/p/s')
	for sent in sents:
		for wordform in sent.getchildren():
			lexical_sense = wordform.get('lexsn')
			for word_index in range(len(feature_words)):
				if feature_words[word_index] == wordform.text:
					for lexical_s_i in range(len(lexical_senses)):
						if lexical_senses[lexical_s_i] == lexical_sense:
							feature_words_sense_count[word_index][lexical_s_i] += 1
									
prob_feature_words_sense_count = [[0 for j in range(len(lexical_senses))]for i in range(len(feature_words))]									

for i in range(len(feature_words)):
	for j in range(len(lexical_senses)):
		prob_feature_words_sense_count[i][j] = feature_words_sense_count[i][j] / count_lexical_senses[j]
		
		
#print(prob_feature_words_sense_count)

for i in range(len(feature_words)):
	for j in range(len(lexical_senses)):
		if prob_feature_words_sense_count[i][j] == 0:
			prob_feature_words_sense_count[i][j] = 0.0000000001


final_prob = [1 for i in range(len(lexical_senses))]

for i in range(len(feature_words)):
	for j in range(len(lexical_senses)):
		final_prob[j] *= prob_feature_words_sense_count[i][j]
		
for i in range(len(lexical_senses)):
	final_prob[i] *= probability_sense[i]

max_prob = 0
max_prob_index = 0
	
for i in range(len(probability_sense)):
	if probability_sense[i] > max_prob:
		max_prob = probability_sense[i]
		max_prob_index = i

lemma_key = lexical_senses_lemma[max_prob_index] + "%" + lexical_senses[max_prob_index]

#print(lemma_key)

l = wordnet.lemma_from_key(lemma_key)

print(wordnet.lemma((str(l)).split("'")[1]).synset().definition())

