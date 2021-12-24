from random import choice
def dnk(n, m):
    data = {}
    for _ in range(n):
        s = "".join(choice("cgta") for _ in range(m))
        a = s.count('a') / len(s)
        c = s.count('c') / len(s)
        t = s.count('t') / len(s)
        g = s.count('g') / len(s)
        gc = (s.count('g') + s.count('c')) / len(s)
        data[s] = (f'a - {a}%', f'c - {c}%', f'g - {g}%', f't - {t}%', f'gc - {gc}%')
    return data
