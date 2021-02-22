import pytest



#参数中可以为元组也可以列表
@pytest.mark.parametrize("a",[0,1])
@pytest.mark.parametrize("b",[3,4,5])
def test_foo(a,b):
    print("测试参数堆叠组合：a->%s,b->%s"%(a,b))