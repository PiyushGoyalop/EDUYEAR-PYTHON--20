#1.) To print index of vowels

a=["a","b","c","d","e"]
b=["a","e","i","o","u"]
for i in a:
     if i in b:
         print(a.index(i))
     else:
         print("No Vowels")


#2.) To reverse the words of a string
str=["Hello","World","Happy","Birthday"]
str.reverse()
b=" ".join(str)
print(b)


#3.)to remove duplicate values without using set()
l=[1,2,3,3,2,4]
x=[]
for i in l:
    if i not in x:
        print(i)
        x.append(i)
print("Original List:",l)
print("List Without Duplicate elements:",x)