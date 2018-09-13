#to test stanford tagger


file="/home/anupam/taggers/StanfordPosTagger/textFile.txt"
while IFS= read -r line
do
    
      touch temp.txt
      echo "$line" > temp.txt
      java -cp "*" edu.stanford.nlp.tagger.maxent.MaxentTagger -model left3WordsStanfordTrainedModel.tagger -textFile temp.txt
done < "$file"

