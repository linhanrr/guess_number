import random
start = input('請輸入隨機變數開始值: ')
end = input('請輸入隨機變數結束值: ')
start = int(start)
end = int(end)
r = random.randint(start, end)
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