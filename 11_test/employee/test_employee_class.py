from employee import Employee


def test_give_default_raise():
    """测试增加默认工资"""
    employee = Employee("ming", "xiao", 60000)
    employee.give_raise()
    assert employee.year_salary == 65000


def test_give_custom_raise():
    """测试增加任意工资"""
    employee = Employee("ming", "xiao", 60000)
    employee.give_raise(20000)
    assert employee.year_salary == 80000
