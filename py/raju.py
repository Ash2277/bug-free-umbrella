def main():
    n=int(input())
    s=input()
    sum1=0
    sum2=0
    a=s.split(' ')
    if(n<10000):
        b=[int(x) for x in a]
        for i in range(0,len(b)):
            sum1+=b[i]    
        for j in range(0,n+1):
            sum2+=j
        if(sum2==sum1):
            print("YES")
        else:
            print("NO")
    else:
        return 0
main()