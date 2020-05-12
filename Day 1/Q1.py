ar = [2, 3, 5, 4, 5, 3, 4]
res = ar[0] 
for i in range(1,len(ar)): 
    res = res ^ ar[i] 
print("Element occuring once is",res )
