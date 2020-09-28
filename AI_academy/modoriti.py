def adder1(a, b):
    print(a+b)

def adder2(a, b):
    return a + b

adder1(2, 4)
sum = adder2(2, 4)
print(sum)

def a(a,b):
    return a + b

def b(a,b):
    return a * b

x = a(2,2) # xに4が代入
y = b(x, x)  # 4 * 4

print(y) # 16が出力される


#演習
def power(x):
    return x*x

def absolute(x):
    if (x < 0):
        return -x
    else:
        return x

power_value = power(10)#xに１０を代入
print(power_value) # 100

absolute_value = absolute(-10)#xに−１０を代入
print(absolute_value) # 10