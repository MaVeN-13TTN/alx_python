def raise_exception():
    raise TypeError("This function raises a TypeError exception.")

try:
    raise_exception()
except TypeError as te:
    print("Exception raised")