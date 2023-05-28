my_tuple = (1,2,3,4)

#tuples can be called as with the index
print(my_tuple[0])
print(my_tuple[-1])

#we can add tuples inside tuples and call it
my_tuple = (1,2,3,(10,20,30),4)
print(my_tuple[3][1])

#we can cast it if's nessesary
my_list = list(my_tuple)
print(type(my_list))

#we can convert the tuple valors into variables.
my_tuple = (10,20,30,40)
w,x,y,z = my_tuple
print(w,x,y,x)

my_tuple = (10,20,10,30)
#We can count
print(my_tuple.count(10))
#And we can find
print(my_tuple.index(20))