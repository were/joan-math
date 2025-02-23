# Use XeLaTeX to compile, for the compatibility with ctex characters
def latex_template(landscape=False,):
    return """
\\documentclass[24pt]{article}

\\usepackage[%s]{geometry}
\\usepackage{xcolor}
\\usepackage{amssymb}
\\usepackage{tikz}
\\usepackage{ctex}
\\usepackage{booktabs}

\\usepackage{tikz}
\\newcommand{\mysquare}{\\tikz\\draw[draw=blue,thick] (0,0) rectangle (0.4,0.55);}

\\geometry{
    left=0.3in,
    right=0.3in,
    top=0.3in,
    bottom=0.3in
}


\\begin{document}

%%s

\\end{document}
""" % ('landscape' if landscape else '',)
