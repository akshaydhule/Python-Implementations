'''
Validate if a given string is numeric.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
Note: It is intended for the problem statement to be ambiguous. 
You should gather all requirements up front before implementing one.
'''

def isNumber( s):
    s1 = s
    s = s.strip() #clear spaces
    if len(s1) == 0 or len(s) == 0:
        return False
    exp = False
    noset = {'0','1','2','3','4','5','6','7','8','9'}
    if s[0] == '-' or s[0] == '+':
        s= s[1:]
    if s.endswith('e') or s.startswith('e'):
        return False
    esplit = s.split('e')
    if len(esplit) > 2 :
        return False
    if len(esplit) == 2:
        exp = True
    count = 0
    for str in esplit:
        if (str.endswith('e')  or str.startswith('e')) : #e exists
            return False
        if str.endswith('-') or str.endswith('+'): #no number after sign
            return False
        if count == 1 and (str[0] == '+' or str[0] == '-'): #remove sign
            str = str[1:]
        decsplit = str.split('.') #split on .    
        if len(decsplit) > 2 or (len(str) == 1 and str == '.'): #more than one .'s
            return False
        if count == 1 and exp == True and len(decsplit) == 2 : 
            return False
        for decstr in decsplit: 
            for i in range(len(decstr)):
                if decstr[i] not in noset: #not number
                    return False
        count += 1
    return True
    
print(isNumber(" 005047e+6"))