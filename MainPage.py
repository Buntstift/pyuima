"""@mainpage pyuima

@section Introduction
pyuima offers a simple pipeline for natural language processing. It is designed for text classification.

@section Pipeline

The general pipeline is as follows:

@section Components

@subsection DocumentAnnotators
@code
class WordTokenize:
    '''
    '''
    def __init__(self, rawTextLabel = 'text', outputLabel = 'tokens',
                 tokenizer = nltk.tokenize.PunktWordTokenizer):
        '''
        '''
        self.rawTextLabel = rawTextLabel
        self.outputLabel = outputLabel
        self.tokenizer = tokenizer
        
    def process(self, res, **kwargs):
        tokenize = self.tokenizer()
        tokens = tokenize.tokenize(kwargs[self.rawTextLabel])
        res.update({self.outputLabel:tokens})
@endcode

@subsection CorpusAnnotators
@code
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
@endcode

@subsection FeatureExtractors 
@code
class DocumentLength:
    ''' Computes the number of tokens of a given text'''

    def __init__(self, inputRawTextLabel = "raw", 
                 outputLabel = "FeatureTextLength"):
        ''' Constructor

        @param inputRawText = "raw"
        @param outputLabel = "FeatureTextLength"
        '''
        self.inputRawTextLabel = inputRawTextLabel
        self.outputLabel = outputLabel

    def process(self, features, **kwargs):
        '''
        '''
        features.update({self.outputLabel: len(kwargs[self.inputRawTextLabel])})
@endcode

@section Example Pipeline

@code

# Sample Pipeline

# loading test texts
textData = PlaintextCorpusReader('/home/david/Dropbox/Master/Info/master_thesis/nltk/corpora/test/', 
                                '.*\.txt',  encoding = 'utf-8')

textDataDict = {
'file1.txt': u'Philipp Lahm hat erneut Probleme mit dem linken Sprunggelenk.',
'file2.txt': u'Ein Volkswagen f\xfcr Kenia, das ist die Vision des Briten Joel Jackson. ',
'file3.txt': u'Russland hat mehrere Tausend Soldaten von der Grenze zur Ukraine abgezogen. \n'}

psychData = pd.DataFrame({'fileId':['file1.txt', 'file2.txt', 'file3.txt'], 'geschl':['m', 'w', 'm']})

featPipe = Pipe(textDataDict, psychData, fileIdLabel='fileId', corpusFormat='dict')
featPipe.initDocumentAnnotators(dA.WordTokenize(outputLabel='tokens'))
featPipe.initCorpusAnnotators(cA.FrequentWords(wordsLabel= 'tokens', returnNumber=5))
featPipe.initFeatureExtractors(fE.DocumentLength(inputRawTextLabel= 'tokens'))
featPipe.run()
featPipe.printRes()

print "\nResult Set for Classifier"
pprint.pprint(featPipe.getResCl(resCol='geschl'))

print "\nResult Set as DataFrame"
pprint.pprint(featPipe.getResDf(resCols=['geschl']))

@endcode

@code
'Data'
      fileId geschl
0  file1.txt      m
1  file2.txt      w
2  file3.txt      m

[3 rows x 2 columns]
'CAS'
{'file1.txt': {'fileId': 'file1.txt',
               'text': u'Philipp Lahm hat erneut Probleme mit dem linken Sprunggelenk.',
               'tokens': [u'Philipp',
                          u'Lahm',
                          u'hat',
                          u'erneut',
                          u'Probleme',
                          u'mit',
                          u'dem',
                          u'linken',
                          u'Sprunggelenk.']},
 'file2.txt': {'fileId': 'file2.txt',
               'text': u'Ein Volkswagen f\xfcr Kenia, das ist die Vision des Briten Joel Jackson. ',
               'tokens': [u'Ein',
                          u'Volkswagen',
                          u'f\xfcr',
                          u'Kenia',
                          u',',
                          u'das',
                          u'ist',
                          u'die',
                          u'Vision',
                          u'des',
                          u'Briten',
                          u'Joel',
                          u'Jackson.']},
 'file3.txt': {'fileId': 'file3.txt',
               'text': u'Russland hat mehrere Tausend Soldaten von der Grenze zur Ukraine abgezogen. \n',
               'tokens': [u'Russland',
                          u'hat',
                          u'mehrere',
                          u'Tausend',
                          u'Soldaten',
                          u'von',
                          u'der',
                          u'Grenze',
                          u'zur',
                          u'Ukraine',
                          u'abgezogen.']}}
'CAS Corpus'
{'FrequentWords': [u'hat', u',', u'Briten', u'Ein', u'Grenze']}
'Features'
[{'FeatureTextLength': 9, 'fileId': 'file1.txt'},
 {'FeatureTextLength': 11, 'fileId': 'file3.txt'},
 {'FeatureTextLength': 13, 'fileId': 'file2.txt'}]

Result Set for Classifier
[({'FeatureTextLength': 9}, 'm'),
 ({'FeatureTextLength': 11}, 'm'),
 ({'FeatureTextLength': 13}, 'w')]

Result Set as DataFrame
   FeatureTextLength     fileId geschl
0                  9  file1.txt      m
1                 11  file3.txt      m
2                 13  file2.txt      w

[3 rows x 3 columns]
@endcode

@section Issues

@author David Hoppe
"""


