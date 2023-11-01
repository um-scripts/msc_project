in_file = open('SJout_ALL.csv', 'r')
head = in_file.readline()

DATA = dict()
UNQ = dict()

L = 0
for l in in_file.readlines():
    lc = l.split(',')
    k = tuple(lc[:3])
    if k not in DATA:
        UNQ[k] = L + 2
        DATA[k] = l
    else:
        print("Found duplicate at line:", L+2, "\tPrevious occurrence at line:", UNQ[k])
    L += 1

out_file = open('NoRepetition_SJout_ALL.csv', 'w')
print("Number of records in original file:", L)
print("Found Unique records:", len(DATA.keys()))
print("Saving the file as:", out_file.name)

out_file.write(head)
for v in DATA.values():
    out_file.write(v)

in_file.close()
out_file.close()