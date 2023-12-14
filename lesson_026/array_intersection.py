find_intersection = lambda arr1, arr2: list(filter(lambda x: x in arr2, arr1))

array1 = [1, 2, 3, 4, 5]
array2 = [4, 5, 6, 7, 8]
intersection = find_intersection(array1, array2)
print(intersection)  # Output: [4, 5]