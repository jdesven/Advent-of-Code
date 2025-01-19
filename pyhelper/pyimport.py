def file_to_str(path):
    with open(path, 'r') as file:
        raw_str = file.read()
    return raw_str

def lines_to_list(file: str, seperator = '', cast = str, read_file = True):
    raw_str = file_to_str(file) if read_file == True else file
    if cast == int:
        input = [int(line) for line in raw_str.splitlines()]
    else:
        if seperator == '':
            input = [line for line in raw_str.splitlines()]
        else:
            input = [line.split(seperator) for line in raw_str.splitlines()]
    return input

def seperator_to_list(file: str, seperator = '' , cast = str, read_file = True):
    raw_str = file_to_str(file) if read_file == True else file
    if seperator != '':
        raw_str = raw_str.split(seperator)
    if cast == int:
        input = [int(element) for element in raw_str]
    else:
        input = [element for element in raw_str]
    return input