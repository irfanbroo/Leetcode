class Solution:
    def isPalindrome(self, x: int) -> bool:
        s=0
        if x==0:
            return True
        if x<0:
            return False
        temp=x
        while x>0:
            d=x%10
            s=s*10+d
            x=x//10
        if temp == s:
            return True
        else:
            return False
