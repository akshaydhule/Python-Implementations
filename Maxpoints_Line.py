'''
Given n points on a 2D plane, find the maximum 
number of points that lie on the same straight line.
'''

#from collections import Point
from __future__ import division
import sys

class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

#given two points find 
#1. slope of the line
#2. y-intercept

class line(object):
    def __init__(self, a, b):
        if (a.x-b.x) != 0:
            self.slope = (a.y-b.y)/((a.x-b.x)*1.0)
            self.yintercept = a.y - (self.slope) * a.x
            if self.slope == 0:
                self.xintercept = sys.maxint
            else:
                self.xintercept = - (self.yintercept)/(self.slope * 1.0)
                        
            
        else:  
            self.slope = sys.maxint
            self.yintercept = sys.maxint
            self.xintercept = a.x
                
            
class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        
        visited: list of points already visited
        line to list of points dictionary
        for every point in list
        1. add each point as reference point to line in dict
        2. iterate to remaining points if it matches the slope
        for every line in the dictionary check if slope matches 
        if yes : add to the list
        
        """
        if len(points) <= 1:
            return len(points) 
        linedict = {}
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                curr = line(points[i], points[j])
                tup = (curr.slope, curr.xintercept, curr.yintercept)
                if tup in linedict.keys():
                    if j not in set(linedict[tup]): 
                        linedict[tup].append(j)
                    if i not in set(linedict[tup]): 
                        linedict[tup].append(i)
                else:
                    linedict[tup] = [i, j]
    
        maxline = 0
        for key in linedict.keys():
            if len(linedict[key]) > maxline:
                print key
                maxline = len(linedict[key])
    
        return maxline


     
def main():
    points = []
    l = [[40,-23],[9,138],[429,115],[50,-17],[-3,80],[-10,33],[5,-21],[-3,80],[-6,-65],[-18,26],[-6,-65],[5,72],[0,77],[-9,86],[10,-2],[-8,85],[21,130],[18,-6],[-18,26],[-1,-15],[10,-2],[8,69],[-4,63],[0,3],[-4,40],[-7,84],[-8,7],[30,154],[16,-5],[6,90],[18,-6],[5,77],[-4,77],[7,-13],[-1,-45],[16,-5],[-9,86],[-16,11],[-7,84],[1,76],[3,77],[10,67],[1,-37],[-10,-81],[4,-11],[-20,13],[-10,77],[6,-17],[-27,2],[-10,-81],[10,-1],[-9,1],[-8,43],[2,2],[2,-21],[3,82],[8,-1],[10,-1],[-9,1],[-12,42],[16,-5],[-5,-61],[20,-7],[9,-35],[10,6],[12,106],[5,-21],[-5,82],[6,71],[-15,34],[-10,87],[-14,-12],[12,106],[-5,82],[-46,-45],[-4,63],[16,-5],[4,1],[-3,-53],[0,-17],[9,98],[-18,26],[-9,86],[2,77],[-2,-49],[1,76],[-3,-38],[-8,7],[-17,-37],[5,72],[10,-37],[-4,-57],[-3,-53],[3,74],[-3,-11],[-8,7],[1,88],[-12,42],[1,-37],[2,77],[-6,77],[5,72],[-4,-57],[-18,-33],[-12,42],[-9,86],[2,77],[-8,77],[-3,77],[9,-42],[16,41],[-29,-37],[0,-41],[-21,18],[-27,-34],[0,77],[3,74],[-7,-69],[-21,18],[27,146],[-20,13],[21,130],[-6,-65],[14,-4],[0,3],[9,-5],[6,-29],[-2,73],[-1,-15],[1,76],[-4,77],[6,-29]]
    for i in l:
        points.append(Point(i[0],i[1]))
    '''
    points.append(Point(1,2))
    points.append(Point(2,2))
    points.append(Point(3,2))
    points.append(Point(2,3))
    
    points.append(Point(1,1))
    points.append(Point(1,1))
    points.append(Point(2,2))
    '''
    s = Solution()
    print(s.maxPoints(points))
    
main()
            
        