list=[5,1,2,3,4]
for i in range (0,len(list)-1):
    for j in range (0,len(list)-i-1):
        if list[j]>list[j+1]:
            temp=list[j]
            list[j]=list[j+1]
            list[j+1]=temp
print(list)