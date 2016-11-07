'''
Given a string return the longest palindrome that can be constructed by removing or shuffling characters. 
Example: 
'aha' -> 'aha' 
'ttaatta' -> ' ttaaatt' 
'abc' -> 'a' or 'b' or 'c' 
'gggaaa' -> 'gaaag' or 'aggga' 
Note if there are multiple correct answers you only need to return 1 palindrome.
'''

def longest_palin(str):
    dict = {}
    '''
    dict = {str[i]: 1 if not dict.get(str[i]) else dict.get(str[i])+ 1 
            for i in range(len(str))}
    '''
    for i in range(len(str)):
        if str[i] in dict.keys():
            dict[str[i]] += 1
        else:
            dict[str[i]] = 1
    
    left = ""
    right = ""
    center = ""
    centerkey = ''
    count = 0
    for key in dict.keys():
        if dict[key]% 2 == 1:
            if dict[key] > count:
                centerkey = key
                count = dict[key]

    for key in dict.keys():
        if key != centerkey:
            for i in range(dict[key]/2):
                left = left + key
                right = key + right

    for i in range(dict[centerkey]):
        center = center + centerkey

    return left + center + right
                      
def main():
    print(longest_palin("gggaaa"))
    
main()         
            
            
            
            
            
            
            
            
            
            
            