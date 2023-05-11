# Import time module
import time

# record start time
start = time.time()

# define a sample code segment
w = int(input())
if w == 2 or w % 2 == 1:
    print('NO')
else:
    print('YES')
# record end time
end = time.time()

# print the difference between start
# and end time in milli. secs
print("The time of execution of above program is :",
      (end-start) * 10**3, "ms")
