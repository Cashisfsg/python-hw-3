def double_zero(lst):

    double_zero_list = []

    for i in range(len(lst)):
        if lst[i] == 0:
            double_zero_list += [lst[i]] * 2
        else:
            double_zero_list += [lst[i]]

    print(f'Original list: {lst} -> Double zero list: {double_zero_list}')
    return double_zero_list

if __name__ == '__main__':
    double_zero([0, 0])