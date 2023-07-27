
def raise_exception_msg(message=""):
    error_message = f"NameError: {message}"
    exec("raise " + error_message)
    #def raise_exception_msg_with_line_number(message="", line_number=0):
        #error_message = f"NameError: {message} at line {line_number}"