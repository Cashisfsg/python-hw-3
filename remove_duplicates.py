def remove_duplicates(lst):

    filtered_list = []

    for i in lst:
        if i not in filtered_list:
            filtered_list.append(i)

    print(f'Sorted list: {lst} -> Filtered list: {filtered_list}')
    return filtered_list

if __name__ =='__main__':
    remove_duplicates([1, 1, 1, 2, 3, 3, 4])