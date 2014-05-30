import unittest
import pyuima
from pyuima.Base import Pipeline
import pandas as pd
import nltk
from nltk.corpus.reader import CategorizedPlaintextCorpusReader as reader



class TestPipeline(unittest.TestCase):
    ''' Test functions for the basic pipeline

    '''

    def setUp(self):
         self.text = {'eins': 'Russland hat mehrere Tausend Soldaten von der Grenze zur Ukraine abgezogen.',
                      'zwei': 'Na, sitzen Sie heute allein im Buero, weil sich praktisch alle anderen oberschlauen Kollegen diesen Freitag freigenommen haben?'}

    def test_Pipeline(self): 
        print self.text
        pipe = Pipeline(self.text, corpusFormat = 'dict')


if __name__ == '__main__':
    unittest.main()
