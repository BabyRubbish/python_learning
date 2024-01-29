from survey import AnonymousSurvey


def test_store_single_response():
    """测试单个答案会被妥善地存储"""
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)
    language_survey.store_response("English")
    assert "English" in language_survey.responses


def test_store_three_response():
    """测试三个答案会被妥善地存储"""
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)
    responses = ["English", "Mandarin", "Spanish"]
    for response in responses:
        language_survey.store_response(response)
        assert response in language_survey.responses
