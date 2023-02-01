def math_assertions(x, y):
    assert (x + y) == 15, "addition is incorrect"
    assert (x - y) == -5, "subtraction is incorrect"
    assert (x * y) == 50, "multiplication is incorrect"
    assert (x / y) == 0.5, "division is incorrect"
    print("assertions are correct")


if __name__ == "__main__":
    math_assertions(5, 10)
    math_assertions(10, 5)
