def field(items, *args):
    assert len(args) > 0
    if len(args) == 1:
        key = args[0]
        for item in items:
            value = item.get(key)
            if value is not None:
                yield value
    else:
        for item in items:
            filtered = {key: item.get(key) for key in args if item.get(key) is not None}
            if filtered:
                yield filtered

def main1():

    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
    ]

    print("Тест с одним аргументом 'title':")
    for value in field(goods, 'title'):
        print(value)

    print("\nТест с несколькими аргументами 'title', 'price':")
    for item in field(goods, 'title', 'price'):
        print(item)

if __name__ == "__main__":
    main1()