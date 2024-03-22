import os
dict1={
    "Sholay":["SanjeevKumar","AmitabhBuchchan","Dharmendra","Hemamalini","Jayabhaduri"],
    "Lagaan":["AmirKhan","GracySingh"],
    "Swadesh":["Sharukhan","Gayatri"]
    }
list1=list(dict1.keys())
list2=list(dict1.values())
root1="Movies/"
len1=len(list1)
for j in range(0,len1,1):
    list3=list2[j]
    for i in list3:
        os.makedirs(root1+list1[j]+"/"+i)
