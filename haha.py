import random
start = input('请输入初始值：')
end = input('请输入末尾值：')
start = int(start)
end = int(end)
r = random.randint(start,end)
count = 0
while True :
	count += 1
	num = input("请输入数字：")
	num = int(num)
	if num > r :
		print('太大了，小一点！')
	elif num < r :
		print('太小了，大一点！')
	else :
		print('恭喜你猜对了')
		print('这是你猜对的第',count,'次')
		break