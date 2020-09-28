def add(x1):
    x2 = 10 # 関数内で変数を作成(ローカル変数)
    result = x1 + x2
    print(result)

add(5) # 5 + 10で15が出力

#folse
def add(x1):
    x2 = 10 # 関数内で変数を作成(ローカル変数)
    result = x1 + x2
    print(result)

add(5) # 5 + 10で15が出力
# print(x2) # ここでエラーが発生

#correct
def add(x1,x2):
    result = x1 + x2
    return result

x1 = 5
x2 = 10
result = add(x1, x2) # 5 + 10で15が出力
print(result)

#3
glb = 0

def func1():
    glb = 1

def func2():
    global glb
    glb = 5

print(glb) # 0が出力される
func1()
print(glb) # 0が出力される
func2()
print(glb) # 5が出力される

#4
var1 = 'グローバル変数'

def sample():
    var2 = 'ローカル変数'
    return (var1, var2)

print(sample())

#演習
from random import choice

def get_fortune():
    # ここにコードを記述して下さい。
    results = ['大吉', '吉', '小吉', '凶', '大凶', '末吉']
    return ("今日の運勢は" + choice(results) + "です")

result = get_fortune()
print(result) # 今日の運勢は大吉です