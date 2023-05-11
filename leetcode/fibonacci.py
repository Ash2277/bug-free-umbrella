class Solution:
    def fib(self, n: int) -> int:
        lst = [0, 1]
        # a=0
        # b=1
        for i in range(1, n):
            s = lst[i-1]+lst[i]
            lst.append(s)
            # a+=1
            # b+=1
        return lst[n]
