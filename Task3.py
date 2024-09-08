
def Minimum(Arr, StartInd, EndInd):
        Num=StartInd
        for x in range(StartInd,EndInd+1):
           
            if(Arr[x]<Arr[Num]):
                 Num = x
                 
        return Num
if __name__=="__main__":

    Arr= [3,4,7,8,0,1,23,-2,-5] 
    startingIndex=input("StartingIndex: ")
    endingIndex=input("EndingIndex: ")
    StartInd=int(startingIndex)
    EndInd=int(endingIndex)
    
    if(StartInd>=len(Arr) or EndInd>=len(Arr)):
         print("Index out of range")
    else:
         ReqInteger=Minimum(Arr,StartInd,EndInd)  
         print("Output: ",ReqInteger)

