OpeningParen = '('
ClosingParen = ')'
Underscore = '_'


def is_end_of_variable(curr_char: chr):
    return not curr_char.isalnum() and curr_char != Underscore


def not_end_of_variable(curr_char: chr):
    return not is_end_of_variable(curr_char)


def is_whitespace(curr_char: chr):
    return curr_char.isspace()


def is_newline(curr_char: chr):
    return curr_char == '\n'


def not_newline(curr_char: chr):
    return not is_newline(curr_char)


if __name__ == '__main__':
    print(is_end_of_variable('x'))
