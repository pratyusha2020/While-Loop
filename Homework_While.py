n= int(input("Enter a number:"))
c=0
temp=n
while temp > 0:
    digit= temp%10
    c=c+1
    temp//=10
print(c)