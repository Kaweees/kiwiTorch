from utils import return_one


def hello():
    print("Hello from kiwitorch pkg")


def return_two() -> int:
    """Returns 2

    Returns:
        int: The number 2
    """
    return 1 + return_one()
