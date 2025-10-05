'''
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

 

Example 1:


Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
[0,4]: [0,4] -> Pacific Ocean 
       [0,4] -> Atlantic Ocean
[1,3]: [1,3] -> [0,3] -> Pacific Ocean 
       [1,3] -> [1,4] -> Atlantic Ocean
[1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean 
       [1,4] -> Atlantic Ocean
[2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean 
       [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
[3,0]: [3,0] -> Pacific Ocean 
       [3,0] -> [4,0] -> Atlantic Ocean
[3,1]: [3,1] -> [3,0] -> Pacific Ocean 
       [3,1] -> [4,1] -> Atlantic Ocean
[4,0]: [4,0] -> Pacific Ocean 
       [4,0] -> Atlantic Ocean
Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.
Example 2:

Input: heights = [[1]]
Output: [[0,0]]
Explanation: The water can flow from the only cell to the Pacific and Atlantic oceans.
 

Constraints:

m == heights.length
n == heights[r].length
1 <= m, n <= 200
0 <= heights[r][c] <= 105

'''
 
# Brute Force - BFS
class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        m,n=len(heights),len(heights[0])
        res=[]
        for row in range(m):
            for col in range(n):
                pacific=atlantic=False 
                if (row==0 and col==n-1) or (row==m-1 and col==0):
                    res.append([row,col])
                    continue
                # for atlantic always if it is at last row or last column it  can easily reach atlantic 
                if col==n-1 or row==m-1:
                    atlantic=True 
                
                else:
                    visited=[[False for _ in range(n)] for _ in range(m)]
                    atlantic=self.checkAtlanticOcean(m,n,row,col,heights[row][col],visited,heights)
                
                if row==0 or col==0:
                    pacific=True 
                else:
                    visited=[[False for _ in range(n)] for _ in range(m)]
                    pacific=self.checkPacificOcean(m,n,row,col,heights[row][col],visited,heights)
                    
                if atlantic and pacific:
                    res.append([row,col])
        return res
    def checkAtlanticOcean(self,m:int,n:int,row:int,col:int,value:int,visited:list[list[bool]],matrix:list[list[int]]):
        if visited[row][col]: return False 
        if row>=m-1 or col>=n-1: return True 
        visited[row][col]=True 
        res=False 
        if row+1<m and matrix[row+1][col]<=value:
            res=res or self.checkAtlanticOcean(m,n,row+1,col,matrix[row+1][col],visited,matrix)
        if col+1<n and matrix[row][col+1]<=value:
            res=res or self.checkAtlanticOcean(m,n,row,col+1,matrix[row][col+1],visited,matrix)
        if col-1>=0 and matrix[row][col-1]<=value:
            res=res or self.checkAtlanticOcean(m,n,row,col-1,matrix[row][col-1],visited,matrix)
        if row-1>=0 and matrix[row-1][col]<=value:
            res=res or self.checkAtlanticOcean(m,n,row-1,col,matrix[row-1][col],visited,matrix)
        return res  
    def checkPacificOcean(self,m:int,n:int,row:int,col:int,value:int,visited:list[list[bool]],matrix:list[list[int]])->bool:
        if visited[row][col]: return False 
        if row<=0 or col<=0: return True 
        visited[row][col]=True 
        res=False 
        
        if row-1>=0 and matrix[row-1][col]<=value:
            res=res or self.checkPacificOcean(m,n,row-1,col,matrix[row-1][col],visited,matrix)
        if col-1>=0 and matrix[row][col-1]<=value:
            res=res or self.checkPacificOcean(m,n,row,col-1,matrix[row][col-1],visited,matrix)
        if col+1<n and matrix[row][col+1]<=value:

            res=res or self.checkPacificOcean(m,n,row,col+1,matrix[row][col+1],visited,matrix)
        if row+1<m and matrix[row+1][col]<=value:
            res=res or self.checkPacificOcean(m,n,row+1,col,matrix[row+1][col],visited,matrix)
        return res
# DFS

class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        m,n=len(heights),len(heights[0])
        pacific_ocean=[[False for _ in range(n)] for _ in range(m)]
        atlantic_ocean=[[False for _ in range(n)] for _ in range(m)]
        for row in range(m):
            self.findPathForOcean(row,0,pacific_ocean,heights)
            self.findPathForOcean(row,n-1,atlantic_ocean,heights)
        for col in range(n):
            self.findPathForOcean(0,col,pacific_ocean,heights)
            self.findPathForOcean(m-1,col,atlantic_ocean,heights)
        res=[]
        for i in range(m):
            for j in range(n):
                if pacific_ocean[i][j] and atlantic_ocean[i][j]:
                    res.append([i,j])
        return res 
    def findPathForOcean(self,row:int,col:int,visited:list[list[bool]],matrix:list[list[int]])->bool:
        if visited[row][col]:
            return
        visited[row][col]=True 
        for r,c in [[-1,0],[1,0],[0,-1],[0,1]]:
            new_row,new_col=r+row,c+col 
            if 0<=new_row<len(matrix) and 0<=new_col<len(matrix[0]) and matrix[new_row][new_col]>=matrix[row][col]:
                self.findPathForOcean(new_row,new_col,visited,matrix) 
 
class TestApp:
    def testCaseOne(self):
        assert Solution().pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]])==[[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]  
    def testCaseTwo(self):
        assert Solution().pacificAtlantic([[1]])==[[0,0]]
    def testCaseThree(self):
        assert Solution().pacificAtlantic([[10,10,10],[10,1,10],[10,10,10]])==[[0,0],[0,1],[0,2],[1,0],[1,2],[2,0],[2,1],[2,2]]
    def testCaseFour(self):
        assert Solution().pacificAtlantic([[1,2,3],[8,9,4],[7,6,5]])==[[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]] 