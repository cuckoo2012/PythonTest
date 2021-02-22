'''这个是装饰器的前身'''
# import time
#
# def sum(*kwargs):
#     total = 0
#     for ele in kwargs:
#         total = total + ele
#     time.sleep(5)
#     return total
#
# #func这里指的是sum方法，此时的func可以传入其他不同的方法
# def record_time(func):
#     def wrapper(*kwargs):
#         print('function start at {}'.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) ))
#         total = func(*kwargs)
#         print('function end at {}'.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) ))
#         return total
#     return wrapper
#
# if __name__ == "__main__":
#     print(record_time(sum)(1,2,3,4))

'''下面的代码是将上面一段代码简单的变更，写成了规范的语法糖'''
import time
def record_time(func):
    def wrapper(*kwargs):
        print('function start at {}'.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) ))
        total = func(*kwargs)
        print('function end at {}'.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) ))
        return total
    return wrapper

@record_time
def sum(*kwargs):
    total = 0
    for ele in kwargs:
        total = total + ele
    time.sleep(5)
    return total

if __name__ == "__main__":
    print(sum(1,2,3,4))
