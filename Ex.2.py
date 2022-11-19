array = ["A","B","C","E","F"]
print("Unpoped Stack")
print("Address Stack")
for i in range(len(array)):
    print("|   "f"{i}","  |",f"{array[i]}","|")
array.pop()
array.pop()
array.pop()
array.pop()
array.pop()
array.append("F")
array.append("E")
array.append("C")
array.append("B")
array.append("A")
print("Poped Stack")
print("Address Stack")
for i in range(len(array)):
    print("|   "f"{i}","  |",f"{array[i]}","|")