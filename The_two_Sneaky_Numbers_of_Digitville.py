class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        hmap = {}
        ans = []
        for num in nums:
            if num in hmap:
                hmap[num]+=1
            else:
                hmap[num]=1
        for num, count in hmap.items(): 
            if count > 1:
                ans.append(num)
        return ans

     ## The .items() method of a dictionary returns a view object that displays a list of the dictionary's key-value tuple pairs.

##Example: For count_map = {'i': 1, 'r': 2}, count_map.items() returns [('i', 1), ('r', 2)]
