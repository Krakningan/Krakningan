#!/usr/bin/env python
# coding: utf-8

# In[1]:


a = int(input("Введите a: "))
b = int(input("Введите b: "))
(b, a) = (a, b)
print("a =", a)
print("b =", b)


# In[2]:


a_str = input("Введите число: ")
sum = 0
for l in a_str:
    sum += int(l)
print("Сумма -", sum)


# In[3]:


try:
    a = int(input("Введите a: "))
    b = int(input("Введите b: "))
    c = int(input("Введите c: "))
    if a != 0:
        d = b*b - 4*a*c
        if d > 0:
            x1 = (-b + d**(1/2)) / (2*a)
            x2 = (-b - d**(1/2)) / (2*a)
            print("x1 =", x1)
            print("x2 =", x2)
        elif d == 0:
            x = -b / (2*a)
            print("x =", x)
        else:
            print("Дискриминант меньше нуля, уравнение не имеет действительных решений")
    else:
        print("Это не квадратное уравнение")
except ValueError:
    print("Все переменные должны быть числами")


# In[ ]:




