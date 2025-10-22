'''
You are given an integer array nums and two integers k and numOperations.

You must perform an operation numOperations times on nums, where in each operation you:

Select an index i that was not selected in any previous operations.
Add an integer in the range [-k, k] to nums[i].
Return the maximum possible frequency of any element in nums after performing the operations.

 

Example 1:

Input: nums = [1,4,5], k = 1, numOperations = 2

Output: 2

Explanation:

We can achieve a maximum frequency of two by:

Adding 0 to nums[1], after which nums becomes [1, 4, 5].
Adding -1 to nums[2], after which nums becomes [1, 4, 4].
Example 2:

Input: nums = [5,11,20,20], k = 5, numOperations = 1

Output: 2

Explanation:

We can achieve a maximum frequency of two by:

Adding 0 to nums[1].
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109
0 <= k <= 109
0 <= numOperations <= nums.length


'''
import numpy as np

class Solution:
    def maxFrequency(self, nums: list[int], k: int, numOperations: int) -> int:
        n=max(nums)
        count=[0]*(n+1)
        for num in nums:
            count[num]+=1
        prefix_sum=[0]
        for i in range(n+1):
            prefix_sum.append(prefix_sum[-1]+count[i])
        ans=0
        for i in range(n+1):
            right=prefix_sum[min(n+1,i+k+1)]-prefix_sum[i+1]
            left=prefix_sum[i]-prefix_sum[max(0,i-k)]
            curr=count[i]+min(numOperations,left+right)       
            ans=max(ans,curr)
        return ans 
    

from collections import defaultdict
class Solution:
    def maxFrequency(self,nums:list[int],k:int,numOperations:int):
        ans=0 
        freq=defaultdict(int)
        events=[]
        sorted_collections=[]
        for num in nums:
            freq[num]+=1
            start,end=num-k,num+k 
            events.append([start,1])
            events.append([end,-1])
            sorted_collections.append(start)
            sorted_collections.append(end+1)
            sorted_collections.append(num)
        sorted_collections.sort()
        events.sort(key=lambda x:x[0])
        count=eventId=0
        for x in sorted_collections:
            while eventId<len(events) and events[eventId][0]<=x:
                count+=1 if events[eventId][1]==1 else -1 
                eventId+=1
            curr_freq=freq[x]
            curr_max=curr_freq+min(numOperations,max(0,count-curr_freq))
            ans=max(ans,curr_max)
        return ans 
             
Solution().maxFrequency([1,4,5],1,2)            
            
        
        
        
        
class TestApp:
    def testCaseOne(self):
        assert Solution().maxFrequency([1,4,5],1,2)==2
    def testCaseTwo(self):
        assert Solution().maxFrequency( [5,11,20,20],5,1)==2
