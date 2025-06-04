def find_mine(field):
    for row_index, row in enumerate(field):
        for col_index, value in enumerate(row):
            if value == 1:
                return [row_index, col_index]
    return None
