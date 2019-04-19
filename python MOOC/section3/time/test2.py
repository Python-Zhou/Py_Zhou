import time
t = time.gmtime()
k = time.strftime("%a")

if k in ['Sat', 'Sun']:
    print("周日")
else:
    print("工作日")