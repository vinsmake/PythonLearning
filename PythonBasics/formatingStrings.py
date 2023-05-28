age = input("tell me your age ")
age = int(age)
newAge = age + 1

#this is a convertion method
print("cool, you are " + str(age) + " years old, so will be " + str(newAge) + " soon")
#this is a format function
print("cool, you are {} years old, so will be {} soon".format(age,newAge))
#this is a literal string
print(f"cool, you are {age} years old, so will be {newAge} soon")

