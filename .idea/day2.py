#coding=utf-8

#单行注释
#print("hello")


#多行注释
'''
print("hello")
print("hello")
print("hello")
print("hello")
'''

"""
print("hello")
print("hello")
print("hello")
"""

'''
applePrice=3.6 #苹果的价格
weight=3 #苹果的重量
monney=applePrice*weight
print(monney)
'''

'''
height=input("请入你的身高：")
print("身高:%d"%height)
'''

'''
print("---------------")
name=raw_input("请输入名字:") #python2
age=raw_input("请输入年龄：")
"""name=input("请输入名字:") #python3
age=input("请输入年龄：") """
print("----------------")
print("名字:%s"%name)
print("年龄：%s"%age)
'''

"""
age=raw_input("请输入你的年龄：")#默认输入的字符串类型
age_num=int(age)

# age=19
if  age_num>18:
	print("你成年了，可以去网吧")
else:
	print("你未成年，不可以去网吧")
"""

#可以输出多行
'''
age=19
if age>18:
	print("111")
	print("222")
print("aaa") #不管条件是否成立它都会执行
'''

#运算符
'''
a=5
b=3
print("和:%d"%(a+b))
print("差:%d"%(a-b))
print("积:%d"%(a*b))
print("商:%d"%(a//b))
print("取整:%d"%(a/b))
print("取余:%d"%(a%b))
'''
"""
print("幂：%d"%(2**10))
print("幂：%d"%(2**16))
print("hi"*6)
"""

'''
name="python"
age=1
print("name:%s,age:%d"%(name,age))
'''