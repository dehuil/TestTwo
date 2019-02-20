mes=raw_input("dd")
l1=[]
l2=[]

if len(mes)%2!=0:
    print "y"
else:
    for x in range(0,len(mes)):
        if  x<len(mes):
            l1.append(mes[x])
        else:
            l2.append(mes[x])
if cmp(l1,l2)==1:
    print("bu")
else:
    print("shi")