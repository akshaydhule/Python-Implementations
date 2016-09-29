import filecmp
import sys
global list1 
list1 = []

def swap(char_list, i,j):
    temp = char_list[i]
    char_list[i]=char_list[j]
    char_list[j]=temp

def anagram(char_list, front, rear):
    if(front==rear):
        str1 = ''.join(char_list)
        list1.append(str1)
    else:
        for i in xrange(front, rear+1):
            swap(char_list, front, i)
            anagram(char_list,front+1, rear)
            swap(char_list, i, front)
        
        
    
#main function
ip = raw_input('Enter the string?')
char_list = list(ip)
size = len(ip)
anagram(char_list,0, size-1)
list1.sort()
size = len(list1)
f = open('output.txt','a')
for i in xrange(0,size):
    f.write(list1[i])
    f.write('\n')
f.close()
