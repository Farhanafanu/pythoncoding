def check_scope():
    def do_local():
        test = "local test"  # This creates a local variable 'test' within 'do_local()'.

    def do_nonlocal():
        nonlocal test  # 'nonlocal' is used to indicate that 'test' refers to the nearest enclosing scope.
        test = "nonlocal"  # This modifies the value of 'test' in the nearest enclosing scope.

    def do_global():
        global test  # 'global' is used to indicate that 'test' refers to the global scope.
        test = "global"  # This modifies the value of the global variable 'test'.

    test = "default"  # This is a local variable within 'check_scope()'.
    print("Before any changes:", test)  # Output: Before any changes: default

    do_local()  # This calls the 'do_local()' function, but it doesn't affect the value of 'test'.
    print("After 'do_local()':", test)  # Output: After 'do_local()': default

    do_nonlocal()  # This calls the 'do_nonlocal()' function and modifies the value of 'test'.
    print("After 'do_nonlocal()':", test)  # Output: After 'do_nonlocal()': nonlocal

    do_global()  # This calls the 'do_global()' function and modifies the global variable 'test'.
    print("After 'do_global()':", test)  # Output: After 'do_global()': nonlocal


check_scope()
