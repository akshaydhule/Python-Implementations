'''
WAP to take one element from each of the array add it to the target sum. 
Print all those three-element combinations. 

/* 
A = [1, 2, 3, 3] 
B = [2, 3, 3, 4] 
C = [1, 2, 2, 2] 
target = 7 
*/ 

Result: 
[[1, 2, 4], [1, 3, 3], [1, 3, 3], [1, 3, 3], [1, 3, 3], [1, 4, 2], 
[2, 2, 3], [2, 2, 3], [2, 3, 2], [2, 3, 2], [3, 2, 2], [3, 2, 2]]
'''

def nocomb(a,b,c):
    i = len(a) - 1
    j = len(b) - 1
    k = len(c) - 1
    output = []
    nocomb1(a,b,c,i,j,k,output)
    for i in output:
        print(i)
    
def nocomb1(a,b,c,i,j,k, output):
    if(i<0 or j<0 or k<0):
        return
    else:
        if a[i] + b[j] + c [k] == 7:
            output.append([a[i], b[j], c[k]])
        nocomb1(a,b,c,i-1,j,k,output)
        nocomb1(a,b,c,i,j-1,k,output)
        nocomb1(a,b,c,i,j,k-1,output)

def main():
    a = [1,2,3,4]
    b = [2,3,3,4]
    c = [1,2,2,2]
    nocomb(a,b,c)
    
main()