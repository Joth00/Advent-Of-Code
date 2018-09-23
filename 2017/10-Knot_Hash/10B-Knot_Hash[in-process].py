def switch(mylist):
    endlist = list()
    for i in range(1, len(mylist)+1):
        endlist.append(mylist[-i])
    return endlist


def select(mystart, mylen, mylist):
    size = len(mylist)
    crnt = mystart
    selection = list()
    for _x in range(mylen):
        if crnt >= size:
            crnt %= size
        selection.append(mylist[crnt])
        crnt += 1
    return selection


def replace(myrepl, mystart, mylist):
    size = len(mylist)
    crnt = mystart
    for x in myrepl:
        if crnt >= size:
            crnt %= size
        mylist[crnt] = x
        crnt += 1
    return mylist


inpt = '199,0,255,136,174,254,227,16,51,85,1,2,22,17,7,192'
lengths = list(map(int, inpt.split(',')))
lst = list(range(256))

skip = 0
crnt = 0

for x in lengths:
    if x <= len(lst):
        print('== V == VALID LENGTH')
        lst = replace(switch(select(crnt, x, lst)), crnt, lst)
        crnt += x + skip
        skip += 1
    else:
        print('== X == INVALID LENGTH')

result = lst[0] * lst[1]

print('\n', lst)
print('\nRESULT:', result)