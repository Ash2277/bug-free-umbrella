n=int(input())
b=n-1
for i in range(n):
    a=0
    for j in range(n):
        print('#',end='') if(a>=b) else print(end=' ')
        a=a+1
    print('')
    b=b-1   