def say_hello(name):
    print("こんにちは" + str(name) + "さん")

say_hello("山田")

def func(a, b=5):
    print(a)
    print(b)

func(2,15)
func(3)

def sample(arg, arg_list=[]):
    arg_list.append(arg)
    print(arg_list)

sample('python')
sample('Python')

def sample(arg):
    arg_list = [] # リストの初期化
    arg_list.append(arg)
    print(arg_list)

sample('python') # ['python']
sample('Python')

#演習
def gen_text(text, num):
    return text * int(num)
text = gen_text("回数", 3)
print(text)

text2 = gen_text("パイソん", 5)
print(text2)

from random import choice

def get_fortune():
    # ここにコードを記述して下さい。
    results = ['大吉', '吉', '小吉', '凶', '大凶', '末吉']
    return "今日の運勢は" +  choice(results) + "です"

result = get_fortune()
print(result) # 今日の運勢は大吉です