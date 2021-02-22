def inc(x):
    return x + 1
# 修改ini文件,让check开头的也能识别（python_files= check* test*）
# 因为配置了addopts = -sv，直接输入命令pytest check.py命令就可以执行该文件的测试用例了
''' 
pytest.ini 的参数说明可以参照pytest --help，会具体说明可以用那些参数，这些参数有什么含义
python_files (args):  glob-style file patterns for Python test module discovery
  python_classes (args):prefixes or glob names for Python test class discovery
  python_functions (args):prefixes or glob names for Python test function and method discovery
'''

def check_answer():
    print("这是我得第一条测试用例")
    assert inc(3) == 4

def test_foo():
    print("这是我得第二条测试用例")
    assert inc(3) == 4