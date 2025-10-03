'''

Given an m x n integer matrix heightMap representing the height of 
each unit cell in a 2D elevation map, return the volume of water it 
can trap after raining.

 

Example 1:


Input: heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
Output: 4
Explanation: After the rain, water is trapped between the blocks.
We have two small ponds 1 and 3 units trapped.
The total volume of water trapped is 4.
Example 2:


Input: heightMap = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
Output: 10
 

Constraints:

m == heightMap.length
n == heightMap[i].length
1 <= m, n <= 200
0 <= heightMap[i][j] <= 2 * 104


'''

import heapq

class Solution:
    def trapRainWater(self, heightMap: list[list[int]]) -> int:
        min_heap=[]
        trapped=0
        rows,cols=len(heightMap),len(heightMap[0])
        if rows<=2 or cols<=2: return trapped
        visited=[[False for _ in range(cols)] for _ in range(rows)]
        for i in range(rows):
            visited[i][0]=visited[i][-1]=True 
            min_heap.append([heightMap[i][0],i,0])
            min_heap.append([heightMap[i][-1],i,cols-1])
        for j in range(cols):
            visited[0][j]=visited[-1][j]=True
            min_heap.append([heightMap[0][j],0,j])
            min_heap.append([heightMap[-1][j],rows-1,j])
        heapq.heapify(min_heap)
        level=0
        while min_heap:
            value,row,col=heapq.heappop(min_heap)
            level=max(level,value)
            top=bottom=left=right=-1
            if row>0:
                top=heightMap[row-1][col]
                if not visited[row-1][col]:
                    heapq.heappush(min_heap,[heightMap[row-1][col],row-1,col])
                    visited[row-1][col]=True 
            if row+1<rows:
               bottom=heightMap[row+1][col]
               if not visited[row+1][col]:
                   heapq.heappush(min_heap,[heightMap[row+1][col],row+1,col])
                   visited[row+1][col]=True 
                   
            if col>0:
                left=heightMap[row][col-1]
                if not visited[row][col-1]:
                    heapq.heappush(min_heap,[heightMap[row][col-1],row,col-1])
                    visited[row][col-1]=True 
            if col+1<cols:
                right=heightMap[row][col+1]
                if not visited[row][col+1]:
                    heapq.heappush(min_heap,[heightMap[row][col+1],row,col+1])
                    visited[row][col+1]=True 
            if top!=-1 and bottom!=-1 and left!=-1 and right!=-1 and value<level:
                trapped+=level-value
        return trapped 
class TestApp:
    def testCaseOne(self):
        assert Solution().trapRainWater([[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]])==4 
    def testCaseTwo(self):
        assert Solution().trapRainWater([[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]])==10
    def testCaseThree(self):
        assert Solution().trapRainWater([[5,5,5,1],[5,1,1,5],[5,1,5,5],[5,2,5,8]])==3            
            
