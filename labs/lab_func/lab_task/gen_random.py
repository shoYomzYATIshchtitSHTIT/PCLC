import random

def gen_random(num_count, begin, end):
    """
    Рандомные числа
    :param num_count: число случайных чисел
    :param begin: с какого числа
    :param end: по какое
    :return: картеж чисел
    """
    return (random.randint(begin, end) for _ in range(num_count))


def main2():
    print("Пример вывода gen_random(5, 1, 3):")
    for number in gen_random(5, 1, 3):
        print(number, end=' ')


if __name__ == "__main__":
    main2()