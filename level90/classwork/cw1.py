def is_every_element_list(arr):
    return all(isinstance(el, list) for el in arr)
