
input_dict = {
    'key1': 72,
    'key2': "intellectual",
    'key3': "o",
    'key4': "space",
    'key5': ['Wine', 'Love', 'Corporation', 'Billboard', 'Cloud']
}

symbols = {
    'space':        ' ',
    'colon':        ':',
    'semicolon':    ';',
    'comma':        ',',
    'period':       '.',
    'dash':         '-',
    'underscore':   '_'
}


def main():
    rules = [
        lambda x: chr(x),
        lambda word: word[4-1:6],
        lambda val: val,
        lambda description: symbols[description] if description in symbols else '',
        lambda w_lst: ''.join([word[len(w_lst) % 2 == 1 and idx or 0]
                               for idx, word in enumerate(w_lst)])
    ]

    print(''.join([rule(input_dict[key])
                   for rule, key in zip(rules, input_dict)]))


if __name__ == '__main__':
    main()
