import sys
import math


def get_coef(index, prompt) -> float:
    try:
        try:
            coef_str = sys.argv[index]
            coef = float(coef_str)
            return coef
        except ValueError:
            pass
    except:
        while True:
            try:
                print(prompt)
                coef_str = input()
                coef = float(coef_str)
                return coef
            except ValueError:
                pass


def get_roots(a, b, c) -> list:
    result = []
    D = b * b - 4 * a * c
    if D == 0.0:
        root = -b / (2.0 * a)
        result.append(root)
    elif D > 0.0:
        sqD = math.sqrt(D)
        root1 = (-b + sqD) / (2.0 * a)
        root2 = (-b - sqD) / (2.0 * a)
        result.append(root1)
        result.append(root2)

    return result


def main():
    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
    roots = get_roots(a, b, c)

    count = 0
    for el in roots:
        if el > 0:
            count += 1

    finally_roots = []
    for el in roots:
        if el > 0 or el == 1:
            finally_roots.append(math.sqrt(el))
            finally_roots.append(-1 * math.sqrt(el))
        elif el == 0:
            finally_roots.append(el)

    len_roots = len(finally_roots)
    if len_roots == 0:
        print('Корней нет')
    elif len_roots == 1:
        print(f'Один корень: {abs(finally_roots[0])}')
    elif len_roots == 2:
        print('Два корня: {} и {}'.format(finally_roots[0], finally_roots[1]))
    elif len_roots == 3:
        print('Три корня: {} и {} и {}'.format(finally_roots[0], finally_roots[1], finally_roots[2]))
    else:
        print('Четыре корня: {} и {} и {} и {}'.format(finally_roots[0], finally_roots[1], finally_roots[2],
                                                       finally_roots[3]))


if __name__ == "__main__":
    print('\n============ LAB-01 ============\n')
    main()
    print('\n================================\n')