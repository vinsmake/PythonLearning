#this is a int 
data1 = 10 
#this is a float 
data2 = 7.5


print(data1)
print(data2)


print(type(data1))
print(type(data2))
print(type(data1 + data2))

data3 = data1 + data2*2

print(data3)
print(type(data3))
#we convert the float to an int
data3 = int(data3)
print(data3)
print(type(data3))

age = input("tell me your age ")
age = int(age)
newAge = age + 1

#this is a convertion method
print("cool, you are " + str(age) + " years old, so will be " + str(newAge) + " soon ")
#this is a format function
print("cool, you are {} years old, so will be {} soon ".format(age,newAge))
#this is a literal string
print(f"cool, you are {age} years old, so will be {newAge} soon ")
