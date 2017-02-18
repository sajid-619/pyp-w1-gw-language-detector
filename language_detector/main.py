# -*- coding: utf-8 -*-

"""This is the entry point of the program."""

def detect_language(text, languages):
    """Returns the detected language of given text."""
    # implement your solution here
    high_count = 0
    count_lang = ""
    for language in languages:
        
        cur_count = 0
        for word in text.split():
            
            if word in language['common_words']:
                cur_count +=1
        if cur_count > high_count:
            high_count = cur_count
            count_lang = language['name']
            
    return count_lang
