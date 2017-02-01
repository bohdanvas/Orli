lst = [1, [2, 3], 4, [[6, 7, [5], [[[6, 8]]]]]]
del(lst[1])
lst.insert( 1, 2)
lst.insert( 2, 3)
del(lst[4])
lst1 = [6, 7, 5, 6, 8]
lst.extend(lst1)
print(lst)
