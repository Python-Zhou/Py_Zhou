
'''
输入一个三位数与程序随机数比较大小
如果大于程序随机数,则分别输出这个三位数的个位\十位\百位
如果等于程序随机数,则提示中奖,记100分
如果小于程序随机数,则将120个字符输入到文本文件中(规则是每一条字符串的长度为12,单独占一行,并且前四个,后八个是数字
'''

# 输入函数
num = input("请输入三位数:")
# 程序随机数
random_num = random.randrange(100,1000)
#检测输入是否是纯数字
if num.isdigit() and 100<=int(num) <=999:
    # 判断随机数与输入数的大小
    if num > random_num:
        print(random_num)
    if num == random_num:
        print(random_num)
    if num < random_num:
        print(random_num)
else:
    print("请按规定输入")