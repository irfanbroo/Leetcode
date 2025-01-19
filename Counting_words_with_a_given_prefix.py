class Solution:
    def is_pref(self,word1,word2):
        m = len(word1)
        n = len(word2)
        if m > n:
            return False
        for i in range(m):
            if word1[i]!=word2[i]:
                return False
        return True
    
    
    def prefixCount(self, words: List[str], pref: str) -> int:
        n = len(words)
        c=0
        for i in range(n):
            if self.is_pref(pref,words[i]):
                c+=1
        return c
