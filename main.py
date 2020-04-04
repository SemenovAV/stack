from stack import Stack


def check_brackets(brackets, pairs):
    if len(brackets) % 2 != 0:
        return 'Несбалансировано'
    else:
        stack = Stack()
        for bracket in brackets[::-1]:
            if stack.size == 0 or not stack.peek() or stack.peek() != pairs.get(bracket):
                stack.push(bracket)
            else:
                stack.pop()
    return 'Сбалансировано' if stack.is_empty() else 'Несбалансировано'


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
        print(check_brackets(data, PAIRS))
