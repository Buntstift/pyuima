"""@file DocumentFeatures.py


Documentation for this module.

"""


def featMeanSentsLength(fileid, corpus, stopwords, **kwargs):
    '''This is blub
    @param fileid
    @param corpus
    @param stopwords
    @param **kwargs
    @retval none
    '''
    features = {}
    doc = corpus.sents(fileids=fileid)
    return {'MeanSentsLength': mean([len(s) for s in doc])}


def featMeanWordLength(fileid, corpus, stopwords, **kwargs):
    '''
    '''
    features = {}
    doc = corpus.words(fileids=fileid)
    return {'MeanWordLength': mean([len(w) for w in doc])}


def featNumberOfStopwords(fileid, corpus, stopwords, **kwargs):
    '''
    '''
    features = {}
    doc = corpus.words(fileids=fileid)
    return {'NumberOfStopwords': len([w for w in doc if w in stopwords])}


def featureFrequentWords(fileid, corpus, frequentWords = [], **kwargs):
    '''
    '''
    features = {}
    doc = corpus.words(fileids=fileid)
    features['length'] = len(doc)
    document_words = set(doc) 
    for word in frequentWords:
        features['contains (%s)', word] = (word in document_words)
    return features

def featureTextLength(fileid, corpus, **kwargs):
    '''
    '''
    features = {}
    doc = corpus.words(fileids=fileid)
    features['textLength'] = len(doc)
    return features
