
a, b = map(int, input().split(' '))


def compute_gcd(x, y):

    while(y):
        x, y = y, x % y
    return x


def compute_lcm(x, y):
    lcm = (x*y)//compute_gcd(x, y)
    return lcm


print(compute_lcm(a, b))
