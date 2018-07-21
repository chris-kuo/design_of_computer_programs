import itertools
import re
import time
import timer

########## Cryptarithmetic Solver ##########


def solve(formula):
    """Given a formula like 'ODD + ODD == EVEN', fill in digits to solve it.
    Input formula is a string; output is a digit-filled-in string or None."""
    return next((f for f in fill_in(formula) if valid(f)))


def fill_in(formula):
    "Generate all possible fillings-in of letters in formula with digits."
    # should be a string
    letters = ''.join(
        [c for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" if c in formula])
    for digits in itertools.permutations('1234567890', len(letters)):
        table = str.maketrans(letters, ''.join(digits))
        yield formula.translate(table)


def valid(formula):
    """Formula is valid iff it has no numbers with leading zeros, and evals true"""
    try:
        return not re.search(r'\b0[0-9]', formula) and eval(formula) is True
    except ArithmeticError:
        return False


def faster_solve(formula):
    f, letters = compile_formula(formula)
    for digits in itertools.permutations((1, 2, 3, 4, 5, 6, 7, 8, 9, 0), len(letters)):
        try:
            if f(*digits) is True:
                table = str.maketrans(letters, ''.join(map(str, digits)))
                return formula.translate(table)
        except ArithmeticError:
            pass


def compile_formula(formula, verbose=False):
    letters = ''.join(set(re.findall('[A-Z]', formula)))
    parms = ', '.join(letters)
    tokens = map(compile_word, re.split('([A-Z]+)', formula))
    body = ' '.join(tokens)
    f = 'lambda %s: %s' % (parms, body)
    if verbose:
        print(f)
    return eval(f), letters


def compile_word(word):
    if word.isupper():
        terms = [('%s*%s' % (10**i, d)) for (i, d) in enumerate(word[::-1])]
        return '(' + "+".join(terms) + ')'
    else:
        return word


########## Test Functions ##########


examples = """TWO + TWO == FOUR
A**2 + B**2 == C**2
A**2 + BE**2 == BY**2
X / X == X
A**N + B**N == C**N and N > 1
ATOM**0.5 == A + TO + M
GLITTERS is not GOLD
ONE < TWO and FOUR < FIVE
ONE < TWO < THREE
RAMN == R**3 + RM**3 == N **3 + RX**3
sum(range(AA)) == BB
sum(range(POP)) == BOBO
ODD + ODD == EVEN
PLUTO not in set([PLANETS])""".splitlines()


def test():
    t0 = time.clock()
    for example in examples:
        print()
        print(13*' ', example)
        print('%6.4f sec:   %s ' % timer.timedcall(faster_solve, example))
    print('%6.4f tot.' % (time.clock() - t0))


test()
