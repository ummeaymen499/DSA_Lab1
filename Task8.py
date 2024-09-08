A = [0,3,4,10,11] 
B = [1,8,13,24] 
SortedArray=[]
def SortedMerge(Arr1, Arr2):
    i,j=0,0
    while (i< len(Arr1) and j< len(Arr2)):
        if(Arr1[i]<Arr2[j]):
            SortedArray.append(Arr1[i])  
            i=i+1  
        elif(Arr1[i]>Arr2[j]):
            SortedArray.append(Arr2[j])
            j=j+1    
        elif(Arr1[i]==Arr2[j]):
            SortedArray.append(Arr1[i])
            i=i+1
            j=j+1
    if(len(SortedArray)<len(Arr1+Arr2)):
            while(j<len(Arr2)):
                SortedArray.append(Arr2[j])
                j=j+1
    else:
             while(i<len(Arr1)):   
                SortedArray.append(Arr2[i])
                i=i+1
    return SortedArray
Array=SortedMerge(A,B)
print(Array)

