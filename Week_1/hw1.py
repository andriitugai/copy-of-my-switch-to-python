input_dict = {
    'key1': 72,
    'key2': "intellectual",
    'key3': "o",
    'key4': "space",
    'key5': ['Wine', 'Love', 'Corporation', 'Billboard', 'Cloud']
}


def rule1(ascii_code) -> str:
    '''
    Return symbol which corresponds ASCII code provided
    '''
    return chr(ascii_code)


def rule2(w_str):
    '''
    Return string which consists of symbols ##4 - 6 (included) of the string w_str provided 
    '''
    return ''.join(w_str[4-1:6])


def rule3(val):
    '''
    Return the argument 'as is'
    '''
    return val


def rule4(description):
    '''
    Return symbol which corresponds it's description provided
    and an empty string for unknown description
    '''
    symbols = {
        'space':        ' ',
        'colon':        ':',
        'semicolon':    ';',
        'comma':        ',',
        'period':       '.',
        'dash':         '-',
        'underscore':   '_'
    }
    description = description.lower()
    if description in symbols.keys():
        return symbols[description]
    else:
        return ''


def rule5(word_list):
    '''
    Return string depending on the length of the list provided:
    If the length is even the string contains the first letters of the elements of the list
    If the length is odd the string contains letters, which nubmer is equal to the number of element in the list
    '''
    if len(word_list) % 2 == 0:
        letters = [word[0] for word in word_list]
    else:
        letters = [word[i] for i, word in enumerate(word_list)]

    return ''.join(letters)


def hw_1(input_dict):
    '''
    Return a string as a result of joining values from input_dict according to the rules provided
    '''
    rules = [rule1, rule2, rule3, rule4, rule5]

    values = [rule(input_dict[key])
              for rule, key in zip(rules, input_dict)]

    # joining the values to the result string using values[2] as a separator
    result = values[2].join([values[i] for i in range(len(values)) if i != 2])
    # Change the rule3 to:
    # 3) Use the value of 'key3' "as is"
    res2 = ''.join(values)
    return result, res2


if __name__ == '__main__':
    result, res2 = hw_1(input_dict)
    print(result)
    print(res2)
