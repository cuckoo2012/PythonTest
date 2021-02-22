# # -*- coding: utf-8 -*-
# # @Author : feier
# # @File : conftest.py
import pytest
import yaml
import os
'''
1、获取yaml文件中的参数
2、在执行测试用例之前，用@pytest.fixture 初始化测试数据
3、对测试对象进行模块实例化
'''

# # 通过 os.path.dirname 获取当前文件所在目录的路径
from calculator.page.calculator import Calculator

yaml_file_path = os.path.dirname(__file__) + "/data.yml"

with open(yaml_file_path,encoding="utf-8") as f:
    datas = yaml.safe_load(f)
    print(datas)
    # 获取文件中key为datas的数据
    add_datas = datas["add_datas"]
    # 获取文件中key为myids的数据
    add_ids = datas["add_myids"]

    #除法
    div_datas= datas["div_datas"]
    div_myids= datas["div_myids"]
    #减法
    sub_datas= datas["sub_datas"]
    sub_myids= datas["sub_myids"]
    #乘法
    mul_datas= datas["mul_datas"]
    mul_myids= datas["mul_myids"]
#加法
@pytest.fixture(params=add_datas, ids=add_ids)
def get_add_datas(request):
    print("开始计算")
    data = request.param
    print(f"request.param的-加法-测试数据是：{data}")
    yield data
    print("结束计算")
#除法
@pytest.fixture(params=div_datas, ids=div_myids)
def get_div_datas(request):
    print("开始计算")
    data = request.param
    print(f"request.param的-除法-测试数据是：{data}")
    yield data
    print("结束计算")
#减法
@pytest.fixture(params=sub_datas, ids=sub_myids)
def get_sub_datas(request):
    print("开始计算")
    data = request.param
    print(f"request.param的-减法-测试数据是：{data}")
    yield data
    print("结束计算")
#乘法
@pytest.fixture(params=mul_datas, ids=mul_myids)
def get_mul_datas(request):
    print("开始计算")
    data = request.param
    print(f"request.param的-乘法-测试数据是：{data}")
    yield data
    print("结束计算")

@pytest.fixture(scope="module")
def get_calc():
    print("获取计算器实例")
    calc = Calculator()
    return calc