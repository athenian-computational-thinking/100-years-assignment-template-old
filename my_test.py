from my_code import year_100


def test_inc():
    assert 2105 == year_100(15)
    assert 2120 == year_100(0)
    assert 2095 == year_100(25)
