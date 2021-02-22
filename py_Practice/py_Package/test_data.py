import yaml
#将字典格式创建并写入yaml文件中
# with open("yaml.yml","w") as f:
#     yaml.dump(data={'a':[1,2]},stream=f)
#读取yaml文件
# #读取方式一
# with open("yaml.yml","r") as f:
#     date = yaml.load(f,Loader=yaml.FullLoader)
#     print(date)

#读取方式二：
# print(yaml.load(open("yaml.yml"),Loader=yaml.FullLoader))

#读取三
def test01():
    date = yaml.safe_load(open("./data.yml"))
    print("yaml读取出来的格式",date)
    #print(date["a"])
    print("第一个数组值",date[0])
    print(f"第二个数组值{date[1]}")
    print("第一个数组中的字典值",date[0]["a"],date[0]["b"])
    print("第二个数组中的字典值", date[1]["aa"], date[1]["bb"])
    length = len(date)
    print(type(length))
    print(length)
    for i in range(length):
        print(f"第{i}个的数值值：{date[i]}")
