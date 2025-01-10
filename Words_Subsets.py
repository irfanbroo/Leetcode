from collections import Counter
class Solution:

    def counter(self,word):
        return Counter(word)
    
    
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        b_max = Counter()
        for b in words2:
            b_freq = self.counter(b)
            for char in b_freq:
                b_max[char] = max(b_max[char], b_freq[char])
        res = []
        for a in words1:
            a_freq = self.counter(a)
            flag = True
            for char in b_max:
                if b_max[char] > a_freq[char]:
                    flag = False
                    break
            if flag:
                res.append(a)
        return res
                    
            

            
        
        
