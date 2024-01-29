class Employee:
    """创建一个职员类"""

    def __init__(self, first, last, salary) -> None:
        """初始化职员属性"""
        self.first_name = first
        self.last_name = last
        self.year_salary = salary

    def give_raise(self, increment=5000):
        """给职员加工资"""
        self.year_salary += increment
