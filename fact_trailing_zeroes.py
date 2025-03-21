## Ok so in this code we are passing only 474/500
## TLE and the rest of the approach needs optimisation in order to compute the fact 

class Solution:
    def find(self,n):
        if n <3:
            return n       
        
        fact = [1] * (n+1)
        fact[1] = 1
        fact[2] = 2
        for i in range(3,n+1):
            fact[i] = i * fact[i-1]
        return fact[n]
    
    
    
    
    def trailingZeroes(self, n: int) -> int:
        if n == 0:
            return 0
        
        
        ans = self.find(n)
        c=0
        x =  ans
        while x!=0:
            if x%10 == 0:
                c+=1
                x = x//10
            else:
                break

        return c
