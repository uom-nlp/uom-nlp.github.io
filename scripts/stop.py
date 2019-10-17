from spacy.lang.en.stop_words import STOP_WORDS
from spacy.lang.en import English
from collections import defaultdict
import operator
import string

input = "abstract.txt"
stopwords = set(["propose", "task", "data", "training", "outperforms", "proposed", "level", "natural", 
    "method", "performance", "evaluation", "paper", "text", "based", "results", "state-of-the-art",
    "english", "including", "work", "tasks", "substantial", "improvements"])

nlp = English()

word_freq = defaultdict(int)

for line in open(input):
    for w in nlp(line):
    #for w in line.strip().split():
        if (not w.is_stop) and (w.text.lower() not in stopwords):
        #wx = w.translate(str.maketrans('', '', string.punctuation))
        #if (not nlp.vocab[wx].is_stop) and (wx.lower() not in stopwords):
            print(w, end=" ")
    print()

#for w, f in sorted(word_freq.items(), reverse=True, key=operator.itemgetter(1))[:100]:
#    if not nlp.vocab[w].is_stop:
#        print(w, f)
