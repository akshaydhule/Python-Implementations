'''
Given an array of words (i.e. ["ABCW", "BAZ", "FOO", "BAR", "XTFN", "ABCDEF"]), 
find the max value of length(s) * length(t), where s and t are words from the array. 
The catch here is that the two words cannot share any characters. 
Assume that there are many words in the array (N words) and average length of word is M. 

Answer for the example above is "ABCW" and "XTFN" as the result is 4 * 4 = 12. 
"ABCW" and "ABCDEF" do not work since they share similar characters.
wordlist[i]: [] for i in range(len(wordlist))
'''

def printdict(dict = {}):
    for key in dict.keys():
        for i in dict[key]: 
            print(i)

def maxlen(wordlist =[]):
    dict = {}
    for i in range(len(wordlist)):
        charlist = list(wordlist[i])
        for char in charlist:
            if char in dict.keys() and i not in dict[char]:
                dict[char].append(i)
            else:
                dict[char] = [i]
    
    #printdict(dict)
    
    numlist = list(range(len(wordlist)))
    worddict = {}
    for i in range(len(wordlist)):
        word = numlist
        word.remove(i)
        word = set(word)
        charlist = list(wordlist[i])
        for char in charlist:
            word = word - set(dict[char])
        worddict[wordlist[i]] = list(word)
        
    maxlen = 0
    for word in worddict.keys():
        for i in worddict[word]:
            if(maxlen< (len(word)*len(wordlist[i]))):
                maxlen = (len(word)*len(wordlist[i]))
    
    return maxlen

def main():
    wordlist = ["ZXVNM", "BAZ", "FOO", "BAR", "XTFN", "ABCDEF"]
    print(maxlen(wordlist))
    
main()