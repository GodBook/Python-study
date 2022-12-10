# 找质数
while True:
    num = int(input("我想找所有在0到？中间的质数。\n整数？= "))
    if num == 0:
        print("无结果，0既不是质数也不是合数！\n")
    elif num == 1:
        print("在0到1中间的质数有：1 ")
    elif num >= 2:
        print("0~", num, "之间的质数有：")
        for a in range(2, num + 1):
            for b in range(2, a):
                if a % b == 0:  # 此时a不是质数
                    break
            else:
                print(a, end=" , ")
        print("\n")
    else:
        print("请输入一个正确的数！\n")
