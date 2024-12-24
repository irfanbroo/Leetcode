class Solution:
    def reverseString(self, s: List[str]) -> None:
        n = len(s)
        i, j =0, n-1
        while i <= j:
            s[i],s[j] = s[j],s[i]
            i +=1
            j -=1
        return s
        
