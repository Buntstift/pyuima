import nltk

'''
@todo add pos tags
@todo add lemmas
@todo add stems
@todo add liwc classes
@todo add polarity scores
'''

class FrequentWords:

    def __init__(self, wordsLabel, stopwords = [], outputLabel = 'FrequentWords',
                 returnNumber = 50):
        self.__wordsLabel = wordsLabel
        self.__outputLabel = outputLabel
        self.__stopwords = stopwords
        self.__returnNumber = returnNumber
    
    def process(self, res, **kwargs):
        words = kwargs[self.__wordsLabel]
        listWords = []
        for i in words:
            [listWords.append(x) for x in i]
        all_words = nltk.FreqDist(w for w in listWords 
                                  if w not in self.__stopwords)
        frequentWords = all_words.keys()[:self.__returnNumber] 
        res.update({self.__outputLabel: frequentWords})
