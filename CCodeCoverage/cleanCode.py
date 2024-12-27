
# def alter_file(path_to_file: str):
#     ...

from io import _WrappedBuffer, TextIOWrapper


one_line_comment_sequence = '//'
curr_letter: chr = None


def drop_letter(file: TextIOWrapper[_WrappedBuffer], letter: chr):
    file.write(letter)


def read_file(file: TextIOWrapper[_WrappedBuffer]):
    while (curr_letter := file.read(1)) != None:
        ...


def handle_single_line_comment(file: TextIOWrapper):
    ...


def handle_multi_line_comment(file: TextIOWrapper):
    ...


def clean_file(path_to_file: str):
    with open(path_to_file, 'r+') as reading_file, open('cleaned_file.c', 'a+') as writing_file:
        ...


if __name__ == '__main__':
    ...
