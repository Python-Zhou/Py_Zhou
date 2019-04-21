score = eval(input('请输入分数'))

if score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'

print("等级是{}".format(grade))