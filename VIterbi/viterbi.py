import sys
from collections import Counter, defaultdict
from nltk.probability import ConditionalFreqDist as CFD
from nltk.tokenize import TreebankWordTokenizer
from nltk.corpus import treebank
from pprint import pprint
from math import log


T=CFD()
L=CFD()

def extractTransitions(tagged_sents=treebank.tagged_sents(tagset='universal')):
	for s in tagged_sents:
		lasttag = 0
		for token,tag in s:
			T[lasttag][tag]+=1
			L[tag][token]+=1
			lasttag = tag

#Transition probability
def Pt(lasttag, tag):
	p = T[lasttag].freq(tag)
	p = 0.005 if p == 0 else p
	return log(p)

#Likelihood of word belonging to tag
def Pl(word, tag):
	p = L[tag].freq(word)
	p = 0.000001 if p == 0 else p
	return log(p)

def printseqw(seqptr):
	for tag in seqptr[0].keys():
		print "|%12s"%(tag),
	print '|'
	for d in seqptr:
		for w,ptr in d.values():
			print "|%7.2f,%4s"%(w,ptr),
		print '|'

def viterbi(seq):
	Nt=len(seq)
	if Nt == 0:
		return

	tags = T.keys()
	tags.remove(0)
	#init
	seqptr = [{}]
	seqptr[0] = {tag: (Pl(seq[0], tag)+Pt(0,tag), 0) for tag in tags }
	#forward
	for t in xrange(1, Nt):
		dt = {}
		for tag in tags:
			maxp= -0xfffffff
			ptr = ''
			for lasttag in tags:
				p = seqptr[t-1][lasttag][0]+Pt(lasttag,tag)
				if p > maxp:
					maxp = p
					ptr = lasttag
			dt[tag] = (maxp+Pl(seq[t],tag) , ptr)
		seqptr.append(dt)
	#backtrack
	#printseqw(seqptr)
	tagmax = max(seqptr[Nt-1], key=lambda k: seqptr[Nt-1][k][0])
	tagseq = [tagmax]
	ptr = seqptr[Nt-1][tagmax][1]
	for t in xrange(Nt-2, -1, -1):
		tagseq.insert(0, ptr)
		ptr = seqptr[t][ptr][1]
	print "Tag sequence",tagseq
	



#print "Viterbi demo"
#print "Loading statistics from WSJ Penn Treebank"
extractTransitions()
print "Enter sentence to be tagged"
tbtk = TreebankWordTokenizer()

def demo():
	for line in sys.stdin:
		seq = tbtk.tokenize(line)
		viterbi(seq)

demo()
