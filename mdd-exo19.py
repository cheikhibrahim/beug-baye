sa=0
a=int(input('entre un nombre'))
for d in range(1,a):
    if a%d==0:
        sa==sa+d
if sa==a:
    print(a,'est parfait')
else:
        print(a,'nest pas parfait')
