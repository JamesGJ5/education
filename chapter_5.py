def print_hello():
    print("hello")

def do_n(f, n):
    if n <= 0:
        return
    f()
    do_n(f, n - 1)

do_n(print_hello, 0)