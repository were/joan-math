import operator


def generate_table(op, mn):
    raw = list(range(1, 10))
    
    expr = []
    for i in range(1, 10):
        expr.append([])
        for j in range(1, 10):
            if j >= i:
                expr[-1].append('$%d %s %d = %d$' % (i, mn, j, op(i, j)))
            else:
                expr[-1].append('')
    
    rows = []
    
    for i in range(9):
        rows.append(' & '.join(expr[j][i] for j in range(9)))
    
    rows = '\\\\\n'.join(rows)
    
    
    col = 'p{2.5cm}' * 9
    
    res = f"""
    {{
    \\begin{{tabular}}{{ {col} }}
    
    {rows}
    
    \\end{{tabular}}
    }}
    """
    return res

add_table = '\\section{加法表}\n' + generate_table(operator.add, '+')
mul_table = '\\section{乘法表}\n' + generate_table(operator.mul, '\\times')

exec(open('../common.py').read())

content = add_table + mul_table
content = '{\n \large\n' + content + '\n}'

print(latex_template(landscape=True) % content)

