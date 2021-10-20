def is_palindrome(word):
     forward = ''.join (e for e in word.lower() if e.isalpha())
     forward = list (forward)
     backward = forward[::-1]   # Inverting the string
     return forward == backward  # comparison between forward and backward strings
