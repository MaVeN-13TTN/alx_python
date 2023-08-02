def raise_exception():
    try:
        # Raise the TypeError here
        raise TypeError("This is a type exception!")
    except TypeError as e:
        print("Exception has been raised")