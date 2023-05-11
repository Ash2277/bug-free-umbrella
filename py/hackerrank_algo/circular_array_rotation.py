#my code doesnt work for all cases
n,k,q=input().split(' ')
a=input().split(' ')
for i in range(int(k)):
    c=[]
    c=[a[len(a)-1]]+a[0:len(a)-1]
    a=c
for i in range(int(q)):
    d=int(input()) 
    print(a[d])
#online
# N,K,Q = input().strip().split()
# arr = input().strip().split()

# N = int(N)
# K = int(K)
# Q = int(Q)

# if K >= N:
#     K %= N
    
# if K != 0:
#     arr = arr[-K:] + arr[:-K]

# for i in range(Q):
#     print(arr[int(input())])