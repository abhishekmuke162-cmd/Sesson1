#Find Duplicate Element in a List
lst=[1,2,3,4,5,1,2,3]
duplicates=[]
for i in lst:
    if lst.count(i)>1 and i not in duplicates:
        duplicates.append(i)
print("Duplicate:",duplicates)
