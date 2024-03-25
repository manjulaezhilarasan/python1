stationnames=[]
stationcodes=[]
f1=open("railwaystations.txt","r")
for i in range(0,10,1):
    list1=f1.readline().split(",")
    stationnames.append(list1[0])
    stationcodes.append(list1[1])
print(stationnames)
print(stationcodes)

