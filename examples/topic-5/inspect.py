import inspect
lines = inspect.getsource(eval)
print(lines)