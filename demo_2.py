# 转义字符\n \t \b \\ \' \"
print('ab')
print('a\nb')

# \t 水平制表符，将光标移动到下一个tab键按下的位置
print('abcd')
print('ab\tcd')
print('abc\td')
print('abcd\te')
print('abcde\tf')

# \r 回车，使光标回到行首
print('ab\rcd')

# \b 退格
print('ab\bcd')

# \\  \' \"
print('\\', '\'', '\"')

# 原字符可以使字符串中的转义字符失效，通常在字符串之前加上r或R
print(r'ac\ncd')
print(R'\t\b\r')
