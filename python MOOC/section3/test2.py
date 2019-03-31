# DayDayUp02.py
# 工作日每天提高1%，休息日下降1%
dayup = 1
dayfactor = 0.01
for i in range(1,366):
    if i % 7 in [6, 0]:
        dayup = dayup * (1-dayfactor)
    else:
        dayup = dayup * (1 + dayfactor)
print("{:.2f}".format(dayup))



