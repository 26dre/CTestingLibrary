OpeningParen = '('
ClosingParen = ')'


def is_end_of_variable(curr_char: chr):
    return curr_char.isspace() or curr_char == OpeningParen or curr_char == OpeningParen


def not_end_of_variable(curr_char: chr):
    return not is_end_of_variable(curr_char)


def is_whitespace(curr_char: chr):
    return curr_char.isspace()


if __name__ == '__main__':
    print(is_whitespace('x'))
