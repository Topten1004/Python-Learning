thisset = {"apple", "banana", "cherry"}
print(thisset)


set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

set1 = {"apple", "banana", "cherry"}
set2 = {1,2,3}

set3 = set1.union(set2)

print(set3)

