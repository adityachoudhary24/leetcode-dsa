class Solution:
    def countElements(self, nums: list[int]) -> int:
        ans=[]
        maxi=max(nums)
        mini=min(nums)
        count=0
        for i in nums:
            if i>mini and i<maxi:
                ans.append(str(i))
        n=len(ans)
        return n        