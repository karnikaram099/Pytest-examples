# import pytest
#
# @pytest.fixture()
# def setup():
#     print("before every method setup will be excicuted")
#
# def testmethod1(setup):
#     print("method1 is excicuted")
#
# def testmethod2(setup):
#     print("method2 is going to execute")
#


import pytest
@pytest.yield_fixture()
def setup():
    print("this is going to execute before every test method")
    yield
    print("this is going to execute after every test method")

def testmethod1(setup):
    print("test method one is  going ton execute")

def testmethod2(setup):
    print("test method 2 is going to execute")