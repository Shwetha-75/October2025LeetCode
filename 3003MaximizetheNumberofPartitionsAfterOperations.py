''''

You are given a string s and an integer k.

First, you are allowed to change at most one index in s to another lowercase English letter.

After that, do the following partitioning operation until s is empty:

Choose the longest prefix of s containing at most k distinct characters.
Delete the prefix from s and increase the number of partitions by one. The remaining characters (if any) in s maintain their initial order.
Return an integer denoting the maximum number of resulting partitions after the operations by optimally choosing at most one index to change.

 

Example 1:

Input: s = "accca", k = 2

Output: 3

Explanation:

The optimal way is to change s[2] to something other than a and c, for example, b. then it becomes "acbca".

Then we perform the operations:

The longest prefix containing at most 2 distinct characters is "ac", we remove it and s becomes "bca".
Now The longest prefix containing at most 2 distinct characters is "bc", so we remove it and s becomes "a".
Finally, we remove "a" and s becomes empty, so the procedure ends.
Doing the operations, the string is divided into 3 partitions, so the answer is 3.

Example 2:

Input: s = "aabaab", k = 3

Output: 1

Explanation:

Initially s contains 2 distinct characters, so whichever character we change, it will contain at most 3 distinct characters, so the longest prefix with at most 3 distinct characters would always be all of it, therefore the answer is 1.

Example 3:

Input: s = "xxyz", k = 1

Output: 4

Explanation:

The optimal way is to change s[0] or s[1] to something other than characters in s, for example, to change s[0] to w.

Then s becomes "wxyz", which consists of 4 distinct characters, so as k is 1, it will divide into 4 partitions.

 

Constraints:

1 <= s.length <= 104
s consists only of lowercase English letters.
1 <= k <= 26


'''

class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        n,max_partition_count,s=len(s),0,list(s)
        for i in range(n):
            for j in range(26):
                new_char=chr(j+97) 
                if new_char==s[i]:
                    continue 
                temp=s[i]
                s[i]=new_char
                partition=self.partition(s,k)
                s[i]=temp
                max_partition_count=max(max_partition_count,partition if partition else 1)
        max_partition_count=max(max_partition_count,self.partition(s,k))
        return max_partition_count
    def partition(self,string:list[str],k:int)->int:
        partition,count,alphabets,stack,n=1,0,[0]*26,[],len(string)
        for i in range(n):
            if not alphabets[ord(string[i])-97]:
                count+=1
                alphabets[ord(string[i])-97]+=1
            if count>k:
               alphabets=[0]*26
               alphabets[ord(string[i])-97]+=1
               partition+=1   
               count=1 
            stack.append(string[i])
        return partition 
class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        n=len(s)
        left=[[0]*3 for _ in range(n)]
        right=[[0]*3 for _ in range(n)]
        mask=0
        distinct=0
        partitions=0
        for i in range(n-1):
            bit=1<<ord(s[i])-97
            if (bit & mask)==0:
                distinct+=1
                if distinct<=k:
                    mask|=bit 
                else:
                    partitions+=1
                    mask=bit 
                    distinct=1
            left[i+1][0]=partitions
            left[i+1][1]=mask 
            left[i+1][2]=distinct 
        print(left)
        mask=partitions=distinct=0
        for i in range(n-1,0,-1):
            bit=1<<ord(s[i])-97 
            if (bit&mask) ==0:
                distinct+=1
                if distinct<=k:
                    mask|=bit 
                else:
                    partitions+=1
                    mask=bit 
                    distinct=1
            right[i-1][0]=partitions
            right[i-1][1]=mask 
            right[i-1][2]=distinct
        max_count=0 
        for i in range(n):
            total=left[i][0]+right[i][0]+2
            combinationsMask=left[i][1]|right[i][1]
            combinationsDistinct=int.bit_count(combinationsMask)
            if left[i][2]==k and right[i][2]==k and combinationsDistinct<26:
                total+=1
            elif min(combinationsDistinct+1,26)<=k:
                total-=1
            max_count=max(max_count,total)
        print(max_count)
        return max_count                              
        
Solution().maxPartitionsAfterOperations("accca",2)       

class TestApp:
    def testCaseOne(self):
        assert Solution().maxPartitionsAfterOperations("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxzabcdefghijklmnopqrstuvwxy",25)
    def testCaseTwo(self):
        assert Solution().maxPartitionsAfterOperations("aabaab",3)==1
    def testCaseThree(self):
        assert Solution().maxPartitionsAfterOperations("accca",2)==3
    def testCaseFour(self):
        assert Solution().maxPartitionsAfterOperations("xxyz",1)==4
    def testCaseFive(self):
        assert Solution().maxPartitionsAfterOperations("baacccb",1)==6
    