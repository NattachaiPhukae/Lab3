array = ["A","B","C","E","F"]
print("Unpoped Stack")
print("Address Stack")
for i in range(len(array)):
    print("|   "f"{i}","  |",f"{array[i]}","|")
array.pop()
print("Poped Stack")
print("Address Stack")
for i in range(len(array)):
    print("|   "f"{i}","  |",f"{array[i]}","|")