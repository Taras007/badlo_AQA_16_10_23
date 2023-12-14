lists = [[1, 2, 3], [4, 5], [6, 7, 8, 9], [10]]
max_min_list = lambda lists: (max(lists, key=len), min(lists, key=len))

max_list, min_list = max_min_list(lists)
print(f"Max list: {max_list}, Min list: {min_list}")