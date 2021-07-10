'''
A set is a collection which is both unordered and unindexed.
A set is unchangeable, and do not allow duplicate values , this means Once a set is created,
you cannot change its items, but you can add new items.

Sets are written with curly brackets.

Duplicate values will be ignored
'''

set1={'abc',1,2,3,"PRATEEK"}
print(type(set1))
print(set1)

set2 = set(("apple", "banana", "cherry"))
print(set2)
print("banana"in set2)

set3 = {"apple", "banana", "cherry"}
set3.add(1) #Since set is unordered it will add the element to a new index location each time we user add function
print(set3)


'''
Add Sets
To add items from another set into the current set, use the update() method.
We can also add items from a list to a current set using update() method
'''

set4={"apple", "banana", "cherry" ,"mango"}
set5={"kiwi","strawberry","pineapple"}
set5.update(set4)
print(set5)

set6={"kiwi","strawberry","pineapple","pineapple"}
list=[1,2,3,"abc"]
set6.update(list)
print(set6)

'''
Python - Remove Set Items
remove()-: If the item to remove does not exist, remove() will raise an error.
discard()-: If the item to remove does not exist, discard() will NOT raise an error.
pop()-: pop() method to remove an item, but this method will remove the last item. Remember that sets are unordered, 
so you will not know what item that gets removed.
'''

'''
SET INTERSECTION
The union() method returns a new set with all items from both sets:

The update() method inserts the items in set2 into set1:

The intersection_update() method will keep only the items that are present in both sets.

The intersection() method will return a new set, that only contains the items that are present in both sets.

The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.

The symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets.

'''
set7={"kiwi","strawberry","pineapple"}
set7.pop()
print(set7)