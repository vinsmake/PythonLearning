#list can contain any type of data
ni = ['vins', 1, 'sehu', 2, 'kai', 3]

#lenght of the list
print(len(ni))

# number 2 (sehu) object inside the string
print(ni[2])

#prints only 2 elements from 0 forward
print(ni[0:2])

#replace de 0 element
ni[0] = 'vinsmake'
print(ni)

#add an element at the end
ni.append('sake')
ni.append( 4)
print(ni)

#removes an element
ni.append('natu')
print(ni)
ni.pop()
print(ni)


id = ['b','c','a']

#sorts the list, can't create a variable of the sorted list.
id.sort()
print(id)

#reverses the list, can't create a variable of the sorted list.
id.reverse()
print(id)