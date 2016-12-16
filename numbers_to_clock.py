'''
Given 4 integers, return largest possible and valid time in HH:MM format.

example:
input: 2,4,0,0
output: 20:40

input: 1,9,8,9
output: NOT POSSIBLE
'''

import numbers
import itertools
import copy

def solution(A,B,C,D):
    num =[]
    num.append(A)
    num.append(B)
    num.append(C)
    num.append(D)
    keywords = []
    #generate all combinations
    for i in itertools.permutations(num, r =2 ):
        s =""
        for j in i:
            s = s+str(j)
        keywords.append(s)

    hour = -1
    minute = -1
    #valid for hour and minutes
    validHours = []
    validMinutes = []
    for i in keywords:
        if int(i)<24:
            validHours.append(i)
        if int(i)<60:
            validMinutes.append(i)

    maxHour = -1
    maxMinute = -1
    
    #loop through all possible combinations
    for hour in validHours:
        for minute in validMinutes:
            nums = copy.copy(num)
            keyword = copy.copy(keywords)
            hour1 = int(copy.copy(hour))
            count=0
            rem = -1
            while(count<2):
                rem = int(hour1)%10
                nums.remove(rem)
                hour1 = hour1/10
                count += 1
            
            if int(hour)<24 and int(minute) < 60:
                if hour in keyword:
                    newkeyword = []
                    for i in itertools.permutations(nums, r =2 ):
                        s =""
                        for j in i:
                            s = s+str(j)
                        newkeyword.append(s)
                        
                    if minute in newkeyword:
                        if(int(hour)>int(maxHour)) or (hour == maxHour and int(minute)>int(maxMinute)):
                            maxHour = hour 
                            maxMinute = minute
                            
    if maxHour is not -1:
        return (maxHour) + ':' + (maxMinute)
    else:
        return 'NOT POSSIBLE'
    

def main():
    print(solution(2,4,0,0))
    
main()