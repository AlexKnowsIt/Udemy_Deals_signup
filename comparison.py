list1 = [1,2,3,4,5]
list2 = [1,3,5,7,9]

listcomp1 = list(set(list1).difference(list2))
print(listcomp1)