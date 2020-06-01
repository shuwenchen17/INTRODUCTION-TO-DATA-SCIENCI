def absolute(x):
    """
    Returns the absolute value of x.
    """
    if x < 0:
        abs_x = -x
        print("{}的絕對值是{}".format(x, abs_x))
        return abs_x
    else:
        print("{}的絕對值是{}".format(x, x))
        return x
posotive_56 = absolute(-5566)
print(posotive_56)
