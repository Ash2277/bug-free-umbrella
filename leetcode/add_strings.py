class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n1 = 0
        n2 = 0
        final = ""
        for i in num1:
            n1 = n1*10+(ord(i)-48)
        for i in num2:
            n2 = n2*10+(ord(i)-48)
        add = n1+n2
        if add == 0:
            final = "0"
        while(add > 0):
            e = int(add % 10)
            add = add//10
            f = chr(e+48)
            final += f
        return final[::-1]
