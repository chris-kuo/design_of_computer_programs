
def search(pattern, text):
    "Return True if pattern appears anywhere in text"
    return match('.*' + pattern, text)


def match(pattern, text):
    pass


def test():
    assert search('baa*!', "Sheep said baaaa!")
    assert search('baa*!', "Sheep said baaaa humbug") == False
    assert match('baa*!', "Sheep said baaaa!") == False
    assert match('baa*!', "baaaaaaaaa! said the sheep")
    assert search('def', 'abcedfg')
    assert search('def$', 'abcdef')
    assert search('def$', 'abcedfg') == False
    assert search('^start', 'not the start') == False
    assert match('start', 'not the start') == False
    assert match('a*b*c*', 'just anything')
