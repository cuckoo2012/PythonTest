import pytest
class Test01():
    def test_00(self):
        print("第一个测试用例")
    def test_02(self):
        print("第二个测试用例")
class Test02():
    def test_10(self):
        print("第三个测试用例")
    def test_12(self):
        print("第四个测试用例")

'''#第一种运行方式（Python解释器），下面此方式会把文件中的所有test用例都执行一遍'''

if __name__ == '__main__':
    #pytest.main(['test_pytestExcute.py'])
    #指定测试用例执行
    pytest.main(['test_pytestExcute.py::Test02'],'-v')

'''第二种方式在terminal中
1、输入命令指定某个类中的测试方法：pytest -sv test_pytestExcute.py::Test02::test_10
2、输入pytest -k "Test01" -v，会执行测试集类Test01下面的方法，执行结果如下：
test_practice.py::Test01::test_00 PASSED                                                                                     [ 50%]
test_practice.py::Test01::test_02 PASSED 
3、输入pytest -k "test_00 or test_10" -v，会执行对应指定的测试用例，测试结果如下：
test_practice.py::Test01::test_00 PASSED                                                                                     [ 50%]
test_practice.py::Test02::test_10 PASSED 
'''