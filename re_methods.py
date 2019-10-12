'''
Examples of using regex methods with re module
By Binggang Liu
'''

import re

text_for_search = '''
1234598760 abcde ABCDE : ; , ' " / & @ % ! ~

MetaCharacters (which need to be escaped):
. ^ $ * + ? {} { } [] [ ] ( ) 0 \ |
for example, regular expression for searching eaglesoarllc.com: r'eaglesoarllc\.com'

312.345.4567
612-456-2345
432*434*3245
221#332#3333

star, tar, atar, itar

Mr. Stone 
Mr Jacobson
Mrs. Davison
Ms Major
Mr. K

Gen.2:23  Gen.34:1  Psa.105:3   Psa.4:28  Psa.149:9

word.  ford, kord; exort: hood?
'''

#pattern = re.compile(r'^') 
    #will match the empty charater '' in the beginning of first line
#pattern = re.compile(r'^''') 
    #will match the empty charater '' in the beginning of first line
#pattern = re.compile(r'\^') 
    #will match the ^ charater in the text
#pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d') 
    # '.' will match all symbols between the numbers
#pattern = re.compile(r'\d{3}.\d{3}.\d{4}') 
    # this is equivalent to the snippet above   
#pattern = re.compile(r'\d\d\d\.\d\d\d\.\d\d\d\d') 
    # '\.' will only match '.'
#pattern = re.compile(r'\d\d\d[-.*]\d\d\d[-.*]\d\d\d\d') 
    # will match anything inside the square bracket, dot inside the square bracket does not need to be escaped
#pattern = re.compile(r'[36]12[.-]\d\d\d[-.]\d\d\d\d') 
    #will match 312.345.4567, and 612-456-2345
#pattern = re.compile(r'[2-5]') 
    #will match all numbers from 2 to 5
#pattern = re.compile(r'[a-zA-Z]') 
    #will match all characters from a-z, A-Z
#pattern = re.compile(r'[^a-zA-Z]') 
    #will match all characters not in a-z, A-Z
#pattern = re.compile(r'[^i]tar') 
    #will match all characters followed by tar, including ' tar'
#pattern = re.compile(r'Mr\.?\s[A-Z]\w*') 
    # will match Mr., Mr, ('?' means 0 or one) followed by a space, then any one Capital letter, then 0 or more word letters
#pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*') 
    # will match all titles followed by a space, then any one Capital letter, then 0 or more word letters
#pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*') 
    #another way
#pattern = re.compile(r'\.(\d|\d\d|\d\d\d):') 

pattern = re.compile(r'\w(\.|,|;|:|\?|\'|\'s|\)|!)') 

matches = pattern.finditer(text_for_search)

for match in matches:
    print(match)

