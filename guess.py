import random
r = random.randint(1, 100)
count = 0
while True:
    count += 1 #相當於count = count + 1
    num = input('請猜一個數字: ')
    num = int(num)
    if num == r:
        print('恭喜你!你猜對了!')
        print('這是你猜的第', count, '次')
        break
    elif num > r:
        print('不對喔，答案比較小')
    elif num < r:
        print('不對喔，答案比較大')
    print('這是你猜的第', count, '次')