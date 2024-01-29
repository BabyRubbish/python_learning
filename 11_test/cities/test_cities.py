from city_function import city_country


def test_city_country():
    """测试函数能否正确处理 santiago chile 的实参"""
    combination = city_country("santiago", "chile")
    assert combination == "Santiago, Chile"


def test_city_country_population():
    """测试函数能否正确处理 santiago chile population=5_000_000 的实参"""
    combination = city_country("santiago", "chile", 5_000_000)
    assert combination == "Santiago, Chile - Population 5000000"
