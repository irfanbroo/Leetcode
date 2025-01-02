class Solution:
    def is_vow(self,c):
        return c in 'a,e,i,o,u'
    def is_str_vow(self,s):
        return self.is_vow(s[0]) and self.is_vow(s[-1])
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(words)
        pr=[0] * (n+1)
        
        for i in range(n):
            pr[i+1] = pr[i] + (1 if self.is_str_vow(words[i]) else 0)
        
        arr=[]
        for l, r in queries:
            arr.append(pr[r+1] - pr[l])
        return arr
        
        
