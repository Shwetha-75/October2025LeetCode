'''

There are numBottles water bottles that are initially full of water. 
You can exchange numExchange empty water bottles from the market 
with one full water bottle.

The operation of drinking a full water bottle turns it into an empty bottle.

Given the two integers numBottles and numExchange, return the 
maximum number of water bottles you can drink.

 

Example 1:


Input: numBottles = 9, numExchange = 3
Output: 13
Explanation: You can exchange 3 empty bottles to get 1 full water bottle.
Number of water bottles you can drink: 9 + 3 + 1 = 13.
Example 2:


Input: numBottles = 15, numExchange = 4
Output: 19
Explanation: You can exchange 4 empty bottles to get 1 full water bottle. 
Number of water bottles you can drink: 15 + 3 + 1 = 19.
 

Constraints:

1 <= numBottles <= 100
2 <= numExchange <= 100



'''

class Solution:
    def numWaterBottles(self, b: int, n: int) -> int:
        if b<n: return b
        count=b 
        while b>=n:
            count+=b//n 
            b=b//n+b%n 
        return count
class Solution:
    def numWaterBottles(self, b: int, n: int) -> int:
        return int(b+(b-1)/(n-1))
    
class TestApp:  
    def testCaseOne(self):
        assert Solution().numWaterBottles(15,4)==19 
    def testCaseTwo(self):
        assert Solution().numWaterBottles(9,3)==13
    def testCaseThree(self):
        assert Solution().numWaterBottles(2,3)==2
    def testCaseFour(self):
        assert Solution().numWaterBottles(6,5)==7