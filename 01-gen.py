import random

res = []

raw = list(range(1, 10))

selected = set()

for i in range(30):
    while True:
        x = random.choice(raw)
        y = random.choice(raw)
        if x + y < 11:
            continue
        if (x, y) in selected:
            continue
        selected.add((x, y))
        break

    expr = f'${x} + {y} = ?$ & ${x} + {{\\color{{red}} \\square}} = 10$ & ${{\\color{{red}} \square}} + {{\color{{blue}} \square}}={y}$ & ${x} + {y} = 1$\mysquare\\\\'

    res.append(expr)

res = '\n'.join(res)

latex_table = f"""
{{
\huge
\\begin{{tabular}}{{p{{4cm}}p{{4cm}}p{{4cm}}p{{4cm}}}}

{res}

\\end{{tabular}}
}}
"""

exec(open('./common.py').read())

print(latex_template % latex_table)

