from Models.Mask_Search import Mask_Search
a=Mask_Search()
Total='最近的藥局\n'
for i in (a.Return_Nearby()):
    Total+=str(i)+'\n'
print('''----------------------------------------------------------------------------------------''')
print(Total)