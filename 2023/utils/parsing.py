

def parse(s, code):
    return _parse(s.strip(), code)[0]

def _parse(s, code):
    '''
    input
    s: relevant part of the input string
    code: suffix of the entire code string
    output
    (content, rest_index)
    content: parse result
    rest_index: index in code where to continue
    '''
    if code[0] == 's':
        return s, 1
    elif code[0] == 'i':
        return int(s), 1
    di = 1  # delimiter index
    while not code[di].isdigit():
        di += 1
    delim, n, ncode = code[:di], int(code[di]), code[di+1:]
    split = s.split(delim)
    if n == 1:
        content1, rest_i = _parse(split[0], ncode)
        return [content1] + [_parse(part, ncode)[0] for part in split[1:]], di+1+rest_i
    # n >= 2
    content = []
    rest_i = di+1
    for part in split:
        part_content, intermediate_rest_i = _parse(part, ncode)
        content.append(part_content)
        rest_i += intermediate_rest_i
        ncode = ncode[intermediate_rest_i:]
    return content, rest_i

