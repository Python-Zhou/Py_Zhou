# WeekNamePrintV1.py
weekStr = "星期一星期二星期三星期四星期五星期六星期日"
aa = input("输入一个数字：")
print(weekStr[eval(aa[-1])*3-3: eval(aa[-1])*3])
