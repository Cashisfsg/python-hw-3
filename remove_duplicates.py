def remove_duplicates(amount):

    try:
        amount = int(amount)
    except ValueError:
        print('Amount must be a number')
        return

    if amount < 1:
        print('List must contain at least 1 element')
        return

    try:
        list = sorted([int(input(f'Enter number #{i + 1}: ')) for i in range(amount)])
    except ValueError:
        print('Invalid value')
        return

    filtered_list = []

    for i in list:
        if i not in filtered_list:
            filtered_list.append(i)

    print(f'Sorted list: {list} -> Filtered list: {filtered_list}')
    return filtered_list

if __name__ =='__main__':
    remove_duplicates(input('Enter amount of numbers: '))