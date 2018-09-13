#to train the tagger 

java -cp "*" edu.stanford.nlp.tagger.maxent.MaxentTagger -model left3WordsStanfordTrainedModel.tagger -trainFile trainingFile.txt -arch "left3words,naacl2003unknowns,wordshapes(-1,1)" -nthreads "3" -tokenize "false"

