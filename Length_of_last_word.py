class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        j = len(s) - 1
        c = 0
        while j>=0:
            if s[j]!=" ":
                c +=1
            elif s[j] == " " and c > 0:
                break
            j -=1
        return c
