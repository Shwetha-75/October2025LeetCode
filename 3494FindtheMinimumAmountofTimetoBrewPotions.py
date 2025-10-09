''''

You are given two integer arrays, skill and mana, of length n and m, respectively.

In a laboratory, n wizards must brew m potions in order. Each potion has a mana capacity mana[j] and must pass through all the wizards sequentially to be brewed properly. The time taken by the ith wizard on the jth potion is timeij = skill[i] * mana[j].

Since the brewing process is delicate, a potion must be passed to the next wizard immediately after the current wizard completes their work. This means the timing must be synchronized so that each wizard begins working on a potion exactly when it arrives. ​

Return the minimum amount of time required for the potions to be brewed properly.

 

Example 1:

Input: skill = [1,5,2,4], mana = [5,1,4,2]

Output: 110

Explanation:

Potion Number	Start time	Wizard 0 done by	Wizard 1 done by	Wizard 2 done by	Wizard 3 done by
0	0	5	30	40	60
1	52	53	58	60	64
2	54	58	78	86	102
3	86	88	98	102	110
As an example for why wizard 0 cannot start working on the 1st potion before time t = 52, consider the case where the wizards started preparing the 1st potion at time t = 50. At time t = 58, wizard 2 is done with the 1st potion, but wizard 3 will still be working on the 0th potion till time t = 60.

Example 2:

Input: skill = [1,1,1], mana = [1,1,1]

Output: 5

Explanation:

Preparation of the 0th potion begins at time t = 0, and is completed by time t = 3.
Preparation of the 1st potion begins at time t = 1, and is completed by time t = 4.
Preparation of the 2nd potion begins at time t = 2, and is completed by time t = 5.
Example 3:

Input: skill = [1,2,3,4], mana = [1,2]

Output: 21

 

Constraints:

n == skill.length
m == mana.length
1 <= n, m <= 5000
1 <= mana[i], skill[i] <= 5000
 


'''

class Solution:
    def minTime(self, skill: list[int], mana: list[int]) -> int:
        cols,rows=len(skill)+1,len(mana)
        matrix=[[0 for _ in range(cols)] for _ in range(rows)]
        for i in range(1,cols):
            matrix[0][i]=matrix[0][i-1]+skill[i-1]*mana[0]
        for i in range(1,rows):
            matrix[i][1]=matrix[i-1][1]+mana[i]*skill[0]
            for j in range(2,cols):
                if matrix[i][j-1]<=matrix[i-1][j]:
                    matrix[i][j]=matrix[i-1][j]+skill[j-1]*mana[i]
                else:
                    matrix[i][j]=matrix[i][j-1]+skill[j-1]*mana[i]
            for j in range(cols-2,-1,-1):
                matrix[i][j]=matrix[i][j+1]-skill[j]*mana[i]
        return matrix[-1][-1]
class Solution:
    def minTime(self, skill: list[int], mana: list[int]) -> int:
        n,m=len(skill),len(mana)
        time=[0]*n
        current_time=0
        for i in range(n):
            if i>0:
                time[i]=time[i-1]+skill[i]*mana[0]
            else:
                time[i]=skill[i]*mana[0]
            current_time=max(time[i],current_time)
        for i in range(1,m):
            time[0]=time[0]+skill[0]*mana[i]
            current_time=time[0]
            
            for j in range(1,n):
                if 1<j<n-1 and time[j-1]<=time[j]:
                    time[j]=time[j]+skill[j]*mana[i]
                elif 0<j and time[j-1]>time[j]:
                    time[j]=time[j-1]+skill[j]*mana[i]    
                else:
                   time[j]=time[j]+skill[j]*mana[i]
                current_time=max(current_time,time[j])
            
            time[n-1]=current_time 
            for j in range(n-2,-1,-1):
                time[j]=time[j+1]-skill[j+1]*mana[i]
        return time[-1]
            
        
        
        pass
class TestApp:
    def testCaseOne(self):
        assert Solution().minTime([1,5,2,4],[5,1,4,2])==110 
    def testCaseTwo(self):
        assert Solution().minTime([1,1,1],[1,1,1])==5 
    def testCaseThree(self):
        assert Solution().minTime([1,2,3,4],[1,2])==21