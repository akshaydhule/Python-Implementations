import sys

'''
Functions
main: reads line by line and populates chainMap
chainCheck: checks if chain is good or bad
input : BEGIN:a;a-b;b-c;d-a;d-END;c-d;
output : GOOD
input : BEGIN-a;a-b;b-c;d-a;
output : BAD

'''
import sys

#checks for GOOD or BAD check
def chainCheck(chainMap):
    start = "BEGIN"
    end  = "END"
    visited = set()
    while(start != end):
        #check if loop
        if start not in visited:
            visited.add(start)
            #check if key is available
            if start in chainMap.keys():
                start = chainMap[start]
            else:
                return "BAD"
        else:
            return "BAD"
    #check if all nodes are covered
    if len(visited) != len(chainMap):
        return "BAD"
    else:
        return "GOOD"
        
#main function to read lines and populate map[source:destination]

def main():
    chainMap = {}
    for line in sys.stdin:
        line = line.strip()
        chains = line.split(';')
        print chains
        for chain in chains:
            pair = chain.split('-')
            chainMap[pair[0]] = pair[1]
        print(chainCheck(chainMap))

    
    
#main function call

main()