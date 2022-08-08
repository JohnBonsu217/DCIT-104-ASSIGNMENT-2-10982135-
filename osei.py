from audioop import avg


s=0
j=0
for i in range (1,10000):
     if i%2==0:
      s=s+i
      j+=1
print(s/j)
   