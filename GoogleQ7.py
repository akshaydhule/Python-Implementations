'''
Created on 27-Sep-2016
//Name: GoogleQ7.py

//Description: GIven a list of words, and the number of rows and columns, 
return the number of words that can be fit into the rows and columns by 
stringing together each consecutive word. If the next word doesn't fit in the same line, 
it should move to the next line. Find an efficient solution for this. For eg. 

List of words: { "Do", "Run" } 
Number of columns: 9 
Number of rows: 2 

First row: "Do Run Do" (7 letters + 2 spaces fit into 9 columns) 
Second row: "Run Do" (Only 2 words fit into 9 columns)
 
'''
def splitwords(wordlist, row, col):
    worddic = {}
    for i in range(row):
        worddic[i] = str()
    count =0
    rownum=0
    i=0
    while rownum<row:
        if i >= len(wordlist):
            i =0
        if count>= col:
            count =0
            rownum += 1
            if rownum>=row:
                return worddic
        if(count + len(wordlist[i])<=col):
            if count ==0:
                worddic[rownum] += str(wordlist[i])
                count += len(wordlist[i])
                i +=1 
            elif count + len(wordlist[i]) + 1<=col:
                worddic[rownum] = str(worddic[rownum]) + str(' ') + str(wordlist[i])
                count += len(wordlist[i]) + 1
                i +=1
            else:
                rownum += 1
                if rownum>=row:
                    return worddic
                count = 0
                
    
def main():
    wordlist = ['Do','Run']
    worddic = {}
    row =2
    worddic = splitwords(wordlist,2, 9)
    for i in range(row):
        print str(worddic[i])
    
main()