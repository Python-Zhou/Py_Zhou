Adayup = pow(1+0.01, 365)

df1 = 0.01

def BdayUp(df):
    Bdayup = 1
    for k in range(1, 366):
        if k % 7 in [6, 0]:
            Bdayup = Bdayup * (1 - 0.01)
        else:
            Bdayup = Bdayup * (1 + df)
    return Bdayup

while BdayUp(df1) < Adayup:
    df1 += 0.001
print("{:.3f}".format(df1))

