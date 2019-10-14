"""
regex  re模块功能演示
"""
import re

# 目标字符串
s = "Anan:1992,Liufeng:1996"
pattern = r"(\w+):(\d+)"  # 正则表达式

# re模块调用findall
l = re.findall(pattern,s)
print(l)

# compile对象调用findall
regex = re.compile(pattern)
# l = regex.findall(s)
l = regex.findall(s, 0, 12)
print(l)

# 按照正则表达式匹配内容切割字符串
# l = re.split(r"[:,]",s)
l = re.split(r"[:,]",s,1)   #
print(l)

# 替换目标字符串
# s = re.sub(r":","-",s)  # 默认全部替换
s = re.sub(r":","-",s,1)
print(s)
