#naive method
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==1:
            lst=[[1]]
            return lst
        else:
            lst=[[1],[1,1]]
            a=[1,1]
            # c=[1,1]
            for i in range(2,numRows):
                b=1
                a=[1,1]
                c=0
                d=1
                for j in range(0,len(lst[i-2])):
                    a.insert(b,lst[i-1][c]+lst[i-1][d])
                    b+=1
                    c+=1
                    d+=1
                lst.append(a)
                c=a
            return lst
#reduced space
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==1:
            lst=[[1]]
            return lst
        else:
            lst=[[1],[1,1]]
            a=[1,1]
            for i in range(2,numRows):
                a=[1,1]
                for j in range(1,len(lst[i-2])+1):
                    a.insert(j,lst[i-1][j-1]+lst[i-1][j])
                lst.append(a)
            return lst
#best method
from math import factorial
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        li=[]
        for i in range(numRows):
            li1=[]
            for j in range(i+1):
                li1.append(factorial(i)//(factorial(j)*factorial(i-j)))
            li.append(li1)
        return li