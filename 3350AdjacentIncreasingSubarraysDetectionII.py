'''

Given an array nums of n integers, your task is to find the maximum value of k for which there exist two adjacent subarrays of length k each, such that both subarrays are strictly increasing. Specifically, check if there are two subarrays of length k starting at indices a and b (a < b), where:

Both subarrays nums[a..a + k - 1] and nums[b..b + k - 1] are strictly increasing.
The subarrays must be adjacent, meaning b = a + k.
Return the maximum possible value of k.

A subarray is a contiguous non-empty sequence of elements within an array.


Example 1:

Input: nums = [2,5,7,8,9,2,3,4,3,1]

Output: 3

Explanation:

The subarray starting at index 2 is [7, 8, 9], which is strictly increasing.
The subarray starting at index 5 is [2, 3, 4], which is also strictly increasing.
These two subarrays are adjacent, and 3 is the maximum possible value of k for which two such adjacent strictly increasing subarrays exist.
Example 2:

Input: nums = [1,2,3,4,4,4,4,5,6,7]

Output: 2

Explanation:

The subarray starting at index 0 is [1, 2], which is strictly increasing.
The subarray starting at index 2 is [3, 4], which is also strictly increasing.
These two subarrays are adjacent, and 2 is the maximum possible value of k for which two such adjacent strictly increasing subarrays exist.
 

Constraints:

2 <= nums.length <= 2 * 105
-109 <= nums[i] <= 109

'''

class Solution:
    def maxIncreasingSubarrays(self, nums: list[int]) -> int:
        boundaries={}
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if nums[j-1]<nums[j]:
                    if i not in boundaries:
                        boundaries[i]=[[j-i+1,i,j]]
                    else:
                        boundaries[i].append([j-i+1,i,j])
                else:
                    break
        k=0
        for boundary in boundaries:
            for item in boundaries[boundary]:
                if item[2]+1 in boundaries:
                    for ele in boundaries[item[2]+1]:
                        if ele[0]==item[0]:
                            k=max(k,ele[0])
        return k 
class Solution:
    def maxIncreasingSubarrays(self, nums: list[int]) -> int:
        count,prev_count,n=1,0,len(nums)
        ans=0
        for i in range(1,n):
            if nums[i]>nums[i-1]:
                count+=1
            else:
                prev_count,count=count,1 
            ans=max(ans,min(prev_count,count),count//2)
        return ans
class TestApp:
    def testCaseOne(self):
        assert Solution().maxIncreasingSubarrays([2,5,7,8,9,2,2,4,3,1])==2
    def testCaseTwo(self):
        assert Solution().maxIncreasingSubarrays([1,2,3,4,4,4,4,5,6,7])==2
