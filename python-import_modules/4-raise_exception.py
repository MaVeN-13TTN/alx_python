def raise_exception():
    # Raise a TypeError exception with a custom message
    raise TypeError("Custom exception message")

try:
    raise_exception()
except TypeError as te:
    print("Exception raised")