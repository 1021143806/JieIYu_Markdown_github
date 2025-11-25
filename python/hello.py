#1 Python 基础

# print('Hello')
# print('World')

# for x in range(1,10):  #数字的列表不包含结束的数字，输出1-9
#     print(x)  

# if True :
#     print("welcome")
# if False:
#     print("goodbye")

# import random
# print(random.randint(1, 100))  # 输出1到100之间的随机整数

# import random
# for x in range(1,10):    #掷色子*10
#     randomNumber = random.randint(1,6)
#     print(randomNumber)  # 输出1到6之间的随机整数

# import random
# for x in range(1,10):    #掷两个色子*10
#     randomNumber1 = random.randint(1,6)
#     randomNumber2 = random.randint(1,6)
#     total=randomNumber1+randomNumber2
#     if randomNumber1==randomNumber2:
#         print("double")
#     else:
#         if total >8:
#             print ("big")
#         elif total >4 and total <=8:
#             print ("not bad")
#         else:
#             print("small")
#     print(total)  # 输出和

# import random
# #for x in range(1,10):    #掷出6停止
# randomNumber1 = 0
# randomNumber2 = 0
# while not (randomNumber1 == 6 and randomNumber2 == 6):#直到骰到两个6为止
#     randomNumber1 = random.randint(1,6)
#     randomNumber2 = random.randint(1,6)
#     total=randomNumber1+randomNumber2
#     if randomNumber1==randomNumber2:
#         print("double")
#     else:
#         if total >8:
#             print ("big")
#         elif total >4 and total <=8:
#             print ("not bad")
#         else:
#             print("small")
#     print(total)  # 输出和

#不停掷色，直到掷出两个色子点数一致
# import random
# randomNumber1 = 0
# randomNumber2 = 0
# while True:
#     randomNumber1 = random.randint(1,6)
#     randomNumber2 = random.randint(1,6)
#     total=randomNumber1+randomNumber2
#     print(total)  # 输出和
#     if randomNumber1==randomNumber2:
#         print("double")
#         break
#     else:
#         if total >8:
#             print ("big")
#         elif total >4 and total <=8:
#             print ("not bad")
#         else:
#             print("small")

#2 字符串、列表和字典

# 字符串
# bookName = "My Python World"
# # >>> bookName = "My python World"
# # >>> bookName
# # 'My python World'
# print(bookName)
# print(len(bookName))  # 获取字符串长度
# print(bookName[0])  # 获取第一个字符
# print(bookName[0:2])  # 获取第一个和第二个字符
# print(bookName[3:])  # 获取第四个字符到最后
# print(bookName[-1])  # 获取最后一个字符
# print(bookName[-2])  # 获取倒数第二个字符
# print(bookName[0:5])  # 获取前五个字符
# print(bookName[0:5:2])  # 获取前五个字符中的每隔一个字符
# print(bookName[0:5:3])  # 获取前五个字符中的每隔两个字符
# print(bookName[0:5:4])  # 获取前五个字符中的每隔三个字符

#列表
# numbers = [1, 2, 3, 4, 55]
# print(numbers)
# print(len(numbers))  # 获取列表长度
# numbers.insert(0, 0)  # 在列表开头插入0

# complexList = [1, 2, 3, 4, 5, ["hello", "world", True, False]]
# print(complexList)
# print(complexList[5][2])  # # 获取第三个元素的第三个字符

#函数
# 定义函数
# def addWords(sentence):
#     newString = sentence + 'please'
#     return newString
# print(addWords('hello '))  # 调用函数，输出 hello please

# def say_hello(n):
#     for x in range(0,n):
#         print("Hello World")
# say_hello(5)  # 调用函数，输出 Hello World 5次

#猜字游戏
