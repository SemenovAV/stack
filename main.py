from stack import Stack


def check_brackets(brackets, pairs):
    """
    Проверяет сбалансированность строк.
    :param brackets: str - сторока для проверки
    :param pairs: dict - словарь в формате: {'Открывающий символ': 'Закрывающий символ'}
    :return: bool

    """
    if len(brackets) % 2 != 0:
        return False
    else:
        stack = Stack()
        for bracket in brackets[::-1]:
            if not stack.size or not stack.peek() or stack.peek() != pairs.get(bracket):
                stack.push(bracket)
            else:
                stack.pop()
    return stack.is_empty()


if __name__ == '__main__':
    PAIRS = {
        '[': ']',
        '{': '}',
        '(': ')',
        '<': '>',
    }
    test_data = [
        '(((([{}]))))',
        '[([])((([[[]]])))]{()}',
        '{{[()]}}',
        '}{}',
        '{{[(])]}}',
        '[[{())}]',
    ]
    for data in test_data:
        print('Сбалансировано' if check_brackets(data, PAIRS) else 'Несбалансировано')
