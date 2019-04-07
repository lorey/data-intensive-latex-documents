from collections import OrderedDict

from jinja2 import Environment


def escape_latex(latex):
    escaped_latex = latex

    # ordered dict to make sure backslash comes first
    special_replacements = OrderedDict()
    special_replacements['\\'] = '\\textbackslash'
    special_replacements['~'] = '\\textasciitilde'
    special_replacements['^'] = '\\textasciicircum'

    for char, replacement in special_replacements.items():
        escaped_latex = escaped_latex.replace(char, replacement)
    print(escaped_latex)

    escape_chars = ['&', '%', '$', '#', '_', '{', '}']
    for char in escape_chars:
        escaped_latex = escaped_latex.replace(char, '\\' + char)
    print(escaped_latex)
    return escaped_latex


def create_jinja_env():
    """
    Returns a latex-compliant jinja-environment
    :return: environment
    """
    env = Environment(block_start_string='\BLOCK{', block_end_string='}', variable_start_string='\VAR{',
                    variable_end_string='}', comment_start_string='\#{', comment_end_string='}',
                    line_statement_prefix='%-', line_comment_prefix='%#', trim_blocks=True, autoescape=False, )
    env.filters['to_latex'] = escape_latex
    return env
