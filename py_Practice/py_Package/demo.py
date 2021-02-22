# 原来的业务代码，打印计算一个元祖内数值的求和功能开始、结束时间
#
import time
def sum(*kwargs):
    print('function start at {}'.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) ))
    total = 0
    for ele in kwargs:
        total = total + ele
    time.sleep(5)
    print('function end at {}'.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) ))
    return total

if __name__ == "__main__":
    print(sum(1,2,3,4))


