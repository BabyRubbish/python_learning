from name_function import get_formatted_name


def test_first_last_name():
    """能够正确处理像 Janis Jopin 这样的姓名吗?"""
    formatted_name = get_formatted_name("janis", "joplin")
    assert formatted_name == "Janis Joplin"


def test_first_last_middle_name():
    """能够正确处理像 Wolfgang Amadeus Mozart 这样的姓名吗?"""
    formatted_name = get_formatted_name("wolfgang", "amadeus", "mozart")
    assert formatted_name == "Wolfgang Mozart Amadeus"
