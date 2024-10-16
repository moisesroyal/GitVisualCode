print('Operaciones de conjunto')
set_countries = {'col','mex','bol'}
print(set_countries)
print(type(set_countries))

set_numbers = {1,2,2,443,23}
print (set_numbers)

set_types = {1, 'moises', False, 16.5}
print(set_types)

set_from_string = set('moises')
print(set_from_string)

set_from_tuples = set(('abc', 'va', 'cde', 'eb', 'abc'))
print (set_from_tuples)

numbers = [1,2,4,3,1,2,3,3,4,1]
set_numbers = set(numbers)
print (set_numbers)
unique_numbers = list(set_numbers)
print (unique_numbers)

print('Modificacion de conjunto')
size = len(set_countries)
print(size)
print('col' in set_countries)
print('pe' in set_countries)

#add
set_countries.add('pe')
print(set_countries)
set_countries.add('pe')
print(set_countries)

#update
set_countries.update({'ar','ecua','pe'})
print(set_countries)

#remove

set_countries.remove('col')
print(set_countries)
set_countries.remove('ar')
# discard
set_countries.discard('arg')
print(set_countries)
set_countries.add('arg')
print(set_countries)

set_countries.clear()
print(set_countries)

print(len(set_countries))

print('Operaciones con conjunto')

set_a = {'col','mex','bol'}
set_b = {'pe','bol'}
set_c = set_a.union(set_b) 
print(set_c)
print(set_a | set_b)
set_c = set_a.intersection(set_b)
print(set_c)
print(set_a & set_b)

set_c = set_a.difference(set_b)
print(set_c)
print(set_a - set_b)


set_c = set_a.symmetric_difference(set_b)
print(set_c)
print(set_a ^ set_b)