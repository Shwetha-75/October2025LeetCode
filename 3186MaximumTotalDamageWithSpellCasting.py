'''

A magician has various spells.

You are given an array power, where each element represents the damage of a spell. Multiple spells can have the same damage value.

It is a known fact that if a magician decides to cast a spell with a damage of power[i], they cannot cast any spell with a damage of power[i] - 2, power[i] - 1, power[i] + 1, or power[i] + 2.

Each spell can be cast only once.

Return the maximum possible total damage that a magician can cast.

 

Example 1:

Input: power = [1,1,3,4]

Output: 6

Explanation:

The maximum possible damage of 6 is produced by casting spells 0, 1, 3 with damage 1, 1, 4.

Example 2:

Input: power = [7,1,6,6]

Output: 13

Explanation:

The maximum possible damage of 13 is produced by casting spells 1, 2, 3 with damage 1, 6, 6.

 

Constraints:

1 <= power.length <= 105
1 <= power[i] <= 109

'''


from collections import defaultdict
class Solution:
    def maximumTotalDamage(self, power: list[int]) -> int:
        unique_value=defaultdict(int)
        for pow in power:
            unique_value[pow]+=1
        array=list(unique_value.keys())
        n=len(array)
        array.sort()
        temp=[0]*n 
        temp[0]=array[0]*unique_value[array[0]]
        max_res=0
        j=0
        max_value=0
        for i in range(1,n):
            left=array[i]-2 
            while array[j]<left:
                  print(array[j])
                  max_value=max(max_value,temp[j])
                  j+=1            
            temp[i]=array[i]*unique_value[array[i]]+max_value 
            max_res=max(max_res,temp[i])
        return max_res

class TestApp:
    def testCaseOne(self):
        assert Solution().maximumTotalDamage([1,1,3,4])==6 
    def testCaseTwo(self):
        assert Solution().maximumTotalDamage([7,1,6,6])==13
    def testCaseThree(self):
        assert Solution().maximumTotalDamage([8,1,2,4])==13
    def testCaseFour(self):
        assert Solution().maximumTotalDamage([3,1,4,2])==5
    def testCaseFive(self):   
        assert Solution().maximumTotalDamage([5,9,2,10,2,7,10,9,3,8])==31 
