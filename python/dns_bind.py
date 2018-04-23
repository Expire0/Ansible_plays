zone = open("domain.com.hosts", "r")
l=[]

for i in zone:
    l.append(i)


serial = l[3]
userserial = input("enter: ")
print(serial)
l.remove(l[3])
l.insert(3, userserial)


print(l[3])


for u in l:
    print(u)
