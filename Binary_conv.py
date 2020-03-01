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
    myval = int(n%2)
    integer.append(myval)
    print(myval)
    myval1 = int(n/2)
    print(myval1)
    n = myval1
    print("myrefval:",n)
    if myval1 < 2:
        integer.append(myval1)
        break

print("integer is:",integer)
integer2 = list()
print("")
print("")
for i in range(0,len(integer),1):
    print(i)
    if integer == None:
        break
    value = integer.pop(-1)
    print("value is",value)
    integer2.insert(1,value)
    print("integer2 is:",integer2)
#------popping the list to rotate the values-----


print(integer)
print(integer2)
value = 0
print("")
print("")
for i,k in enumerate(integer2):
    ref = int(k)
    if ref == 0:
        value = value+0
    elif ref == 1:
        value = value + 10**((len(integer2)-1)-i)
    else:
        print("invalid data")
    print(10**((len(integer2)-1)-i))

print("myvalue is :",value)
