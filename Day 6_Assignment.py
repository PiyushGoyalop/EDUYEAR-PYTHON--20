a=[1,2,7,9,12,44,16,55,3,6,8,5,4,10,221122,121,353,111,252]
a1=["M","O","M"]

#1.) Count The NUmber Of Even And Odd Numbers
e,o=0,0
for i in a:
    if i%2==0:
        e+=1
    else:
        o+=1
print("There Are",e,"Even Numbers")
print("There Are",o,"Odd Numbers")


#2.)Min And Max without using min(), max() functions

s=sorted(a)
min_a=a[0]
max_a=a[-1]
i= a.index(min_a)
print("Minimum Number=",a[i])
i1= a.index(max_a)
print("Maximum Number=",a[i1])


#3.)To Check whether the list is palindrome or not
c1=a1[::-1]
if c1==a1:
    print(a1,"is palindrome")
else:
    print(a1,"is not Palindrome")



#4.)To Print Palindrome Numbers
for z in range(len(a)):
    b=a[z]
    c=str(b)
    c=c[::-1]
    c=int(c)
    if c==b:
        print(c,"Is Palindrome")

