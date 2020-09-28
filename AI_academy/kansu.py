a = [10, 20, 30, 40, 50]
print(len(a))

from random import choice
print(choice(a))

def hello():
    print("hello!")

# 関数の呼び出し(実行)
hello()

print("名前を入力してください")
name = input("名前を入力してください")
print("あなたの名前は"+name+"です")

while True:
    print("Please Input!")
    i = input()
    print(i)