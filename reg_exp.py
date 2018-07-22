
def search(pattern, text):
    "Return True if pattern appears anywhere in text"
    if pattern.startswith('^'):
        # pattern must occur at start of text
        return match(pattern[1:], text)
    else:
        # pattern can occur anywhere in the text
        return match('.*' + pattern, text)


def match(pattern, text):
    "Match pattern at beginning of text"
    print("matching %s in %s" % (pattern, text))
    if pattern == '':
        return True
    elif pattern == '$':
        return text == ''  # must match nothing before end of word
    elif len(pattern) >= 2 and pattern[1] in '*?':
        # need to match letter with wildcard modifier
        p, op, pat = pattern[0], pattern[1], pattern[2:]
        if op == '*':
            return ((match1(p, text) and match(pattern, text[1:])) or  # match at least 1 char
                    match(pat, text))  # or match none
        elif op == '?':
            return ((match1(p, text) and match(pat, text[1:])) or  # match 1 char
                    match(pat, text))  # or match none
    else:
        # the next pattern token to match is single letter
        return match1(pattern[0], text) and match(pattern[1:], text[1:])


def match1(p, text):
    "Match 1 letter at beginning of text"
    if not text:  # empty text
        return False
    else:
        return p == '.' or p == text[0]


def test():
    assert search('baa*!', "Sheep said baaaa!")
    assert search('baa*!', "Sheep said baaaa humbug") == False
    assert match('baa*!', "Sheep said baaaa!") == False
    assert match('baa*!', "baaaaaaaaa! said the sheep")
    assert search('def', 'abcdefg')
    assert search('def$', 'abcdef')
    assert search('def$', 'abcedfg') == False
    assert search('^start', 'not the start') == False
    assert match('start', 'not the start') == False
    assert match('a*b*c*', 'just anything')
    assert match('x?', 'text')
    assert match('text?', 'text')
    assert match('text?', 'tex')

    def words(text): return text.split()

    return "test passes"


print(test())
