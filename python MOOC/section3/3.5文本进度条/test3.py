import time
import math
scale = 50
print("执行开始".center(scale//2, "-"))
start = time.perf_counter()
for i in range(scale+1):
    i = i + int((1-math.sin(i*math.pi*2 + math.pi/2)/(-8)))
    a = '*' * i
    b = '.' * (scale - i)
    c = (i/scale)*100
    dur = time.perf_counter() - start
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c, a, b, dur), end='')
    time.sleep(0.1)
print("\n"+"执行结果".center(scale//2, '-'))

