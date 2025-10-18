'''

You are given an integer array nums and an integer k.

You are allowed to perform the following operation on each element of the array at most once:

Add an integer in the range [-k, k] to the element.
Return the maximum possible number of distinct elements in nums after performing the operations.

 

Example 1:

Input: nums = [1,2,2,3,3,4], k = 2

Output: 6

Explanation:

nums changes to [-1, 0, 1, 2, 3, 4] after performing operations on the first four elements.

Example 2:

Input: nums = [4,4,4,4], k = 1

Output: 3

Explanation:

By adding -1 to nums[0] and 1 to nums[1], nums changes to [3, 5, 4, 4].

 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109
0 <= k <= 109

'''

from collections import defaultdict
import heapq

class Solution:
    def maxDistinctElements(self, nums: list[int], k: int) -> int:
        nums.sort()
        hash_map=defaultdict(int)
        
        while nums:
            found=False
            curr=heapq.heappop(nums)
            for i in range(-k,k+1):
                if curr+i not in hash_map:
                    hash_map[curr+i]+=1
                    found=True 
                    break 
            if not found:
                hash_map[curr]+=1
        return len(list(hash_map.keys()))
class Solution:
    def maxDistinctElements(self, nums: list[int], k: int) -> int:
        # nums.sort()
        prev=float('-inf')
        heapq.heapify(nums)
        count=0 
        while nums:
            num=heapq.heappop(nums)
            curr=min(max(num-k,prev+1),num+k)
            if curr>prev:
                count+=1
                prev=curr 
        return count

class TestApp:
    def testCaseOne(self):
        assert Solution().maxDistinctElements([4,4,4,4],1)==3
    def testCaseTwo(self):
        assert Solution().maxDistinctElements([1,2,2,3,3,4],2)==6
    def testCaseThree(self):
        assert Solution().maxDistinctElements([9,5,5],0)==2
        
