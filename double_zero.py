def double_zero(amount):
    try:
        amount = int(amount)
    except ValueError:
        print('Amount must be a number')
        return

    if amount < 1:
        print('List must contain at least 1 element')
        return

    try:
        list = [int(input(f'Enter number #{i + 1}: ')) for i in range(amount)]
    except ValueError:
        print('Invalid value')
        return

    double_zero_list = []

    for i in range(len(list)):
        if list[i] == 0:
            double_zero_list += [list[i]] * 2
        else:
            double_zero_list += [list[i]]

    print(f'Original list: {list} -> Double zero list: {double_zero_list}')
    return double_zero_list

if __name__ == '__main__':
    double_zero(input('Enter amount of numbers: '))