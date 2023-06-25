def my_function():
    """ 
    This excecutes this
    """
    print("Hello, this is my function")

my_function()

z = 200
y = 100
def myfunc():
    global y
    z = 700
    y = 500

myfunc()
print(y)
print (z)