import unittest 
from translator import  englishtofrench, frenchtoenglish

class testenglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(englishtofrench('Hello'), 'Bonjour')

class TestfrenchToEnglish(unittest.TestCase): 
    def test2(self): 
        self.assertEqual(frenchtoenglish('Bonjour'), 'Hello') 

unittest.main()