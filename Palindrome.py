import re

def palindrome_checker(word):
    forwards = ''.join(re.findall(r'[a-z]+', word.lower())) 
    backwards = forwards[::-1] # Inverting the string
    return forwards == backwards # comparison between forward and backward strings

