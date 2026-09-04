class Solution:
    def isPalindrome(self, x: int) -> bool:
       rev=0
       temp=x
       while temp>0:
        r=temp%10
        temp//=10
        rev=rev*10+r
       if rev==x:
        return True
       else:
        return False    
        
