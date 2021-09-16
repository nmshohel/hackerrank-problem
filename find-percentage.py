count=int(input())
for i in range(count):
    b=input()
    # thisdict = {}
    newdict={}
    c=b.split(" ")
    x=int(c[1])
    y=int(c[2])
    z=int(c[3])
    avg=(x+y+z)/3
    newdict[c[0]]=avg
name=input()
print(newdict[name])


