
# def alter_file(path_to_file: str):
#     ...

from io import _WrappedBuffer, TextIOWrapper
from typing import Any, Callable


one_line_comment_sequence = '//'
public_letter: chr = None
read_last_letter: bool = True
# wrote_last_letter: bool = False
continue_writing: bool = True


def write_letter(file: TextIOWrapper[_WrappedBuffer]):
    global public_letter, read_last_letter
    while (continue_writing):

        match read_last_letter:
            case False:
                file.write(public_letter)
                read_last_letter = False
            case _:
                continue


def write_letter_simple(file: TextIOWrapper, letter: chr):
    file.write(letter)


# def read_file_simple(read_file: TextIOWrapper[_WrappedBuffer], write_file: TextIOWrapper):
#     while (curr_letter := read_file.read(1)) != None:
#         match curr_letter:
#             case '/':

#                 ...
#             case _:
#                 if curr_letter.isalnum() or curr_letter == '(' or curr_letter == ')':
#                     write_letter_simple(write_file, curr_letter)

#         ...

def consume_while(read_file: TextIOWrapper, fn: Callable[[chr], bool]):
    while (curr_letter := read_file.read(1)) != None and fn(curr_letter):
        continue

    if curr_letter != None:
        read_file.seek(-1, 1)


def handle_single_line_comment(file: TextIOWrapper):
    ...


def handle_multi_line_comment(file: TextIOWrapper):
    ...


def clean_file(path_to_file: str):
    with open(path_to_file, 'r+') as reading_file, open('cleaned_file.c', 'a+') as writing_file:
        ...


if __name__ == '__main__':
    ...
