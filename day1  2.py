a=[]
n=int(input("enter the number of elements"))
for i in range(1,n+1):
    b=int(input("enter the element"))
    a.append(b)
even=[]
odd=[]
for j in a:
    if(j%2==0):
        even.append(j)
    else:
        odd.append(j)
print("even number is",even)
print("odd number is",odd)
