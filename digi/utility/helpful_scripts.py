import persian


def fixing_numbers(number):
    res = ''.join(number.split(','))
    return persian.convert_fa_numbers(res)
