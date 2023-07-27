if __name__ == "__main__":
    def raise_exception():
        #raise TypeError("An exception has been raised")
        try:
            raise_exception()
        except TypeError as te:
             print("Exception has been raised")
