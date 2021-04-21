aa = []
bb = []

value = 0

for i in range(0,100) :
    aa.append(value)
    value += 2
    
print(aa[0:3])
print(aa[84:])

for i in range(0,100) :
    bb.append(value)
    value-= 2 

#or i in range(0,100) :
    ##print("aa : %d"%aa[i])
    ##print("bb : %d"%bb[i]) 

#print("%d : %d" %aa [-1], bb[-1])

aa = [10,20,30]
bb = [40,50,60]

cc = aa+bb
print(cc)

aa = [10,20,30,40,50,60,70]
aa[1] = 200
print(aa)
aa.sort()