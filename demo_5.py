# 成绩转化成等级
while 1 == 1:
    grade = int(input("请输入你的成绩(0~100)："))
    level = ("S" if grade == 100 else
             "A" if 80 <= grade < 100 else
             "B" if 60 <= grade < 80 else
             "C" if 30 <= grade < 60 else
             "D" if 0 < grade < 30 else
             "E" if grade == 0 else
             "请输入正确的分值(0~100)！")
    print("成绩等级: "+level)
