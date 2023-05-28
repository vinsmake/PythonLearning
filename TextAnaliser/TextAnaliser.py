#the user gives his words
user = input("Tell me your thoughs... ")
#to store letters
letters = []

#to include lower and upper
user = user.lower()

#the user add letters
letters.append(input("add the first letter: ").lower())
letters.append(input("add the second letter: ").lower())
letters.append(input("add the third letter: ").lower())

#We count how many times the letters[] are inside the user
lettersAmountFirst = user.count(letters[0])
lettersAmountSecond = user.count(letters[1])
lettersAmountThird = user.count(letters[2])

#so we print how many times we find that letter
print(f"we have found the letter {letters[0]} {lettersAmountFirst} times")
print(f"we have found the letter {letters[1]} {lettersAmountSecond} times")
print(f"we have found the letter {letters[2]} {lettersAmountThird} times")

#splits the text using space and returns a list of words
words = user.split()
print(f"There are {len(words)} words in your thoughs, nice")

#now we can print them separately
print(f"Also, your first though was {words[0]} and your last though was {words[-1]}, interesting")

#this returns the words in revers as a string
words.reverse()
userInvert = ' '.join(words)
print(f"in revers, it would say {userInvert}, but that's not improtant")

#we search for the word potatoe, and use the dic for every possible situation
findPotetoe = 'potatoe' in user
dicPotatoe = {True:"is", False:"is not"}
print(f"i don't know if you notice, but the word potatoe {dicPotatoe[findPotetoe]} in your thougs")