#import json
#import os
from deep_translator import MyMemoryTranslator

def englishtofrench(english_text):
    """English to French Translation"""
    french_text = MyMemoryTranslator(source = 'en' , target = 'fr').translate(english_text)
    print(french_text)
    return french_text

def frenchtoenglish(french_text):
    """French to English Translation"""
    english_text = MyMemoryTranslator(source = 'fr' , target = 'en').translate(french_text)
    print (english_text)
    return english_text
    