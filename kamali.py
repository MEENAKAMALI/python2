a=[]
s=0
N=int(input("enter no of elementsN"));
for i in range(0,N):
        x=int(input("enter no of elementsX"));
        a.append(x);
        print(a);

K=int(input("enter no of elementsK"));
for r in range(0,K):
        s=s+a[r];
print(s);


