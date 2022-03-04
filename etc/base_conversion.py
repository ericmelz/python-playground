"""
Convert a decimal integer to a different base

E.g., 15 base 2 => 1111
"""


def base_convert(num, base):
    digits = []
    while num > 0:
        digit = num % base
        digits.append(str(digit))
        num //= base
    return ''.join(reversed(digits))


def test1():
    print(f'Test1: {base_convert(15, 2)}')


def test2():
    print(f'Test2: {base_convert(17, 2)}')


def test3():
    print(f'Test3: {base_convert(19, 2)}')


def test4():
    print(f'Test4: {base_convert(23, 2)}')


def test5():
    print(f'Test5: {base_convert(23, 7)}')


if __name__ == '__main__':
    test1()
    test2()
    test3()
    test4()
    test5()


"""
Simulation

10: 15 > 0 => true
11: digit = 15 % 2 = 1
12: digits = [1]
13: num = 15 // 2 = 7

10: 7 > 0 => true
11: digits = 7 % 2 = 1
12: digits = [1 1]
13: num = 7 // 2 = 3

10: 3 > 0 => true
11: digits = 3 % 2 = 1
12: digits = [1 1 1]
13: num = 3 // 2 = 1

10: 1 > 0 => true
11: digits = 1 % 2 = 0
12: digits = [1 1 1 1]
14: num = 1 // 2 = 0

10: 0 > 0 => false
14: ''.join([1 1 1 1]) => 1111 

"""