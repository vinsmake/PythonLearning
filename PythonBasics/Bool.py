myBoolean = True
print(type(myBoolean))
print(myBoolean)

#we can know if something is true with the booleans
answer = 5 > 2+3
answer2 = 5 == 2+3
answer3 = bool(5==2+3)
print(answer)
print(answer2)
print(answer3)

myList = [1,2,3,4]
control = 5 in myList
print(control)
control = 5 not in myList
print(control)