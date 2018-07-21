import time


def timedcall(fn, *args):
    t0 = time.clock()
    result = fn(*args)
    t1 = time.clock()
    return t1 - t0, result


def timedcalls(n, fn, *args):
    times = []
    if isinstance(n, int):
        # time <n> execution of fn
        times = [timedcall(fn, *args)[0] for _ in range(n)]
    else:
        while sum(times) < n:
            times.append(timedcall(fn, *args)[0])
    return min(times), average(times), max(times)


def average(numbers):
    return sum(numbers) / float(len(numbers))
