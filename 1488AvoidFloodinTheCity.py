'''

Your country has an infinite number of lakes. Initially, all the lakes are empty, but when it rains over the nth lake, the nth lake becomes full of water. If it rains over a lake that is full of water, there will be a flood. Your goal is to avoid floods in any lake.

Given an integer array rains where:

rains[i] > 0 means there will be rains over the rains[i] lake.
rains[i] == 0 means there are no rains this day and you can choose one lake this day and dry it.
Return an array ans where:

ans.length == rains.length
ans[i] == -1 if rains[i] > 0.
ans[i] is the lake you choose to dry in the ith day if rains[i] == 0.
If there are multiple valid answers return any of them. If it is impossible to avoid flood return an empty array.

Notice that if you chose to dry a full lake, it becomes empty, but if you chose to dry an empty lake, nothing changes.

 

Example 1:

Input: rains = [1,2,3,4]
Output: [-1,-1,-1,-1]
Explanation: After the first day full lakes are [1]
After the second day full lakes are [1,2]
After the third day full lakes are [1,2,3]
After the fourth day full lakes are [1,2,3,4]
There's no day to dry any lake and there is no flood in any lake.
Example 2:

Input: rains = [1,2,0,0,2,1]
Output: [-1,-1,2,1,-1,-1]
Explanation: After the first day full lakes are [1]
After the second day full lakes are [1,2]
After the third day, we dry lake 2. Full lakes are [1]
After the fourth day, we dry lake 1. There is no full lakes.
After the fifth day, full lakes are [2].
After the sixth day, full lakes are [1,2].
It is easy that this scenario is flood-free. [-1,-1,1,2,-1,-1] is another acceptable scenario.
Example 3:

Input: rains = [1,2,0,1,2]
Output: []
Explanation: After the second day, full lakes are  [1,2]. We have to dry one lake in the third day.
After that, it will rain over lakes [1,2]. It's easy to prove that no matter which lake you choose to dry in the 3rd day, the other one will flood.
 

Constraints:

1 <= rains.length <= 105
0 <= rains[i] <= 109

'''

# Brute Force approach - O(n*n)

from collections import deque

class Solution:
    def avoidFlood(self, rains: list[int]) -> list[int]:
        n=len(rains)
        result=[1]*n 
        dry_days=[False]*n
        hash_map={}
        for i in range(n):
            hash_map[rains[i]]=-1
        for i in range(n):
            if rains[i]==0:
                dry_days[i]=True 
                continue 
            else:
                if hash_map[rains[i]]==-1:
                    hash_map[rains[i]]=i 
                    result[i]=-1
                else:
                    prev=hash_map[rains[i]]
                    dryDay=-1
                    for j in range(prev+1,i):
                        if dry_days[j]:
                            dryDay=j 
                            break 
                    if dryDay==-1:
                        return []
                    result[dryDay]=rains[i]
                    dry_days[dryDay]=False 
                    hash_map[rains[i]]=i
        return result
    
    
# optimized approach at O(nlogn) 

from sortedcontainers import SortedList

class Solution:
    def avoidFlood(self, rains: list[int]) -> list[int]:
        n=len(rains)
        result=[1]*n
        sorted_list=SortedList()
        map={}
        for i in range(n):
            if rains[i]!=0:
                map[rains[i]]=-1
                
        for i in range(n):
            if rains[i]==0:
                sorted_list.add(i)
                continue 
            else:
                if map[rains[i]]==-1:
                    result[i]=-1
                else:
                    day=sorted_list.bisect(map[rains[i]])
                    if day==len(sorted_list): return []
                    result[sorted_list[day]]=rains[i]
                    result[i]=-1 
                    sorted_list.discard(sorted_list[day])
                map[rains[i]]=i
        return result
                    

class TestApp:
    def testCaseOne(self):
        assert Solution().avoidFlood([1,2,3,4])==[-1,-1,-1,-1]
    def testCaseTwo(self):
        assert Solution().avoidFlood([1,2,0,1,2])==[]
    def testCaseThree(self):
        assert Solution().avoidFlood([1,2,0,0,2,1])==[-1,-1,2,1,-1,-1]
    def testCaseFour(self):
        assert Solution().avoidFlood([69,0,0,0,69])==[-1,69,1,1,-1]
    def testCaseFive(self):
        assert Solution().avoidFlood([2,3,0,0,3,1,0,1,0,2,2])==[]
    def testCaseSix(self):
        assert Solution().avoidFlood([10,20,20])==[]
    def testCaseSeven(self):
        assert Solution().avoidFlood([1,2,0,2,3,0,1])==[-1,-1,2,-1,-1,1,-1]
