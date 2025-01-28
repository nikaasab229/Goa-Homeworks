def remove_one_element(lst, index):
    if 0 <= index < len(lst):
        lst.pop(index)
    print(lst)

remove_one_element([10, 20, 30, 40, 50], 2)
def remove_elements_by_indexes(main_list, indexes_list):
    for index in sorted(indexes_list, reverse=True):
        if 0 <= index < len(main_list):
            main_list.pop(index)
    return main_list

main_list = [10, 20, 30, 40, 50]
indexes_list = [1, 3]
result = remove_elements_by_indexes(main_list, indexes_list)
print(result)
def remove_one_element(lst, index):
    if 0 <= index < len(lst):
        lst.pop(index)
    print(lst)

remove_one_element([10, 20, 30, 40, 50], 2)
