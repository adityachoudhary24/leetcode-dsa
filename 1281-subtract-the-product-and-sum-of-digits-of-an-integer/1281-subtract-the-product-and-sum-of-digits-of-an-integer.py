class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sums=0
        product=1
        temp=n
        while temp>0:
            r=temp%10
            temp//=10
            sums+=r
            product*=r
        return product - sums    