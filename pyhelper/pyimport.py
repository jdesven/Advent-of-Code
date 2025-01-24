import re

def file_to_str(path):
    with open(path, 'r') as file:
        raw_str = file.read()
    return raw_str

def lines_to_list(file: str, cast = str, read_file = True, regex = ''):
    raw_str = file_to_str(file) if read_file == True else file
    return [list(map(cast, [line]))[0] if regex == '' else list(map(cast, [''.join(re.findall(regex, line))]))[0] for line in raw_str.splitlines()]

def seperator_to_list(file: str, seperator = '' , cast = str, read_file = True):
    raw_str = file_to_str(file) if read_file == True else file
    if seperator != '':
        raw_str = raw_str.split(seperator)
    return [element if cast == str else list(map(cast, [element]))[0] for element in raw_str]

def lines_to_list_of_list(file: str, seperator = '', cast = str, regex = ''):
    return [seperator_to_list(line, seperator = seperator, cast = cast, read_file = False) for line in lines_to_list(file, regex = regex)]

def grid_to_complex_set(file: str, relevant_chars: set):
    lines = lines_to_list(file)
    output_set = set()
    for i_line, line in enumerate(lines):
        for i_char, char in enumerate(line):
            if char in relevant_chars:
                output_set.add(i_line * 1j + i_char)
    return output_set