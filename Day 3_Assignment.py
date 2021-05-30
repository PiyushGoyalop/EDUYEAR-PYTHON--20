#Age Calcalutor
d=2021
e=int(input("Enter Your Year Of Birth:-"))
f=d-e
print("You are",f,"Years Old")

#SIMPLE CALCULATOR
A=float(input("Enter A Number:-"))
B=float(input("Enter Another Number:-"))
print("a + b = {}".format(A + B))
print("")
print("a - b = {}".format(A - B))
print("")
print("a * b = {}".format(A * B))
print("")
print("a / b = {}".format(A / B))
print("")
print("a % b = {}".format(A % B))
print("")
print("a // b = {}".format(A // B))
print("")
print("a ** b = {}".format(A ** B))





#Calaculator
a=float(input("Enter A Number:-"))
b=float(input("Enter Another Number:-"))
print('If You Want to add the two numbers use ""+""')
print("")
print('If You Want to subtract the two numbers use ""-""')
print("")
print('If You Want to multiply the two numbers use ""*""')
print("")
print('If You Want to divide the two numbers use ""/""')
print("")
print('If You Want the exponential multiplication use ""**""')
print("")
print('If You Want floor division use ""//""')
print("")
print('If You Want remainder use ""%""')
print("")
c=input("Enter The Operation You Need To Perform:")
if(c=='+'):
    print("The Result is",a+b)
elif(c=='-'):
    print("The Result is",a-b)
elif(c=='*'):
    print("The Result is",a*b)
elif(c=='/'):
    print("The Result is",a/b)
elif(c=='**'):
    print("The Result is",a**b)
elif(c=='//'):
    print("The Result is",a//b)
elif(c=='%'):
    print("The Result is",a%b)
else:
    print("INVALID OPERATOR")

print("BYEE")




