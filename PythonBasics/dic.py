dic = {'01':'vinsmake', '02':'mugui', '03':'zoro'}
print(dic)

#prints the data of the id 03
print(dic['03'])

#dic can be created by diferent type of data
cli = {'name':'vinsmake', 'document':2456, 'age':23}
print(cli['name'])


inx = {'doc':100,
       'id':[1,2,3],
       'cty':{'a1':'gdl',
             'b1':'mty',
             'c1':'zpn'}}

#prints doc
print(inx['doc'])

#prints the third id
print(inx['id'][2])

#prints mty
print(inx['cty']['b1'])

#prints mty in upper
print(inx['cty']['b1'].upper())

#adds the cty of tlq
inx['cty']['d1'] = 'tlq'
print(inx['cty']['d1'].upper())

#prints only keys
print(inx.keys())
#prints only values
print(inx.values())
#prints all the data
print(inx.items())