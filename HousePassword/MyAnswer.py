import re

'''
Its the regex thats fucking it up!

also look at AND & OR operators for regexs
'''

def checkio(password):
    if re.search("[\d]",password) and re.search("[a-z]",password) and re.search("[A-Z]",password) and 9 < len(password) <= 64:
        return True
    else:
        return False