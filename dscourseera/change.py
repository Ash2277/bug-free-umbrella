# Uses python3
import sys


def get_change(m):
    # write your code here
    a = m/10
    m = m % 10
    b = m/5
    m = m % 5
    c = m
    return a+b+c


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
