'''
猜数字游戏：
（1）提示用户“猜数字游戏开始了”
（2）指定一个数字让用户来猜
（3）提示用户猜一个数字并获取用户猜的数字
（4）把用户猜的数字和指定的数字进行比较
	如果猜对了，输入“恭喜你，猜对了，可惜没有奖励！”
	如果猜错了，输出“猜错了，正确答案是**”
（5）猜完以后输出“游戏结束了，不玩了！”

'''
print("猜数字游戏开始了")
a = 7
b = input("请输入你猜的数字：")
c = int(b)
d = 0
while d < 1:
    if a == c :
        print("恭喜你，猜对了，可惜没有奖励！")
    else:
        print("猜错了，正确答案是" , a)
    d = d + 1
print("游戏结束了，不玩了！")