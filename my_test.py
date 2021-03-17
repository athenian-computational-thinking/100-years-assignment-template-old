from my_code import year_100


def test_inc():
    assert 2106 == year_100(15)
    assert 2121 == year_100(0)
    assert 2096 == year_100(25)
