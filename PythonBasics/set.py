#There are two ways for declaring a set. In the first one, we use the word Set, and (), inside this, we can use (),[] or {}
my_set = set([1,2,3,4,5])
print(type(my_set))
print(my_set)
#in the orther one, we just use {}
set = {1,2,3,4,5}
print(type(set))
print(set)

#if there is a 2 in set, true
print(2 in my_set)

#we can union the sets, but it will delete repeated valors
set1 = {1,2,3}
set2 = {3,4,5}
set3 = set1.union(set2)
print(set3)

#we can add valors
set3.add(6)
print(set3)
#and discard it
set3.discard(6)
print(set3)
#we can use remove, but if the element doesnt exist, it will return an error, discard in the other hand, will just don't remove anything
set3.remove(5)
print(set3)
#we can also remove everything from the set
set3.clear
print(set3)