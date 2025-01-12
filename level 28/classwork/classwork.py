def manual_index(main_string, search_string):
    if search_string in main_string:
        return main_string.index(search_string)
    else:
        return -1
