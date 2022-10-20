def pluszwei(zahl):
    return (zahl + 2)

try:
    print(pluszwei(2))
    print(pluszwei('3'))
except TypeError:
    print("Parameter muss int oder float sein.")