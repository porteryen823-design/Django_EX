def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    fibs = [0, 1]
    for i in range(2, n + 1):
        fibs.append(fibs[i - 1] + fibs[i - 2])
    return fibs[n]

for i in range(40):
    print(f"F({i:2}) = {fibonacci(i):7}")
