a=[[1,2],
   [3,2]]
c=[[0,0],
   [0,0]]
for i in range(len(a)):
    for j in range(len(a)):
        c[i][j]=a[j][i]
for i in c:
    print(i)
