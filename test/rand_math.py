import random
'''
输入一个三位数与程序随机数比较大小
如果大于程序随机数,则分别输出这个三位数的个位\十位\百位
如果等于程序随机数,则提示中奖,记100分
如果小于程序随机数,则将120个字符输入到文本文件中(规则是每一条字符串的长度为12,单独占一行,并且前四个,后八个是数字
'''

# 输入函数
num = input("请输入三位数:")
# 程序随机数
random_num = random.randrange(100, 1000)
# 检测输入是否是纯数字
if num.isdigit() and 100 <= int(num) <= 999:  # 输入函数返回的是字符类型，不能与整形直接比较，需要强制类型转换
    num = int(num)
    # 判断随机数与输入数的大小
    if num > random_num:
        # 求百位数字方法是地板除100或用数学模块中的floor（）函数
        baiwei = num//100
        # 求十位数字有两个思路
        shiwei = (num - baiwei * 100)//10
        shiwei2 = num%100//10
        # 求个位
        gewei = num%100%10
        print(baiwei,shiwei,shiwei2,gewei)
    if int(num) == random_num:
        print(random_num)
    if int(num) < random_num:
        print(random_num)
else:
    print("请按规定输入")