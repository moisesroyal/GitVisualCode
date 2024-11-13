
my_list = [1,2,3,4]

my_iter = iter(my_list)

print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

limit = 10

odd_itter = iter(range(1,limit+1,2))

for num in odd_itter:
    print(num)

text = "Hola mundo"
iter_text = iter(text)

for char in iter_text:
    print(char)