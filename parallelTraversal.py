l1=[1,2,3,4]
l2=list('abcd')
zippedl1l2 = [i for i in zip(l1,l2)]
setfromzipl1l2={x:y for (x,y) in zip(l1,l2)}
l3=[]
l4=l1+l2

for i in range(0,len(l1+l2)-1,2):
    l3.append((l1+l2)[i])



s = 'spam'
offset = 0
for item in s:
    offset+=1


b = 'bobtornton'
for (offset, item) in enumerate(b):
    print(item, 'appears at offset', offset)



