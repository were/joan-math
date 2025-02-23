import random

def generate_lines(n, l, r, line, sep, res):
    line -= 1
    mod = 10 ** sep
    unique =set()
    for i in range(n):
        while True:
            raw = random.randint(l, r)
            if raw not in unique:
                unique.add(raw)
                break
        dump = []
        while raw:
            dump = [(('%0' + str(sep) + 'd') if raw >= mod else '%d') % (raw % mod)] + dump
            raw = raw // mod
        res.append(', '.join(dump) + ' & \\hfill \\\\')
        for j in range(line):
            res.append(' & \\\\')
        res.append('\midrule')

def generate_table(sep):
    res = []
    generate_lines(8, 1, 100, 1, sep, res)
    generate_lines(8, 1000, 10000, 1, sep, res)
    generate_lines(4, 1000000, 100000000, 2, sep, res)
    res.pop()

    res = '\n'.join(res)

    res = f"""
    {{
    \\Large
    \\begin{{tabular}}{{ l|p{{15cm}} }}
    
    \\toprule
    Number & Read \\\\
    \\midrule
    {res}
    \\bottomrule
    
    \\end{{tabular}}
    }}
    """
    return res


english = generate_table(3)
chinese = generate_table(4)

exec(open('../common.py').read())

print(latex_template() % (english + '\\newpage' + chinese))

