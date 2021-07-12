import random
r = random.randint(1, 100)
while True:
    num = input('請猜一個數字: ')
    num = int(num)
    if num == r:
        print('恭喜你!你猜對了!')
        break
    elif num > r:
        print('不對喔，答案比較小')
    elif num < r:
        print('不對喔，答案比較大')