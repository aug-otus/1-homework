"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*num, power=2):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [x ** power for x in num]



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



def filter_numbers(num, fil):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if fil == ODD:
        return list(filter(lambda x: x % 2 and x > 0, num))
    if fil == EVEN:
        return list(filter(lambda x: x % 2 == 0 and x > 0, num))
    if fil == PRIME:
        return list(filter(is_prime, num))



if __name__ == "__main__":
    print ("power",power_numbers(1,2,5,7))
    print ("odd",filter_numbers([-1,0,1,2,3,4,5,6,7,8,9,10,11],ODD))
    print ("even",filter_numbers([-1,0,1,2,3,4,5,6,7,8,9,10,11],EVEN))
    print ("prime",filter_numbers([-1,0,1,2,3,4,5,6,7,8,9,10,11],PRIME))


