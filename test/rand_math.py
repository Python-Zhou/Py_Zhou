import random
'''
输入一个三位数与程序随机数比较大小
如果大于程序随机数,则分别输出这个三位数的个位\十位\百位
如果等于程序随机数,则提示中奖,记100分
如果小于程序随机数,则将120个字符输入到文本文件中
    (规则是每一条字符串的长度为12,单独占一行,并且前四个,后八个是数字)
'''

class GameNum():

    def line(self):
        # 定义一个空字符串用于拼接字符
        str_num = ''
        # 循环前四个随机字母（用ascii码对应的值来随机在转换为字母）
        for i in range(4):
            # 97-123是小写字母的ascii码值
            str_s = random.randrange(97,123)
            # 将ascii码值转换为对应的字母
            str_s = chr(str_s)
            # 依次拼接
            str_num = str_num +str_s
        # print(str_num)
        # 循环后八个随机数字
        for i in range(8):
            num = random.randrange(0,10)
            str_num = str_num + str(num)
        # print(str_num)
        return str_num

    def num_game(self, total, source):
        print(self,'$')
        while 1:
            # 输入函数
            num = input("请输入三位数,输入-1结束:")
            if num == "-1":
                break
            # 程序随机数
            random_num = random.randrange(100, 1000)
            # 检测输入是否是纯数字
            if num.isdigit() and 100 <= int(num) <= 999:  # 输入函数返回的是字符类型，不能与整形直接比较，需要强制类型转换
                # 计算有效输入多少次
                total += 1
                print('输入%d次'%total)
                num = int(num)
                # 判断随机数与输入数的大小
                if num > random_num:
                    # 求百位数字方法是地板除100或用数学模块中的floor（）函数
                    baiwei = num//100
                    # 求十位数字有两个思路
                    shiwei = (num - baiwei * 100)//10
                    shiwei2 = num%100//10
                    # 求个位有两个思路
                    gewei = num%100%10
                    geiwei2 = num%10
                    print(baiwei,shiwei,shiwei2,gewei,geiwei2)
                    print("这个数的百位是{0}，十位是{1}，个位是{2}".format(baiwei,shiwei,gewei))
                if int(num) == random_num:
                    source = source + 10
                    print('你中奖了，分数是', source)
                    print()
                if int(num) < random_num:
                    # 由于120个字符每行12个，只需存入10行即可
                    for i in range(10):
                        str_line = GameNum.line(self)
                        print(str_line)
                        # 执行文件存入操作
                        with open('str_num.txt','a') as f:
                            f.write(str_line + '\n')
            else:
                print("请按规定输入")

# 程序入口
if __name__ == '__main__': #  调试代码
    print(__name__)  # 在本身模块中__name__ == __main__ ,但是当作为第三方包导入之后（import rand_math),__name__ == 文件名
    # 定义一个变量用于存取初试分数
    source = 0
    # 定义一个变量用于统计输入了多少次
    total = 0
    # GameNum.num_game(0,total, source)
    # 实例化类
    game = GameNum()
    game.num_game(source,total)


