a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

for A in a[1:20:2]:
    print(A)




a=[-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,0,0,10,9,8,7,6,5,4,3,2,1]
for q in a:
    if(q>0):
        print(q)
print("____________________________________")        
for q in a:
    if(q<0):
        print(q)
print("__________________________________________________")
eleman_sayisi = 0
for eleman in a:
    if(eleman==0):
        eleman_sayisi += 1

print("0 saysıs:{}".format(eleman_sayisi))



