text = 'This is a test'

#gives the number 2(i) and -2 (s) from right to left doesn't starts with 0
print(text[2], text[-2])

#gives the position of the first s
print(text.index("s"))

#gives the position of the first 's' starting from number 4
print(text.index('s',4))

#gives the position of the first 's' starting from number 4 and ending in number 8, this means between the 4 and 8 letter
print(text.index('s',4,8))

#gives the first s from end to start
print(text.rindex('s'))

