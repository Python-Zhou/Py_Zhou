class GameZiMu():
    # 打印字母A
    def A(self):
        # 控制行
        for i in range(1,6):
            # 判断开始输入的位置
            for k in range(5-i):
                print("",end = " ")
            # 控制列
            for j in range(1,i+1):
                if i ==1 or i == 3 or j ==1 or j ==i:
                    print('*',end = " ")
                else:
                    print(" ", end =" ")
            print()
    A()

    # 打印字母B
    def B(self):
        # 打印字母B
        for i in range(1, 4):
            for j in range(1, 4):
                if i == 1 or i == 4 or j ==1:
                        if j < 3:
                            print('*', end=' ')
                elif j==3:
                    if i==2 or i == 3:
                        print('*', end=' ')
                else:
                    print(' ', end=' ')
            print()

        for i in range(1, 5):
            for j in range(1, 4):
                if i == 1 or i == 4 or j ==1:
                        if j < 3:
                            print('*', end=' ')
                elif j==3:
                    if i==2 or i == 3:
                        print('*', end=' ')
                else:
                    print(' ', end=' ')
            print()
    B()

    def zimu_bame(self):
        zimu = input('请输入一个大写字母A-B')
        if