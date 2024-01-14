import copy
list1 = [1,2,3,4]
list2 = list1
#In Shallow Copy We are copying the whole list into the another list and when we append any value into the list it will also reflect into the another list.
#This is the problem in shallow copy that change in one list will affect the other list also, ie. Pass By Reference
print(id(list2))
print(id(list1))

list2.append(5)
print(list1)
print(list2)

#deep copy

list3 = copy.deepcopy(list2)
list3.append(6)
print(list3)
print("-------------Original List post deep copy-----------")
print(list2)
