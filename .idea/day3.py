#coding=utf-8
"""
youSay=raw_input("你说：")
sheSay=raw_input("她说：")

'''
if youSay=="去" and sheSay=="去":
    print("可以去")
'''

if youSay=="去" or sheSay=="去":
	print("可以去")

"""

"""
color=raw_input("你白吗？")
money=raw_input("你有钱吗？")
beautiful=raw_input("你漂亮吗？")
if color=="白" and money=="富" and beautiful=="美":
	print("你是白富美")
else:
	print("矮穷丑")
"""

"""
a=10
if  not(a>20 and a<30):
	print("不在范围")
"""

"""
sex=raw_input("你的性别？")
if sex=="男":
	print("你可以留胡子")
elif sex=="女":
	print("你可以留长头发")
else:
	print("你是中性人")
"""

"""
num=int(raw_input("请输入1-7:"))
if num==1:
	print("星期1")
elif num==2:
	print("星期2")
elif num==3:
	print("星期3")
elif num==4:
	print("星期4")
elif num==5:
	print("星期5")
elif num==6:
	print("星期6")
elif num==7:
	print("星期日")
else:
	print("你输入的有误")
"""


"""
num=1
while num<=100:
	print(num)
	num=num+1
"""

"""
ticket=1 #1 有票 0 没票
kinfeLenth=8

if ticket==1:
	print("可以去安检")
	if kinfeLenth<=10:
		print("安检通过")
	else:
		print("安检没通过")
else:
	print("你还没买票")
"""

"""
i=1
while i<=5:
	j=1
	while j<=i:
		 print("*",end="") #python3
		 j=j+1
	print("")
	i=i+1
"""

"""
i=1
while i<=9:
	j=1
	while j<=i:
	     print("%d*%d=%d\t"%(j,i,i*j),end="")
	     j+=1
	print("")
	i+=1
"""

"""
import random
player=int(raw_input("请输入0剪刀1石头2布："))
computer=random.randint(0,2) 
if (player==0 and computer==2) or(player==1 and computer==1)or(player==2 and computer==1):
	print("你赢了")
elif player==computer:
	print("平局")
else:
	print("你输了")
"""

"""
name="Hello"
for temp in name:
	print(temp)
"""

"""
i=1
num=0
while i<=100:
	if i%2==0:
	   print(i)
	   num+=1
	if num==20:
	   break
	i+=1
"""