"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*num, power=2):
    return [x ** power for x in num]
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """

print (power_numbers(1,2,5,7))



# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"

def is_prime(prime):
    if prime >= 2:
        for y in range(2, prime):
            if prime%y == 0:
                return None
        return prime
    else:
        return None



def filter_numbers(*num, fil):
        if fil == 'odd':
            return list(filter(lambda x: x % 2 == 0, *num))
        if fil == 'even':
            return list(filter(lambda x: x % 2, *num))
        if fil == 'prime':
            return list(filter(lambda x: x == is_prime(x), *num))

        """
        функция, которая на вход принимает список из целых чисел,
        и возвращает только чётные/нечётные/простые числа
        (выбор производится передачей дополнительного аргумента)

        >>> filter_numbers([1, 2, 3], ODD)
        <<< [1, 3]
        >>> filter_numbers([2, 3, 4, 5], EVEN)
        <<< [2, 4]
        """

print ("odd",filter_numbers([1,2,3,4,5,6,7,8,9,10,11],fil=ODD))
print ("even",filter_numbers([1,2,3,4,5,6,7,8,9,10,11],fil=EVEN))
print ("prime",filter_numbers([1,2,3,4,5,6,7,8,9,10,11],fil=PRIME))


