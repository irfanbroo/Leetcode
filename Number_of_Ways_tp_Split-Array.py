## This code works but gives a TLE error at the 92/102 testcases.
class Solution:
    def add(self,arr):
        return sum(arr)
    def waysToSplitArray(self, nums: List[int]) -> int:
        n=len(nums)
        c=0
        for i in range(1,n):
            larr=nums[:i]
            rarr=nums[i:]
            
            slarr=self.add(larr)
            srarr=self.add(rarr)
            if slarr >= srarr:
                c+=1
        return c
## In order to fix that, we are using prefix sum to solve
class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        c=0
        n=len(nums)
        parr=[0] * (n+1)

        for i in range(1,n+1):
            parr[i] = parr[i-1] + nums[i-1]
        

        total = parr[-1]
        for i in range(1,n):
            lsum=parr[i]
            rsum=total - lsum

            if lsum >=rsum:
                c+=1
        return c
