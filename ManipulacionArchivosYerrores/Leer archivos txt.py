file = open ('./moises.txt')

#print(file.read())

#print(file.readline())
#print(file.readline())
#print(file.readline())

for line in file:
    print(line)

file.close()


with open ('./moises.txt') as file:
    for line in file:
        print(line)
        
        #cierra de manera automatica
        