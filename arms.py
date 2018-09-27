x=int(input("enter the number"))

sum=0
temp=x
while temp>0:
    digit=temp%10
    sum+=digit**10
    temp//=10
if x==sum:
    print(x,"armstrong")
else:
    print(x,"not")
