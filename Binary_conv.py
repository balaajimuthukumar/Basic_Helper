import _io

#var = "sample string , /"
#print(var)
#file = open(r"C:/Users/mbala/Desktop/tatoo_img.jpg","rb+")
"""value = _io.TextIOWrapper.readlines(file)
print(len(value))
new = list()
pos  = 0
for i in value[1:len(value):1]:
    new.insert(pos,i)
    print(new)
    pos += 1"""
#---------------binary converter-------------------
integer = list()
n = int(input())
#for i in range(0,n):
#    integer.append(input())


while(1):
    refval = n
    myval = refval%2
    myval1 = n/2
    if refval < 2:
        break
    integer.append(myval)
    refval = myval1
    
print(integer)
value = 0
print("")
print("")
for i,k in enumerate(integer):
    ref = int(k)
    if ref == 0:
        value = value+0
    elif ref == 1:
        value = value + 10**((len(integer)-1)-i)
    else:
        print("invalid data")
    print(10**((len(integer)-1)-i))

print(value)
