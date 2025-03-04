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
        
        
# Another more simpler version

class Solution:
    def check_l(self, c):
        if c in "a,e,i,o,u":
            return True

    def check(self, word):
        n = len(word)
        if self.check_l(word[0]) and self.check_l(word[-1]):
            return True
        

    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        ## im thinking about creating a prefix array ;)
        s = 0
        arr = []
        n = len(words)
        pr = [0] * (n+1)
        pr[0] = 0
        for i in range(1,n+1):
            pr[i] = pr[i-1] + (1 if self.check(words[i-1]) else 0)

        for i, j in queries:
            s = pr[j+1] - pr[i]
            arr.append(s)


        return arr
