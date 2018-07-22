
def search(pattern, text):
    "Return True if pattern appears anywhere in text"
    if pattern.startswith('^'):
        # pattern must occur at start of text
        return match(pattern[1:], text)
    else:
        # pattern can occur anywhere in the text
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
    assert match('x?', 'text')
    assert match('text?', 'text')
    assert match('text?', 'tex')

    def words(text): return text.split()
