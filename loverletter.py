#encoding=utf-8
import time, os, datetime

def print_content(content):
    for each_line in content:
        for each in each_line:
            print each,
            time.sleep(0.2)
        print
        time.sleep(0.5)
    print 

def now_time():
    return time.strftime("%Y-%m-%d")

def days(start, end):
    d1 = datetime.datetime.strptime(start, '%Y-%m-%d')
    d2 = datetime.datetime.strptime(end, '%Y-%m-%d')
    delta = d2 - d1
    return str(delta.days)

if __name__ == '__main__':
    know_days = int(days("2017-01-29", now_time())) + 1
    hands_days = int(days("2017-02-12", now_time())) + 1
    content1 = [u"这个世界上有那么多的地方", u"这个世界上有那么多的街巷", u"你没有早一步", u"也没有晚一步来到我的身旁", u"你", u"就是我的命运"]
    content2 = [u"当阳光照在海面上，那时我在想你", u"当月光洒在溪水上，那时我在想你", u"当夜风吹过树梢，那时我在想你", u"如果你是一颗珍珠，我愿意做你的贝壳", u"如果你是一只鸥鸟，我愿意做你的大海", u"如果你是一片白云，我愿意做你的天空", u"如果，如果你愿意", u"请让我分期付款一辈子", u"爱护你，守护你", u"让我们一起牵手到老！"]
    content3 = [u"我们相识：" + str(know_days) + u"天", u"我们牵手：" + str(hands_days) + u"天"]
    content4 = [u"老婆 我爱你！", "", u"LOVE YOU FOREVER", "", time.strftime("%Y-%m-%d %H:%M:%S")]
    for content in [content1, content2, content3, content4]:
        print_content(content)
        #os.system("pause")
        print
    os.system("pause")