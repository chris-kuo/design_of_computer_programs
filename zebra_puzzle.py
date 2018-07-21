import itertools

houses = [1, 2, 3, 4, 5]
orderings = list(itertools.permutations(houses))


def imright(h1, h2):
    "House h1 is immediately right of h2 if h1 - h2 == 1."
    return h1 - h2 == 1


def nextto(h1, h2):
    "Two houses are next to each other if they differ by 1."
    return abs(h1 - h2) == 1


def zebra_puzzle():
    "Return a tuple (WATER, ZEBRA) indicating their hosue numbers."
    houses = first, _, middle, _, _ = [1, 2, 3, 4, 5]
    orderings = list(itertools.permutations(houses))  # 1
    return next((WATER, ZEBRA)
                for (red, green, ivory, yellow, blue) in orderings
                for (Englishman, Spaniard, Ukranian, Japanese, Norwegian) in orderings
                for (coffee, tea, milk, oj, WATER) in orderings
                if imright(green, ivory)  # 6
                if Englishman is red  # 2
                if Norwegian is first  # 10
                if nextto(Norwegian, blue)  # 15
                if coffee is green  # 4
                if Ukranian is tea  # 5
                if milk is middle  # 9
                for (OldGold, Kools, Chesterfields, LuckyStrike, Parliaments) in orderings
                if Kools is yellow  # 8
                if LuckyStrike is oj  # 13
                if Japanese is Parliaments  # 14
                for (dog, snails, fox, horse, ZEBRA) in orderings
                if Spaniard is dog  # 3
                if OldGold is snails  # 7
                if nextto(Chesterfields, fox)  # 11
                if nextto(Kools, horse)  # 12
                )


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


if __name__ == "__main__":
    print(timedcalls(10, zebra_puzzle))
