class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        l = []
        t = []
        for i in range(0,len(digits)):
            l.append(str(digits[i]))
        s = "".join(l)
        if s.isdigit():
            s = int(s)+1
        s = str(s)
        for i in range(0,len(s)):
            if s[i].isdigit():
                a = int(s[i])
                t.append(a)
        return t
