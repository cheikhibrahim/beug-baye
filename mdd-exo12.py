a=int(input('entrer un nombre:a'))
b=int(input('entrer un nombre:b'))
if a>b:
    max=b
else:
        max=a
for i in range(1,min+1):
            if a%i==0 and b%i==0:
                PGDC=i
                print('le PGDCDE',a,'et',b,'est:*',PGDC)
