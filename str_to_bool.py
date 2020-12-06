"""
Модуль содержит функции для приведения строки к типу bool
"""

__all__ = ['str_to_bool']
__author__ = 'Evgenii Romanov'
__version__ = '1.0.0'
__license__ = 'MIT'
__date_created__ = '12/05/2020'

def str_to_bool(str_val):
    """
    Функция конвертирует строку в настоящий bool.

    Правила конвертации:
    =====================
        True (bool) == True, true, T, t, yes, y, 1
        False (bool) == False, false, F, f, no, n, 0

    :param str_val:
    ---------------
        Должна быть строка, содержащая одно из значений
        ('True', 'true', 'T', 't', 'yes', 'y', '1')
        или
        ('False', 'false', 'F', 'f', 'no', 'n', '0')
        При любом другом значении, будет вызвано исключение ValueError
    :return:
    ---------
        Функция возвращает True (тип bool) или False (тип bool)

    Example usage:
    ===============
       -----------------------------------------------------------------------
       |          CMD         |       result      | input type | result type |
       -----------------------------------------------------------------------
       | str_to_bool('True')  | return True       |    str     |    bool     |
       | str_to_bool('False') | return False      |    str     |    bool     |
       | str_to_bool('1')     | return True       |    str     |    bool     |
       | str_to_bool('0')     | return False      |    str     |    bool     |
       | str_to_bool('t')     | return True       |    str     |    bool     |
       | str_to_bool('Tru')   | except ValueError |    str     |             |
       | str_to_bool('asdf')  | except ValueError |    str     |             |
       -----------------------------------------------------------------------

    """

    # Значение, возвращаемое функцией по умолчанию:
    result = None

    t = ('true', 't', 'yes', 'y', '1')  # Значения эквивалентные True.
    f = ('false', 'f', 'no', 'n', '0')  # Значения эквивалентные False.

    if str_val:
        # Без кавычек ('Tru' in 'True') == True. Чтобы такое было
        # невозможно, заключаем значения в экранирующие кавычки,
        # т.е. будет ('"Tru"' in '"True"') == False,
        # но ('"True"' in '"True"') == True.
        q = '\"'
        # Заключаем эквиваленты True в кавычки с помощью генератора:
        t = list(q + x + q for x in t)
        # Заключаем эквиваленты False в кавычки с помощью генератора:
        f = list(q + x + q for x in f)
        str_val = q + str_val + q
        str_val = str_val.lower()

        try:
            if str_val not in t + f:
                # Если значение str_val не имеет эквивалента
                # True или False (в списках t и f), то это значит, что
                # во входном параметре (str_val) ошибка
                # и вызываем исключение:
                raise ValueError
        except ValueError:
            print('Входной параметр функции str_val={0} не имеет эквивалента'
                ' в списках возможных значений для True и False'
                .format(str_val))

        if str_val in t:
            # Входной параметр имеет эквивалент в списке t (True):
            result = True

        if str_val in f:
            # Входной параметр имеет эквивалент в списке f (False):
            result = False

    return result

def main():
    """
    Example of using function str_to_bool
    Примеры использования функции str_to_bool
    """

    res = 'input=\'{0}\', result={1}, type_result={2}'

    # example 1:
    input_val = 'True'
    b = str_to_bool(input_val)
    type_ = type(b)
    print('1. ' + res.format(input_val, b, type_))

    # example 2:
    input_val = 'False'
    b = str_to_bool(input_val)
    type_ = type(b)
    print('2. ' + res.format(input_val, b, type_))

    # example 3:
    input_val = '1'
    b = str_to_bool(input_val)
    type_ = type(b)
    print('3. ' + res.format(input_val, b, type_))

    # example 4:
    input_val = '0'
    b = str_to_bool(input_val)
    type_ = type(b)
    print('4. ' + res.format(input_val, b, type_))

    # example 5:
    input_val = 't'
    b = str_to_bool(input_val)
    type_ = type(b)
    print('5. ' + res.format(input_val, b, type_))

    # example 6:
    # except ValueError:
    print('6.')
    b = str_to_bool('Tru')

    # example 7:
    # except ValueError:
    print('7.')
    b = str_to_bool('asdf')

if __name__ == "__main__":
    main()