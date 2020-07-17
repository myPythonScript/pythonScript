# -*- coding:utf-8 -*-
# import random
#
# for  i in range(0, 6):
#     print(i)
#
#
# print(random.randint(1, 10))
# print(random.random())
# print(random.uniform(1.1,2))
#
# print( random.randrange(1,100,2) )


# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print("%d * %d = %d\t" % (i, j, i * j),end="")
#     print()
# import time
# print (time.strftime("%Y%m%d-%H%M%S",time.localtime(time.time())))
# # print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

# leap = 1
# for i in range(101, 200):
#     for j in range(2, i):
#         if i % j == 0:
#            leap = 0
#            break
#     if leap == 1:
#         print(i)
#     leap = 1


for a in range(100,1000):
    i = a // 100
    j = a // 10 % 10
    k = a % 10
    if a == i ** 3 + j ** 3 + k**3:
        print(a)

