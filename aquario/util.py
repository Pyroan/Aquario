
class Vector2():
    def __init__(self, x, y):
        self.x = x
        self.y = y

def reflected(s: str):
    ''' returns the reflected version of the
    given string (not the same as reversed)
    '''
    reflections = {
        '\\': '/',
        '/': '\\',
        '>': '<',
        '<': '>',
        '[': ']',
        ']': '[',
        '{': '}',
        '}': '{',
        '(': ')',
        ')': '(',
    }
    s = list(s)
    for i in range(len(s)):
        if s[i] in reflections:
            s[i] = reflections[s[i]]
    return ''.join(s[::-1]) # reversed