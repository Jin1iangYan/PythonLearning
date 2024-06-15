def make_incrementor(n):
    return lambda x: x + n

# 此时 f 是 lambda x: x + n，其中 n = 42
f = make_incrementor(42)
print(f(0))

print(f(1))
print(f(100))