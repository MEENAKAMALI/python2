x = 900
y = 1000
print("Prime numbers between x and y")
for s in range(x,y):
   if s > 1:
       for i in range(2,s):
           if (s % i) == 0:
               break
       else:
           print(s)
