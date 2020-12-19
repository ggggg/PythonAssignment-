# This function will print hello x times
def print_hello(times):
    if (times == 0): return
    print("Hello Word")
    print_hello(times - 1)

# start the program
print_hello(20)
