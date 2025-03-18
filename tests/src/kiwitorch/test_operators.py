from kiwitorch.scalar import Scalar


def test_return_two():
    a = Scalar(1.0)
    b = Scalar(2.0)
    c = a + b
    assert c.data == 3.0
    # assert return_two() == 2
