if __name__ == "__main__":
    def safe_print_division(a, b):
        try:
            result = a / b
        except ZeroDivisionError:
            result = None
        finally:
            #print("Inside result: {}".format(result))
            result = safe_print_division(a, b)
            print("{:d} / {:d} = {}".format(a, b, result))
        return result



