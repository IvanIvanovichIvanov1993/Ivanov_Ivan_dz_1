src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = set()
other_set = set()
for el in src:
   if el not in other_set:
       result.add(el)
   else:
       result.discard(el)
   other_set.add(el)
print(result)
a = [el for el in src if el in result]
print(a)