def is_same_class(obj, a_class):
    # Get the type of the object 'obj'
    obj_type = type(obj)
    
    # Compare the type of the object with the specified class 'a_class'
    # and return True if they are the same, otherwise return False
    return obj_type == a_class

