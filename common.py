latex_template = """
\\documentclass[24pt]{article}

\\usepackage{geometry}
\\usepackage{xcolor}
\\usepackage{amssymb}
\\usepackage{tikz}

\\usepackage{tikz}
\\newcommand{\mysquare}{\\tikz\\draw[draw=blue,thick] (0,0) rectangle (0.4,0.55);}

\\geometry{
    left=0.5in,
    right=0.5in,
    top=0.3in,
    bottom=0.3in
}


\\begin{document}

%s

\\end{document}
"""
