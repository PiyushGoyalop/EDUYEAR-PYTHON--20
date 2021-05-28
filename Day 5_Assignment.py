""""#NUMBERS DIVISIBLE BY 5&7
a=int(input("Starting range:"))
b=int(input("Ending range:"))
for i in range(a,b+1):
    if i%5==0 or i%7==0:
        print(i)

#SUM OF THE SERIES
num=int(input("Enter the Number of Terms In The Series:"))
sum=0
for i in range(1,num+1):
    if i== num:
        e="="
    else:
        e="+"
    a="2"*i
    print(a, end=e)
    b=int(a)
    sum+=b
print(sum)




#Take Input And Print Sum Unless "Q" Is Pressed
s=0
while True:
    n=int(input("Enter The Number You Want To Add Up:"))
    s+=n
    v=input("\nPress Q to Quit\n or\nPress any key to Continue")
    if v=="q" or v=="Q":
        break
    else:
        continue
print("*"*50)
print("The Sum of The Entered Numbers is :",s)



#Factoiral Of A Number
a1=int(input("Enter The Number Whose Factorial You Want:"))
a=a1
i=1
while a!=0:
    i=i*a
    a=a-1
print("The Factorial of" ,a1,"is" ,i)

"""

# P-y-T-h-O-n i-S A G-o-O-d p-R-o-G-r-A-m-M-i-N-g l-A-n-G-u-A-g-E
st1 = 'python is a good programming language'
for i in range(len(st1)):
	end_val = '-'
	if st1[i] == ' ':
		end_val = ''
	if i == len(st1)-1:
		end_val = ''
	elif st1[i+1] == ' ':
		end_val = ''

	if i%2 == 0:
		print(st1[i].upper(), end=end_val)
	else:
		print(st1[i].lower(), end=end_val)
