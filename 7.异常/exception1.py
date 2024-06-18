def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")

divide(2, 1)
print('-' * 40)

divide(2, 0)
print('-' * 40)

divide("2", "1")
print('-' * 40)
