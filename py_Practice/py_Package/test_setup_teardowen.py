def setup_module():
    print("\nsetup_module:整个test_setup_teardown.py模块开始前只执行一次")
def teardown_module():
    print("\nteardown_module:整个test_setup_teardown.py模块结束后只执行一次")

def setup_function():
    print("\nsetup_function:不在类中的用例执行前")

def teardown_function():
    print("\nteardown_function:不在类中的用例执行后")

def test_three():
    print("正在执行test three")

def test_four():
    print("正在执行test four")
class TestClass():
    #setup\teardown 后面不带_参数时，在class内就再类里面用，放在class外就再类外面用
    def setup_method(self):
        print("\nsetup_method每个用例执行")
    def teardown_method(self):
        print("\nteardown_method每个用例执行")
    def setup_class(self):
        print("\nsetup_class:所有用例执行前")
    def teardown_class(self):
        print("\nteardown_class:所有用例结束执行")
    def test_one(self):
        print("one正在执行")
    def test_two(self):
        print("two正在执行")

class TestClass02():
    def test_one(self):
        print("2one正在执行")

    def test_two(self):
        print("2two正在执行")