#Before the solution, if there was no such condition like negative in our testcase, here is the straightforward approach

#func

def poww(a,n):

    if n == 1:
        return a
    else:
        mid = n//2
        res1 = poww(a,mid)
        fin = res1 * res1
    
    if n%2 == 0:
        return fin
    else:
        return a * fin


#driver code

res = poww(2,3)
print(res)





## Main solution of the problem


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
        
