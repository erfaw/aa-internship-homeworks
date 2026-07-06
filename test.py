sample_list = [3, 2, 1, 4]


def selection_sort(list: list) -> list:
    for e in list:
        try:
            int(e)
        except ValueError:
            list[list.index(e)] = ord(e)
    
    for i in range(len(list)-1, -1, -1): 
        minimum_element = list[i] 
        for e in list: 
            if e < minimum_element:
                minimum_element = e 
            else: 
                continue

        min_index = list.index(minimum_element) 
        list[i], list[min_index] = list[min_index], list[i] 
    return list

print(selection_sort(sample_list))
