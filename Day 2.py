#VARIABLES TYPES AND ID'S
a=1632
b=2234
c=a+b
d=25.19
e="Hello PyCharm"
f=True
statement="""My Name Is PyCharm and I'm an IDE"""
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(statement)
print(id(a))
print(id(b))
print(id(c))
print(id(d))
print(type(d))
print(type(e))
print(type(f))
print(type(statement))


#PRINT TYPES
City="Delhi"
Occupation="Software Engineer"
print(City)
print(Occupation)


print("City =" , City)
print("Occupation =" , Occupation)

print("Bye\nBro!!")

print("City =" , City , end="__")
print("Occupation =" , Occupation)

print("City =" , City , end="\t")
print("Occupation =" , Occupation , end=" # ")
print("BYE PyCHARM")

print("City =" , City , end="")
print("Occupation =" , Occupation)

print(City , Occupation , sep="__")

print("I Live in" , City , "And I Work As A",Occupation , "There.")

print("I Live in" , City , " And I Work As A",Occupation , " There." , sep="")


#STRING FORMATTING
print("I Live in {} And I Work As A {} There.".format(City,Occupation))
print("I Live in {} And I Work As A {} There.".format(Occupation,City))

print(f"I Live in {City} And I Work As A {Occupation} There.")

Line="I Live in {} And I Work As A {} There.".format(City,Occupation)
Line1=f"I Live in {City} And I Work As A {Occupation} There."
print(Line)
print(Line1)


#TYPE CONVERSIONS

a=55
b=int(a)
c=str(a)
d=bool(a)
e=float(a)
print(a ,type(a))
print(b ,type(b))
print(c ,type(c))
print(d ,type(c))
print(e ,type(e))

f=12.2
g=int(f)
h=str(f)
i=bool(f)
j=float(f)
print(f ,type(f))
print(g ,type(g))
print(h ,type(h))
print(i ,type(i))
print(j ,type(j))

p=True
q=int(p)
r=str(p)
s=bool(p)
t=float(p)
print(p ,type(p))
print(q ,type(q))
print(r ,type(r))
print(s ,type(s))
print(t ,type(t))

k='Hi'
o=bool(k)
print(k ,type(k))
print(o ,type(o))