class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        x = len(strs) 
        strs.sort()
        str = ""
        first = strs[0]
        last = strs[-1]
        for i in range(len(first)):
            if first[i] == last[i]:
                str += first[i]
            else:
                break
        return str
