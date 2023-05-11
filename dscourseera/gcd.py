def gcd(a, b):
    rem = 1
    while(rem != 0):
        rem = int(a) % int(b)
        if(rem == 0):
            print(b)
            exit
        else:
            a = b
            b = rem


n, m = input().split(' ')

c = gcd(int(n), int(m))
