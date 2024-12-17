class Unique(object):

    def __init__(self, items, **kwargs):
        self.items = iter(items)
        self.seen = set()
        self.ignore_case = kwargs.get('ignore_case', False)

    def __next__(self):
        while True:
            item = next(self.items)
            if isinstance(item, str) and self.ignore_case:
                processed_item = item.lower()
            else:
                processed_item = item

            if processed_item not in self.seen:
                self.seen.add(processed_item)
                return item

    def __iter__(self):
        return self



def main3():
    data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    print("Пример 1: Список с числами")
    for item in Unique(data1):
        print(item, end=' ')

    import random
    def gen_random(num_count, begin, end):
        return (random.randint(begin, end) for _ in range(num_count))

    data2 = gen_random(10, 1, 3)
    print("\nПример 2: Генератор случайных чисел")
    for item in Unique(data2):
        print(item, end=' ')

    data3 = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    print("\nПример 3: Список со строками без ignore_case")
    for item in Unique(data3):
        print(item, end=' ')

    print("\nПример 4: Список со строками с ignore_case")
    for item in Unique(data3, ignore_case=True):
        print(item, end=' ')


if __name__ == "__main__":
    main3()