def print_hello(times):
    if (times == 0): return
    print("Hello Word")
    print_hello(times - 1)


print_hello(20)
