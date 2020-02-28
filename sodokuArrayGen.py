#https://www.kaggle.com/bryanpark/sudoku
input = "004300209005009001070060043006002087190007400050083000600000105003508690042910300"
input = "864371259325849761971265843436192587198657432257483916689734125713528694542916378"
print(len(input))


count =0

for i in range(0, 81):
    if i == 0:
        print("[", end="")
    count += 1
    print(input[i], end="")
    if count % 9 != 0 or count == 0:
        print(",", end="")
    if count % 9 == 0 and count != 0 and count != 81:
        print("],\n[", end="")
    elif count == 81:
        print("]", end="")











