class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        ans=[]
        for x in range(1,2*n+1):
            if x%2==0 and x%n==0:
                ans.append(x)

        return min(ans)