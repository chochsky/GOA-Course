def is_second_dimension_list(arr):
    return isinstance(arr, list) and all(isinstance(item, list) for item in arr)
