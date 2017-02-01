lst = [1, [2, 3], 4, [[6, 7, [5], [[[6, 8]]]]]]
del(lst[1:4])
lst1 = [2, 3, 4, 6, 7, 5, 6, 8]
lst.extend(lst1)
print(lst)
