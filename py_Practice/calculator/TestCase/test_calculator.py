# -*- coding: utf-8 -*-
# @Author : feier
# @File : test_calc_new.py
import pytest


class TestCalc:
    '''
    pypi官网上对pytest-ordering的解释执行顺序的枚举值和用法
    https://github.com/ftobia/pytest-ordering/blob/develop/pytest_ordering/__init__.py
    '''
    # 测试add函数
    #@pytest.mark.first
    #跟下面的用法一致
    @pytest.mark.run(order=0)
    def test_add(self, get_calc, get_add_datas):
        result = None
        try:
            # 调用add函数,返回的结果保存在result里面
            result = get_calc.add(get_add_datas[0],get_add_datas[1])
            # 判断result结果是否等于期望的值
            if isinstance(result, float):
                result = round(result, 2)
        except Exception as e:
            print(e)
        assert result == get_add_datas[2]

    # 测试除法div函数
    @pytest.mark.run(order=3)
    def test_div(self, get_calc, get_div_datas):
        result = None
        try:
            # 调用div函数,返回的结果保存在result里面
            result = get_calc.div(get_div_datas[0],get_div_datas[1])
            # 判断result结果是否等于期望的值
            if isinstance(result, float):
                result = round(result, 2)
        except ZeroDivisionError as e:
            print(e)
        assert result == get_div_datas[2]

    @pytest.mark.run(order=1)
    # 测试减法sub函数
    def test_sub(self, get_calc, get_sub_datas):
        result = None
        try:
            # 调用sub函数,返回的结果保存在result里面
            result = get_calc.sub(get_sub_datas[0],get_sub_datas[1])
            # 判断result结果是否等于期望的值
            if isinstance(result, float):
                result = round(result, 2)
        except Exception as e:
            print(e)
        assert result == get_sub_datas[2]

    @pytest.mark.run(order=2)
    # 测试乘法mul函数
    def test_mul(self, get_calc, get_mul_datas):
        result = None
        try:
            # 调用mul函数,返回的结果保存在result里面
            result = get_calc.mul(get_mul_datas[0],get_mul_datas[1])
            # 判断result结果是否等于期望的值
            if isinstance(result, float):
                result = round(result, 2)
        except Exception as e:
            print(e)
        assert result == get_mul_datas[2]

'''
allure报告：
环境准备：1、pip install allure-pytest
2、需要java8+，JDK 1.8+环境，所以提前配置好java环境
http://allure.qatools.ru/ 下载allure-commandline ，
配置系统环境变量path(添加路径E:\allure-2.13.8\bin)可以生成测试报告

测试用例生成测试报告
1、生成数据pytest --alluredir=./result/algorithm
2、生成直接打开的报告 allure serve ./result/algorithm
3、生成报告allure generate ./result/algorithm -o ./report/ --clean
   #allure open -h 127.0.0.1 -p 8883 ./report/ 打开报告
   http://127.0.0.1:8883/index.html#suites测试报告地址可以放在不同的浏览器中执行

'''