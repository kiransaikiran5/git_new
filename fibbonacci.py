fno = 0
sno = 1
print(fno,sno,sep="\n")
res = fno+sno

while res < 100:
    print(res)
    fno = sno
    sno= res
    res = fno+sno