n=int(input("Enter a number:"))
s=0
for i in range(1,n):
    if n%i==0:
        s=s+i
print("Sum of factors=",s)
if s==n:
    print('Perfect number')
else:
     print('Not a Perfect number')
