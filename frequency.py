word = " "
lst = []

frlst = [["the", 0], ["be", 0], ["to", 0], ["of", 0], ["and", 0], ["in", 0], ["a", 0], ["that", 0], ["have", 0], ["i", 0]]

while(word != "quit"):
    print("enter some text")
    word = input().lower()

    if(word == "quit"):
        break
    else:
        lst.extend(word.split())

lst.sort()

for y in range(len(frlst)):
    for items in lst:
        if(items == frlst[y][0]):
            frlst[y].insert(1, frlst[y][1]+1)
            frlst[y].pop(2)

print("\nTotal words: " + str(len(lst)))
print("{:^60}".format("Word frequency of top ten words"))
print("-"*60)

for y in range(len(frlst)):
    print("{:^6}".format(frlst[y][0]), end='')
print()
for y in range(len(frlst)):
    print("{:^6}".format(frlst[y][1]), end='') 