table = [[],[],[],[],[],[],[],[],[],[]]
def hash_function(name):
    total = 0
    for i in range(len(name)):
        total+=(ord(name[i]))
    return (total%10)
def add(name):
    index = hash_function(name)
    table[index].append(name)

add("Tim")
add("Peony")

print(table)