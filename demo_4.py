# 猜数字
import random
answer = random.randint(0, 10)  # 设置一个0~9的随机整数
a = 3
sentence = "欢迎来到猜数字游戏！\n请猜一个不大于10的自然数(你共有3次机会)：\n"
while a > 0:
    num = int(input(sentence))
    if num == answer:
        print("恭喜你猜对了，但没有奖品^-^")
        break
    else:
        if num > answer:
            print("太大了！\n")
            b = str(a-1)
            sentence = "你还剩"+b+"次机会,请继续"
        else:
            print("太小了！")
            b = str(a - 1)
            sentence = "你还剩" + b + "次机会,请继续"
        a = a - 1
print("游戏结束！")
