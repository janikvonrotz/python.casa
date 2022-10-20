def f(x): return x

import inspect
lines = inspect.getsource(f)
print(lines)