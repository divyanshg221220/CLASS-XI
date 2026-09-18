#14.2
L=[("Wilhelm Conrad Röntgen","Physics",1901),("Ronald Ross","Medicine",1902),("Marie Curie","Physics",1903),("Ivan Pavlov","Medicine",1904),("Henryk Sienkiewicz","Literature",1905),("Theodore Roosevelt","Peace",1906)]
for i in range(1,len(L)):
    key=L[i]
    lastname=key[0].split()[-1]
    j=i-1
    while j>=0 and L[j][0].split()[-1]>lastname:
        L[j+1]=L[j]
        j-=1
    L[j+1]=key
print(L)