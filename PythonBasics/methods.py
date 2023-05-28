text = 'this is a normal text, created by me'

#uppercase the string
print(text.upper())

#uppercase the first letter of the string
print(text[0].upper())

#creates a list of every word 
print(text.split())

#creates a list of every word, separated by coma ','
print(text.split(','))

#joins every word, separed by space
name = 'Enrique'
last = 'Plascencia'
ocup = 'developer'
print(" ".join([name, last, ocup]))

#gives the location of the first s, if is not there, answer is -1
print(text.find('s'))

#replace all the 'me' for 'vinsmake'
print(text.replace('me','Vinsmake'))


word = """This is writed
in the same print"""

#if "writed" is inside word, true
print("writed" in word)
#if "writed" is not inside word, true
print("writed" not in word)

#lenght of the string
print(len(word))