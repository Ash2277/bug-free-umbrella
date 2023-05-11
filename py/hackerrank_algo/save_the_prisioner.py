#didnt get
#code took from online
t=int(input())
for i in range(t):
    n,m,s = map(int, input().strip().split(" "))
    print(((s-2+m)%n)+1)