from Task4 import Sort4
def Sort10(Array):
        PositiveNumbers=[]
        NegativeNumbers=[]
        ReqArray=[]
        for i in range(len(Array)):
                  if(Array[i]>=0):
                     PositiveNumbers.append(Array[i])
                  elif(Array[i]<0):
                     NegativeNumbers.append(Array[i])   
        SortedPositiveArray=Sort4(PositiveNumbers)
        SortedNegativeArray=Sort4(NegativeNumbers)
        
        i,j=0,0
        while(i<len(SortedPositiveArray) and j<len(SortedNegativeArray)):
              ReqArray.append(SortedNegativeArray[j])
              ReqArray.append(SortedPositiveArray[i])
              i+=1
              j+=1
        if(len(ReqArray)<len(Array)):
              if(len(SortedPositiveArray)>len(SortedNegativeArray)):
                   while(i<len(SortedPositiveArray)):
                        ReqArray.append(SortedPositiveArray[i])   
                        i+=1
              else:
                   while(i<len(SortedNegativeArray)):
                        ReqArray.append(SortedNegativeArray[i])   
                        j+=1              

        return ReqArray

if __name__=="__main__":     

    Array= [10, -1, 9, 20, -3, -8, 22, 9, 7]      
    ReqArray=Sort10(Array)
    print(ReqArray)





