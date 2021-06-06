#1.)
n=(int(input("Enter The Number:")))
def number(n):
    if n>1:
        for i in range(2,n):
            if n%i==0:
                print(n,"is not a Prime Number")
                break
            else:
                print(n, "is a Prime Number")
    else:
        print(n, "is a not Prime Number")
number(n)


#2.)Factorial

def f(n):
    if n==1 or n==0:
        return 1
    return n*f(n-1)
print(f("Enter A Number:"))
