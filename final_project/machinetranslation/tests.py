import unittest 
from translator import  englishtofrench, frenchtoenglish

class testenglishtofrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(englishtofrench('Hello'), 'Bonjour')
        self.assertNotEqual(englishtofrench('Good Afternoon'), 'Bonjour')

class Testfrenchtoenglish(unittest.TestCase): 
    def test2(self): 
        self.assertEqual(frenchtoenglish('Bonjour'), 'Hello') 
        self.assertNotEqual(frenchtoenglish('Bonsoir'), 'Good Morning') 
unittest.main()