class Solution:
    
    def myAtoi(self, s: str) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -(2**31)
        s = s.strip(" ")
        if not s:
            return 0

        sign = 1
        i = 0
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i +=1 
        
        integer = 0
        while i < len(s):
            c = s[i]
            if not c.isdigit():
                break
            integer = integer * 10 + int(c)
            i += 1
        
        integer = sign * integer
        if integer > INT_MAX:
            return INT_MAX
        if integer < INT_MIN:
            return INT_MIN
        return integer 
        
