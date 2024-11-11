class Solution(object):
    def myPow(self, x, n):
        if n==0:
            return 1
        elif n==1:
            return x
        elif n<0:
            x = 1/x
            n = -n
            return self.myPow(x,n)
        else:
            mid = n//2
            result = self.myPow(x,mid)
            final_result = result * result
        if n%2==0:
            return final_result
        else:
            return x * final_result
        
