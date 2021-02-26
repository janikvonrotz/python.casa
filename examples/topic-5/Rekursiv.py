def f(n):
    if n < 20:
        print(n)
        n += 1
        f(n)

f(0)