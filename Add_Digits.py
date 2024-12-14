class Solution:
    def addDigits(self, num: int) -> int:
        s = 0
        c = 0
        if num <=9:
            return num
        else:
            while num!=0:
                x = num%10
                s = s + x
                num = num//10
            return self.addDigits(s)
