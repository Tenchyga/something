# Файл представляет из себя совокупность разных функций
# для постановления их приоритета выше основной програмы

def sorter(lst):
    new_lst = []
    for element in lst:
        if element not in new_lst:
            new_lst.append(element)
    return new_lst
