import pytest

@pytest.mark.xfail(reason="Найдет баг в приложении, из-за которого тест падает")
def test_with_bug():
    assert 1 == 2

@pytest.mark.xfail(reason="Баг уже устранен, но на тествсе еше висит маркировка xfail")
def test_without_bug():
    ...
